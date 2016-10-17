"""
Another helper module. This module can NOT be safely imported from any fobi
(sub)module - thus should be imported carefully.
"""
import logging

from six import PY3

from django.core.urlresolvers import reverse
from django.forms.widgets import TextInput
from django.utils.encoding import force_text
from django.utils.translation import ugettext

from .base import (
    form_element_plugin_registry,
    form_handler_plugin_registry,
    form_wizard_handler_plugin_registry,
    get_registered_form_element_plugin_uids,
    get_registered_form_element_plugins,
    ensure_autodiscover,
    get_registered_form_handler_plugin_uids,
    get_registered_form_wizard_handler_plugin_uids,
    get_theme,
    get_registered_form_handler_plugins,
    get_registered_form_wizard_handler_plugins,
    get_registered_form_element_plugins_grouped,

)
from .dynamic import assemble_form_class
from .helpers import update_plugin_data, safe_text
from .models import (
    FormElement,
    FormHandler,
    FormWizardHandler
)
from .settings import RESTRICT_PLUGIN_ACCESS, DEBUG

__title__ = 'fobi.utils'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'get_allowed_plugin_uids',
    'get_user_plugins',
    'get_user_plugin_uids',
    'sync_plugins',
    'get_allowed_form_element_plugin_uids',
    'get_user_form_element_plugins',
    'get_user_form_element_plugin_uids',
    'get_allowed_form_handler_plugin_uids',
    'get_allowed_form_wizard_handler_plugin_uids',
    'get_user_form_handler_plugins',
    'get_user_form_wizard_handler_plugins',
    'get_user_form_handler_plugin_uids',
    'get_user_form_wizard_handler_plugin_uids',
    'get_user_plugins_grouped',
    'get_user_form_element_plugins_grouped',
    'get_user_form_handler_plugins_grouped',
    'get_user_form_wizard_handler_plugins_grouped',
)

logger = logging.getLogger(__name__)


def sync_plugins():
    """Sync registered plugins.

    Syncs the registered plugin list with data in
    ``fobi.models.FormFieldPluginModel``,
    ``fobi.models.FormHandlerPluginModel`` and
    ``fobi.models.FormWizardHandlerPluginModel``.
    """
    ensure_autodiscover()

    def base_sync_plugins(get_plugin_uids_func, PluginModel):
        """Base sync plugins.

        :param callable get_plugin_uids_func:
        :param fobi.models.AbstractPluginModel PluginModel: Subclass of
            ``fobi.models.AbstractPluginModel``.
        """
        # If not in restricted mode, the quit.
        # TODO - perform a subclass check

        # TODO - perhaps uncomment this after everything works
        # if not RESTRICT_PLUGIN_ACCESS:
        #    return

        registered_plugins = set(get_plugin_uids_func())

        synced_plugins = set([p.plugin_uid for p in
                              PluginModel._default_manager.only('plugin_uid')])

        non_synced_plugins = registered_plugins - synced_plugins

        if not non_synced_plugins:
            return

        buf = []

        for plugin_uid in non_synced_plugins:
            buf.append(PluginModel(plugin_uid=plugin_uid))

        PluginModel._default_manager.bulk_create(buf)

    base_sync_plugins(get_registered_form_element_plugin_uids, FormElement)
    base_sync_plugins(get_registered_form_handler_plugin_uids, FormHandler)
    base_sync_plugins(get_registered_form_wizard_handler_plugin_uids,
                      FormWizardHandler)

# ****************************************************************************
# ****************************************************************************
# ********************************* Abstract *********************************
# ****************************************************************************
# ****************************************************************************


def get_allowed_plugin_uids(PluginModel, user):
    """Get allowed plugins uids for user given.

    :param fobi.models.AbstractPluginModel PluginModel: Subclass of
        ``fobi.models.AbstractPluginModel``.
    :param django.contrib.auth.models.User user:
    :return list:
    """
    try:
        queryset_groups = PluginModel._default_manager.filter(
            groups__in=user.groups.all()
        ).distinct()
        queryset_users = PluginModel._default_manager.filter(
            users=user
        ).distinct()
        queryset = queryset_groups | queryset_users
        queryset = queryset.only('plugin_uid')
        return [p.plugin_uid for p in queryset]
    except Exception as err:
        if DEBUG:
            logger.debug(err)
        return []


