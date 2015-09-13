from __future__ import absolute_import

__title__ = 'fobi.models'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    # Plugins
    'AbstractPluginModel', 'FormElement', 'FormHandler',

    # Entries
    'AbstractPluginEntry', 'FormWizardEntry', 'FormEntry', 'FormElementEntry',
    'FormFieldsetEntry', 'FormHandlerEntry',
)

import logging
logger = logging.getLogger(__name__)

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group
from django.conf import settings

from autoslug import AutoSlugField

from fobi.base import (
    get_registered_form_element_plugins, get_registered_form_handler_plugins,
    form_element_plugin_registry, form_handler_plugin_registry
    )

# ****************************************************************************
# **************** Safe User import for Django > 1.5, < 1.8 ******************
# ****************************************************************************
AUTH_USER_MODEL = settings.AUTH_USER_MODEL

# Note, that this may cause circular imports - thus the ``get_user_model``
# should be moved elsewhere (be used on the function/method level). For
# now leave commented and solve in future. Possible use the DjangoCMS solution
# https://github.com/divio/django-cms/blob/develop/cms/models/permissionmodels.py#L18

# Sanity checks.
#user = User()
#
#if not hasattr(user, 'username'):
#    from fobi.exceptions import ImproperlyConfigured
#    raise ImproperlyConfigured("Your custom user model ({0}.{1}) doesn't "
#                               "have ``username`` property, while "
#                               "``django-fobi`` relies on its' presence"
#                               ".".format(user._meta.app_label, user._meta.object_name))

# ****************************************************************************
# ****************************************************************************
# ****************************************************************************

# ****************************************************************************
# ****************************************************************************
# ******************************* Plugin models ******************************
# ****************************************************************************
# ****************************************************************************

class AbstractPluginModel(models.Model):
    """
    Abstract plugin model.

    Used when ``fobi.settings.RESTRICT_PLUGIN_ACCESS`` is set to True.

    :Properties:

        - `plugin_uid` (str): Plugin UID.
        - `users` (django.contrib.auth.models.User): White list of the users
          allowed to use the plugin.
        - `groups` (django.contrib.auth.models.Group): White list of the
          user groups allowed to use the plugin.
    """
    #plugin_uid = models.CharField(_("Plugin UID"), max_length=255,
    #                              unique=True, editable=False)
    users = models.ManyToManyField(AUTH_USER_MODEL, verbose_name=_("User"),
                                   blank=True)
    groups = models.ManyToManyField(Group, verbose_name=_("Group"), blank=True)

    class Meta:
        abstract = True

    #def __init__(self, *args, **kwargs):
    #    """
    #    Add choices.
    #    """
    #    super(AbstractPluginModel, self).__init__(*args, **kwargs)
    #    plugin_uid = self._meta.get_field('plugin_uid')
    #    plugin_uid._choices = self.get_registered_plugins()

    def get_registered_plugins(self):
        """
        """
        raise NotImplemented(
            "You should implement ``get_registered_plugins`` method!"
            )

    def __unicode__(self):
        return "{0} ({1})".format(
            dict(self.get_registered_plugins()).get(self.plugin_uid, ''),
            self.plugin_uid
            )

    def plugin_uid_code(self):
        """
        Mainly used in admin.
        """
        return self.plugin_uid
    plugin_uid_code.allow_tags = True
    plugin_uid_code.short_description = _('UID')

    def plugin_uid_admin(self):
        """
        Mainly used in admin.
        """
        return self.__unicode__()
    plugin_uid_admin.allow_tags = True
    plugin_uid_admin.short_description = _('Plugin')

    def groups_list(self):
        """
        Flat list (comma separated string) of groups allowed to use the
        plugin. Used in Django admin.

        :return string:
        """
        return ', '.join([g.name for g in self.groups.all()])
    groups_list.allow_tags = True
    groups_list.short_description = _('Groups')

    def users_list(self):
        """
        Flat list (comma separated string) of users allowed to use the
        plugin. Used in Django admin.

        :return string:
        """
        return ', '.join([u.get_username() for u in self.users.all()])
    users_list.allow_tags = True
    users_list.short_description = _('Users')


class FormElement(AbstractPluginModel):
    """
    Form field plugin. Used when ``fobi.settings.RESTRICT_PLUGIN_ACCESS``
    is set to True.

    :Properties:

        - `plugin_uid` (str): Plugin UID.
        - `users` (django.contrib.auth.models.User): White list of the users
          allowed to use the form element plugin.
        - `groups` (django.contrib.auth.models.Group): White list of the user
          groups allowed to use the form element plugin.
    """
    plugin_uid = models.CharField(
        _("Plugin UID"), max_length=255, unique=True, editable=False,
        choices=get_registered_form_element_plugins()
        )
    #objects = FormFieldPluginModelManager()

    class Meta:
        abstract = False
        verbose_name = _("Form element plugin")
        verbose_name_plural = _("Form element plugins")

    def get_registered_plugins(self):
        """
        Add choices.
        """
        return get_registered_form_element_plugins()