def get_user_plugins(get_allowed_plugin_uids_func,
                     get_registered_plugins_func,
                     registry,
                     user):
    """Get user plugins.

    Gets a list of user plugins in a form if tuple (plugin name, plugin
    description). If not yet autodiscovered, autodiscovers them.

    :param callable get_allowed_plugin_uids_func:
    :param callable get_registered_plugins_func:
    :param fobi.base.BaseRegistry registry: Subclass of
        ``fobi.base.BaseRegistry`` instance.
    :param django.contrib.auth.models.User user:
    :return list:
    """
    ensure_autodiscover()

    if not RESTRICT_PLUGIN_ACCESS or getattr(user, 'is_superuser', False):
        return get_registered_plugins_func()

    registered_plugins = []

    allowed_plugin_uids = get_allowed_plugin_uids_func(user)

    for uid, plugin in registry._registry.items():
        if uid in allowed_plugin_uids:
            plugin_name = safe_text(plugin.name)
            # if PY3:
            #    plugin_name = force_text(plugin.name, encoding='utf-8')
            # else:
            #    plugin_name = force_text(
            #        plugin.name, encoding='utf-8'
            #        ).encode('utf-8')
            registered_plugins.append((uid, plugin_name))

    return registered_plugins


def get_user_plugins_grouped(get_allowed_plugin_uids_func,
                             get_registered_plugins_grouped_func,
                             registry,
                             user,
                             sort_items=True):
    """Get user plugins grouped.

    :param callable get_allowed_plugin_uids_func:
    :param callable get_registered_plugins_grouped_func:
    :param fobi.base.BaseRegistry registry: Subclass of
        ``fobi.base.BaseRegistry`` instance.
    :param django.contrib.auth.models.User user:
    :param bool sort_items:
    :return dict:
    """
    ensure_autodiscover()

    if not RESTRICT_PLUGIN_ACCESS or getattr(user, 'is_superuser', False):
        return get_registered_plugins_grouped_func()

    registered_plugins = {}

    allowed_plugin_uids = get_allowed_plugin_uids_func(user)

    for uid, plugin in registry._registry.items():
        if uid in allowed_plugin_uids:
            if PY3:
                plugin_name = force_text(plugin.name, encoding='utf-8')
                plugin_group = force_text(plugin.group, encoding='utf-8')
            else:
                plugin_name = force_text(
                    plugin.name, encoding='utf-8'
                ).encode('utf-8')
                plugin_group = force_text(
                    plugin.group, encoding='utf-8'
                ).encode('utf-8')

            if plugin_group not in registered_plugins:
                registered_plugins[plugin_group] = []
            registered_plugins[plugin_group].append((uid, plugin_name))

    if sort_items:
        for key, prop in registered_plugins.items():
            prop.sort()

    return registered_plugins


def get_user_plugin_uids(get_allowed_plugin_uids_func,
                         get_registered_plugin_uids_func,
                         registry,
                         user):
    """Gets a list of user plugin uids as a list.

    If not yet auto-discovered, auto-discovers them.

    :param callable get_allowed_plugin_uids_func:
    :param callable get_registered_plugin_uids_func:
    :param fobi.base.BaseRegistry registry: Subclass of
        ``fobi.base.BaseRegistry`` instance.
    :param django.contrib.auth.models.User user:
    :return list:
    """
    ensure_autodiscover()

    if not RESTRICT_PLUGIN_ACCESS or getattr(user, 'is_superuser', False):
        return get_registered_plugin_uids_func()

    registered_plugins = []

    allowed_plugin_uids = get_allowed_plugin_uids_func(user)

    for uid, plugin in registry._registry.items():
        if uid in allowed_plugin_uids:
            registered_plugins.append(uid)

    return registered_plugins


def get_user_handler_plugins(get_allowed_handler_plugin_uids,
                             get_registered_handler_plugins,
                             handler_plugin_registry,
                             user,
                             exclude_used_singles=False,
                             used_handler_plugin_uids=[]):
    """Get list of plugins allowed for user.

    :param get_allowed_handler_plugin_uids:
    :param get_registered_handler_plugins:
    :param handler_plugin_registry:
    :param django.contrib.auth.models.User user:
    :param bool exclude_used_singles:
    :param list used_handler_plugin_uids:
    :return list:
    """
    user_handler_plugins = get_user_plugins(
        get_allowed_handler_plugin_uids,
        get_registered_handler_plugins,
        handler_plugin_registry,
        user
    )
    user_handler_plugin_uids = [plugin_uid
                                for (plugin_uid, plugin_name)
                                in user_handler_plugins]

    if exclude_used_singles and used_handler_plugin_uids:
        # Get all registered form handler plugins (as instances)
        registered_handler_plugins = \
            get_registered_handler_plugins(as_instances=True)

        # Check if we need to reduce the list of allowed plugins if they have
        # been marked to be used once per form and have been used already in
        # the current form.
        for plugin_uid, plugin \
                in registered_handler_plugins.items():

            if plugin.uid in user_handler_plugin_uids \
               and not plugin.allow_multiple \
               and plugin.uid in used_handler_plugin_uids:

                # Remove the plugin so that we don't get links to add it
                # in the UI.
                plugin_name = safe_text(plugin.name)
                user_handler_plugins.remove(
                    (plugin.uid, plugin_name)
                )

    return user_handler_plugins