class FormHandler(AbstractPluginModel):
    """
    Form handler plugin. Used when ``fobi.settings.RESTRICT_PLUGIN_ACCESS``
    is set to True.

    :Properties:

        - `plugin_uid` (str): Plugin UID.
        - `users` (django.contrib.auth.models.User): White list of the users
          allowed to use the form handler plugin.
        - `groups` (django.contrib.auth.models.Group): White list of the
          user groups allowed to use the form handler plugin.
    """
    plugin_uid = models.CharField(
        _("Plugin UID"), max_length=255, unique=True, editable=False,
        choices=get_registered_form_handler_plugins()
        )
    #objects = FormHandlerPluginModelManager()

    class Meta:
        abstract = False
        verbose_name = _("Form handler plugin")
        verbose_name_plural = _("Form handler plugins")

    def get_registered_plugins(self):
        """
        Add choices.
        """
        return get_registered_form_handler_plugins()

# *****************************************************************************
# *****************************************************************************
# ******************************** Entry models *******************************
# *****************************************************************************
# *****************************************************************************

class FormWizardEntry(models.Model):
    """
    """
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_("User"))
    name = models.CharField(_("Name"), max_length=255)
    slug = AutoSlugField(populate_from='name', verbose_name=_("Slug"),
                         unique=True)
    is_public = models.BooleanField(
        _("Is public?"), default=False,
        help_text=_("Makes your form wizard visible to the public.")
        )
    is_cloneable = models.BooleanField(
        _("Is cloneable?"), default=False,
        help_text=_("Makes your form wizard cloneable by other users.")
        )

    class Meta:
        verbose_name = _("Form wizard entry")
        verbose_name_plural = _("Form wizard entries")
        unique_together = (('user', 'slug'), ('user', 'name'),)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        """
        Absolute URL, which goes to the dashboard workspace page.

        :return string:
        """
        return reverse('fobi.form_wizard', kwargs={'slug': self.slug})


class FormEntry(models.Model):
    """
    Form entry.

    :Properties:

        - `user` (django.contrib.auth.models.User: User owning the plugin.
        - `wizard` (str): Form wizard to which the form entry belongs to.
        - `name` (str): Form name.
        - `slug` (str): Form slug.
        - `description` (str): Form description.
        - `is_public` (bool): If set to True, is visible to public.
        - `is_clonable` (bool): If set to True, is clonable.
        - `position` (int): Ordering position in the wizard.
    """
    form_wizard_entry = models.ForeignKey(
        FormWizardEntry, verbose_name=_("Form wizard"), null=True, blank=True
        )
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_("User"))
    name = models.CharField(_("Name"), max_length=255)
    slug = AutoSlugField(
        populate_from='name', verbose_name=_("Slug"), unique=True
        )
    is_public = models.BooleanField(
        _("Public?"), default=False,
        help_text=_("Makes your form visible to the public.")
        )
    is_cloneable = models.BooleanField(
        _("Cloneable?"), default=False,
        help_text=_("Makes your form cloneable by other users.")
        )
    position = models.PositiveIntegerField(
        _("Position"), null=True, blank=True
        )
    success_page_title = models.CharField(
        _("Success page title"), max_length=255, null=True, blank=True,
        help_text=_("Custom message title to display after valid form is "
                    "submitted")
        )
    success_page_message = models.TextField(
        _("Success page body"), null=True, blank=True,
        help_text=_("Custom message text to display after valid form is "
                    "submitted")
        )
    action = models.CharField(
        _("Action"), max_length=255, null=True, blank=True,
        help_text=_("Custom form action; don't fill this field, unless really "
                    "necessary.")
        )
    created = models.DateTimeField(_("Created"), null=True, blank=True,
                                   auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), null=True, blank=True,
                                   auto_now=True)

    class Meta:
        verbose_name = _("Form entry")
        verbose_name_plural = _("Form entries")
        unique_together = (('user', 'slug'), ('user', 'name'),)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        """
        Absolute URL, which goes to the dashboard workspace page.

        :return string:
        """
        return reverse('fobi.form_entry', kwargs={'slug': self.slug})


class FormFieldsetEntry(models.Model):
    """
    Form fieldset entry.
    """
    form_entry = models.ForeignKey(FormEntry, verbose_name=_("Form"),
                                   null=True, blank=True)
    name = models.CharField(_("Name"), max_length=255)
    is_repeatable = models.BooleanField(
        _("Is repeatable?"), default=False,
        help_text=_("Makes your form fieldset repeatable.")
        )

    class Meta:
        verbose_name = _("Form fieldset entry")
        verbose_name_plural = _("Form fieldset entries")
        unique_together = (('form_entry', 'name'),)

    def __unicode__(self):
        return self.name