# ****************************************************************************
# ****************************************************************************
# **************************** Form field specific ***************************
# ****************************************************************************
# ****************************************************************************


def get_allowed_form_element_plugin_uids(user):
    """Get allowed form element plugin uids."""
    return get_allowed_plugin_uids(FormElement, user)


def get_user_form_element_plugins(user):
    """Get user form element plugins."""
    return get_user_plugins(
        get_allowed_form_element_plugin_uids,
        get_registered_form_element_plugins,
        form_element_plugin_registry,
        user
    )


def get_user_form_element_plugins_grouped(user):
    """Get user form element plugins grouped."""
    return get_user_plugins_grouped(
        get_allowed_form_element_plugin_uids,
        get_registered_form_element_plugins_grouped,
        form_element_plugin_registry,
        user
    )


def get_user_form_field_plugin_uids(user):
    """Get user form field plugin uids."""
    return get_user_plugin_uids(
        get_allowed_form_element_plugin_uids,
        get_registered_form_element_plugin_uids,
        form_element_plugin_registry,
        user
    )

# ****************************************************************************
# ****************************************************************************
# *************************** Form handler specific **************************
# ****************************************************************************
# ****************************************************************************


def get_allowed_form_handler_plugin_uids(user):
    """Get allowed form handler plugin uids."""
    return get_allowed_plugin_uids(FormHandler, user)


def get_user_form_handler_plugins(user,
                                  exclude_used_singles=False,
                                  used_form_handler_plugin_uids=[]):
    """Get list of plugins allowed for user.

    :param django.contrib.auth.models.User user:
    :param bool exclude_used_singles:
    :param list used_form_handler_plugin_uids:
    :return list:
    """
    return get_user_handler_plugins(
        get_allowed_form_handler_plugin_uids,
        get_registered_form_handler_plugins,
        form_handler_plugin_registry,
        user,
        exclude_used_singles=exclude_used_singles,
        used_handler_plugin_uids=used_form_handler_plugin_uids
    )


# def get_user_form_handler_plugins(user,
#                                   exclude_used_singles=False,
#                                   used_form_handler_plugin_uids=[]):
#     """Get list of plugins allowed for user.
#
#     :param django.contrib.auth.models.User user:
#     :param bool exclude_used_singles:
#     :param list used_form_handler_plugin_uids:
#     :return list:
#     """
#     user_form_handler_plugins = get_user_plugins(
#         get_allowed_form_handler_plugin_uids,
#         get_registered_form_handler_plugins,
#         form_handler_plugin_registry,
#         user
#     )
#     user_form_handler_plugin_uids = [plugin_uid
#                                      for (plugin_uid, plugin_name)
#                                      in user_form_handler_plugins]
#
#     if exclude_used_singles and used_form_handler_plugin_uids:
#         # Get all registered form handler plugins (as instances)
#         registered_form_handler_plugins = \
#             get_registered_form_handler_plugins(as_instances=True)
#
#         # Check if we need to reduce the list of allowed plugins if they have
#         # been marked to be used once per form and have been used already in
#         # the current form.
#         for plugin_uid, plugin \
#                 in registered_form_handler_plugins.items():
#
#             if plugin.uid in user_form_handler_plugin_uids \
#                and not plugin.allow_multiple \
#                and plugin.uid in used_form_handler_plugin_uids:
#
#                 # Remove the plugin so that we don't get links to add it
#                 # in the UI.
#                 plugin_name = safe_text(plugin.name)
#                 user_form_handler_plugins.remove(
#                     (plugin.uid, plugin_name)
#                 )
#
#     return user_form_handler_plugins


def get_user_form_handler_plugins_grouped(user):
    """Get user form handler plugins grouped."""
    return get_user_plugins_grouped(
        get_allowed_form_handler_plugin_uids,
        get_registered_form_handler_plugins,
        form_handler_plugin_registry,
        user
    )


def get_user_form_handler_plugin_uids(user):
    """Get user form handler plugin uids."""
    return get_user_plugin_uids(
        get_allowed_form_handler_plugin_uids,
        get_registered_form_handler_plugin_uids,
        form_handler_plugin_registry,
        user
    )

# ****************************************************************************
# ****************************************************************************
# ************************* Form wizard handler specific *********************
# ****************************************************************************
# ****************************************************************************


def get_allowed_form_wizard_handler_plugin_uids(user):
    """Get allowed form wizard handler plugin uids."""
    return get_allowed_plugin_uids(FormWizardHandler, user)