class AbstractPluginEntry(models.Model):
    """
    Abstract plugin entry.

    :Properties:

    - `form_entry` (fobi.models.FormEntry): Form to which the field plugin
      belongs to.
    - `plugin_uid` (str): Plugin UID.
    - `plugin_data` (str): JSON formatted string with plugin data.
    """
    form_entry = models.ForeignKey(FormEntry, verbose_name=_("Form"))
    plugin_data = models.TextField(verbose_name=_("Plugin data"), null=True,
                                   blank=True)

    class Meta:
        abstract = True

    #def __init__(self, *args, **kwargs):
    #    """
    #    Add choices.
    #    """
    #    super(AbstractPluginEntry, self).__init__(*args, **kwargs)
    #    plugin_uid = self._meta.get_field('plugin_uid')
    #    plugin_uid._choices = self.get_registered_plugins()

    def __unicode__(self):
        return "{0} plugin for user {1}".format(
            self.plugin_uid, self.form_entry.user
            )

    def get_registered_plugins(self):
        """
        """
        raise NotImplemented("You should implement ``get_registered_plugins``"
                             " method!")

    def get_registry(self):
        """
        """
        raise NotImplemented("You should implement ``get_registry`` method!")

    def get_plugin(self, fetch_related_data=False, request=None):
        """
        Gets the plugin class (by ``plugin_uid`` property), makes an instance
        of it, serves the data stored in ``plugin_data`` field (if available).
        Once all is done, plugin is ready to be rendered.

        :param bool fetch_related_data: When set to True, plugin is told to
            re-fetch all related data (stored in models or other sources).
        :return fobi.base.BasePlugin: Subclass of ``fobi.base.BasePlugin``.
        """
        # Getting form element plugin from registry.
        registry = self.get_registry()
        cls = registry.get(self.plugin_uid)

        if not cls:
            # No need to log here, since already logged in registry.
            if registry.fail_on_missing_plugin:
                err_msg = registry.plugin_not_found_error_message.format(
                    self.plugin_uid, registry.__class__
                    )
                raise registry.plugin_not_found_exception_cls(err_msg)
            return None

        # Creating plugin instance.
        plugin = cls(user=self.form_entry.user)

        # So that plugin has the request object
        plugin.request = request

        return plugin.process(
            self.plugin_data, fetch_related_data=fetch_related_data
            )

    def plugin_uid_code(self):
        """
        Mainly used in admin.
        """
        return self.plugin_uid
    plugin_uid_code.allow_tags = True
    plugin_uid_code.short_description = _('UID')

    def plugin_name(self):
        return dict(self.get_registered_plugins()).get(self.plugin_uid, '')


class FormElementEntry(AbstractPluginEntry):
    """
    Form field entry.

    :Properties:

    - `form` (fobi.models.FormEntry): Form to which the field plugin
      belongs to.
    - `plugin_uid` (str): Plugin UID.
    - `plugin_data` (str): JSON formatted string with plugin data.
    - `form_fieldset_entry`: Fieldset.
    - `position` (int): Entry position.
    """
    plugin_uid = models.CharField(_("Plugin name"), max_length=255,
                                  choices=get_registered_form_element_plugins())
    form_fieldset_entry = models.ForeignKey(FormFieldsetEntry,
                                            verbose_name=_("Form fieldset"),
                                            null=True, blank=True)
    position = models.PositiveIntegerField(_("Position"), null=True, blank=True)

    class Meta:
        abstract = False
        verbose_name = _("Form element entry")
        verbose_name_plural = _("Form element entries")
        ordering = ['position',]

    def get_registered_plugins(self):
        """
        Gets registered plugins.
        """
        return get_registered_form_element_plugins()

    def get_registry(self):
        return form_element_plugin_registry


class FormHandlerEntry(AbstractPluginEntry):
    """
    Form handler entry.

    :Properties:

        - `form_entry` (fobi.models.FormEntry): Form to which the field plugin
          belongs to.
        - `plugin_uid` (str): Plugin UID.
        - `plugin_data` (str): JSON formatted string with plugin data.
    """
    plugin_uid = models.CharField(_("Plugin name"), max_length=255,
                                  choices=get_registered_form_handler_plugins())

    class Meta:
        abstract = False
        verbose_name = _("Form handler entry")
        verbose_name_plural = _("Form handler entries")

    def get_registered_plugins(self):
        """
        Gets registered plugins.
        """
        return get_registered_form_handler_plugins()

    def get_registry(self):
        return form_handler_plugin_registry