def get_user_form_wizard_handler_plugins(
        user,
        exclude_used_singles=False,
        used_form_wizard_handler_plugin_uids=[]):
    """Get list of plugins allowed for user.

    :param django.contrib.auth.models.User user:
    :param bool exclude_used_singles:
    :param list used_form_wizard_handler_plugin_uids:
    :return list:
    """
    return get_user_handler_plugins(
        get_allowed_form_wizard_handler_plugin_uids,
        get_registered_form_wizard_handler_plugins,
        form_wizard_handler_plugin_registry,
        user,
        exclude_used_singles=exclude_used_singles,
        used_handler_plugin_uids=used_form_wizard_handler_plugin_uids
    )


def get_user_form_wizard_handler_plugins_grouped(user):
    """Get user form wizard handler plugins grouped."""
    return get_user_plugins_grouped(
        get_allowed_form_wizard_handler_plugin_uids,
        get_registered_form_wizard_handler_plugins,
        form_wizard_handler_plugin_registry,
        user
    )


def get_user_form_wizard_handler_plugin_uids(user):
    """Get user form handler plugin uids."""
    return get_user_plugin_uids(
        get_allowed_form_wizard_handler_plugin_uids,
        get_registered_form_wizard_handler_plugin_uids,
        form_wizard_handler_plugin_registry,
        user
    )

# ****************************************************************************
# ****************************************************************************
# *************************** Dynamic forms specific *************************
# ****************************************************************************
# ****************************************************************************


def get_assembled_form(form_entry, request=None):
    """Get assembled form.

    :param fobi.models.FormEntry form_entry:
    :param django.http.HttpRequest request:
    :return django.forms.Form:
    """
    # TODO
    FormClass = assemble_form_class(form_entry, request=request)
    form = FormClass()
    return form


def append_edit_and_delete_links_to_field(form_element_plugin,
                                          form_element_entry,
                                          origin=None,
                                          extra={},
                                          widget_cls=None):
    """Append edit and delete links to the field.

    Should return dictionary, which would be used to update default kwargs
    of form fields.

    The hidden inputs `form-{counter}-position` and `form-{counter}-id` are
    for saving the ordering of the elements (`position` field).

    :return dict:
    """
    theme = get_theme(as_instance=True)
    PluginForm = form_element_plugin.get_form()
    counter = extra.get('counter')
    edit_url = reverse(
        'fobi.edit_form_element_entry',
        kwargs={'form_element_entry_id': form_element_entry.pk}
    )

    edit_option_html = theme.edit_form_entry_edit_option_html().format(
        edit_url=edit_url,
        edit_text=safe_text(ugettext("Edit")),
        )
    help_text_extra = theme.edit_form_entry_help_text_extra().format(
        edit_option_html=edit_option_html if PluginForm else '',
        delete_url=reverse(
            'fobi.delete_form_element_entry',
            kwargs={'form_element_entry_id': form_element_entry.pk}
        ),
        delete_text=safe_text(ugettext("Delete")),
        form_element_pk=form_element_entry.pk,
        form_element_position=form_element_entry.position,
        counter=counter
    )
    try:
        help_text = safe_text(form_element_plugin.data.help_text)
    except:
        help_text = ''

    d = {
        'help_text': "{0} {1}".format(help_text, help_text_extra),
    }

    label = safe_text(getattr(form_element_plugin.data, 'label', ''))
    d.update(
        {'label': "{0} ({1})".format(label,
                                     safe_text(form_element_plugin.name))}
    )

    # if 'hidden' == form_element_plugin.uid:
    #    d.update(
    #        {
    #            'widget': TextInput(
    #                attrs={'class': theme.form_element_html_class}
    #            )
    #        }
    #    )
    if widget_cls:
        d.update(
            {
                'widget': widget_cls(
                    attrs={'class': theme.form_element_html_class}
                )
            }
        )
    elif form_element_plugin.is_hidden:
        d.update(
            {
                'widget': TextInput(
                    attrs={'class': theme.form_element_html_class}
                )
            }
        )

    return d


def update_plugin_data_for_entries(entries=None,
                                   request=None,
                                   entry_model_cls=None):
    """Update plugin data for entries.

    Updates the plugin data for all entries of all users. Rules for update
    are specified in the plugin itself.

    :param iterable entries: If given, is used to iterate through and update
        the plugin data. If left empty, all entries will be updated.
    :param django.http.HttpRequest request:
    :param fobi.models.AbstractPluginEntry entry_model_cls: Sublcass of
        the ``fobi.models.AbstractPluginEntry``.
    """
    if entries is None and entry_model_cls is not None:
        entries = entry_model_cls._default_manager.all()

    if not entries:
        return None

    for entry in entries:
        update_plugin_data(entry, request=request)

    logger.debug(entries)
