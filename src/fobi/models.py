from __future__ import absolute_import

import logging

from autoslug import AutoSlugField

from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from six import python_2_unicode_compatible

from .base import (
    form_element_plugin_registry,
    form_handler_plugin_registry,
    form_wizard_handler_plugin_registry,
    get_registered_form_element_plugins,
    get_registered_form_handler_plugins,
    get_registered_form_wizard_handler_plugins,
)
from .constants import WIZARD_TYPES, DEFAULT_WIZARD_TYPE

__title__ = 'fobi.models'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    # Plugins
    'AbstractPluginModel',
    'FormElement',
    'FormHandler',
    'FormWizardHandler',

    # Entries
    'AbstractFormWizardPluginEntry',
    'AbstractPluginEntry',
    'BaseAbstractPluginEntry',
    'FormElementEntry',
    'FormEntry',
    'FormFieldsetEntry',
    'FormHandlerEntry',
    'FormWizardEntry',
    'FormWizardFormEntry',
    'FormWizardHandlerEntry',
)


logger = logging.getLogger(__name__)

# ****************************************************************************
# **************** Safe User import for Django > 1.5, < 1.8 ******************
# ****************************************************************************
AUTH_USER_MODEL = settings.AUTH_USER_MODEL

# ****************************************************************************
# ****************************************************************************
# ****************************************************************************

# ****************************************************************************
# ****************************************************************************
# ******************************* Plugin models ******************************
# ****************************************************************************
# ****************************************************************************


@python_2_unicode_compatible
class AbstractPluginModel(models.Model):
    """Abstract plugin model.

    Used when ``fobi.settings.RESTRICT_PLUGIN_ACCESS`` is set to True.

    :Properties:

        - `plugin_uid` (str): Plugin UID.
        - `users` (django.contrib.auth.models.User): White list of the users
          allowed to use the plugin.
        - `groups` (django.contrib.auth.models.Group): White list of the
          user groups allowed to use the plugin.
    """

    # plugin_uid = models.CharField(_("Plugin UID"), max_length=255,
    #                              unique=True, editable=False)
    users = models.ManyToManyField(AUTH_USER_MODEL, verbose_name=_("User"),
                                   blank=True)
    groups = models.ManyToManyField(Group, verbose_name=_("Group"), blank=True)

    class Meta(object):
        """Meta class."""
        abstract = True

    # def __init__(self, *args, **kwargs):
    #    """
    #    Add choices.
    #    """
    #    super(AbstractPluginModel, self).__init__(*args, **kwargs)
    #    plugin_uid = self._meta.get_field('plugin_uid')
    #    plugin_uid._choices = self.get_registered_plugins()

    def get_registered_plugins(self):
        """Get registered plugins."""
        raise NotImplementedError(
            "You should implement ``get_registered_plugins`` method!"
        )

    def __str__(self):
        return "{0} ({1})".format(
            dict(self.get_registered_plugins()).get(self.plugin_uid, ''),
            self.plugin_uid
        )

    def plugin_uid_code(self):
        """Plugin uid code.

        Mainly used in admin.
        """
        return self.plugin_uid
    plugin_uid_code.allow_tags = True
    plugin_uid_code.short_description = _('UID')

    def plugin_uid_admin(self):
        """Plugin uid admin.

        Mainly used in admin.
        """
        return self.__str__()
    plugin_uid_admin.allow_tags = True
    plugin_uid_admin.short_description = _('Plugin')

    def groups_list(self):
        """Groups list.

        Flat list (comma separated string) of groups allowed to use the
        plugin. Used in Django admin.

        :return string:
        """
        return ', '.join([g.name for g in self.groups.all()])
    groups_list.allow_tags = True
    groups_list.short_description = _('Groups')

    def users_list(self):
        """Users list.

        Flat list (comma separated string) of users allowed to use the
        plugin. Used in Django admin.

        :return string:
        """
        return ', '.join([u.get_username() for u in self.users.all()])
    users_list.allow_tags = True
    users_list.short_description = _('Users')


class FormElement(AbstractPluginModel):
    """Form element.

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
        # choices=get_registered_form_element_plugins()
    )
    # objects = FormFieldPluginModelManager()

    class Meta(object):
        """Meta class."""
        abstract = False
        verbose_name = _("Form element plugin")
        verbose_name_plural = _("Form element plugins")

    def get_registered_plugins(self):
        """Add choices."""
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
        # choices=get_registered_form_handler_plugins()
    )
    # objects = FormHandlerPluginModelManager()

    class Meta(object):
        """Class meta."""
        abstract = False
        verbose_name = _("Form handler plugin")
        verbose_name_plural = _("Form handler plugins")

    def get_registered_plugins(self):
        """Add choices."""
        return get_registered_form_handler_plugins()


class FormWizardHandler(AbstractPluginModel):
    """
    Form wizard handler plugin. Used when
    ``fobi.settings.RESTRICT_PLUGIN_ACCESS`` is set to True.

    :Properties:

        - `plugin_uid` (str): Plugin UID.
        - `users` (django.contrib.auth.models.User): White list of the users
          allowed to use the form handler plugin.
        - `groups` (django.contrib.auth.models.Group): White list of the
          user groups allowed to use the form handler plugin.
    """
    plugin_uid = models.CharField(
        _("Plugin UID"), max_length=255, unique=True, editable=False,
        # choices=get_registered_form_handler_plugins()
    )

    # objects = FormHandlerPluginModelManager()

    class Meta(object):
        """Class meta."""
        abstract = False
        verbose_name = _("Form wizard handler plugin")
        verbose_name_plural = _("Form wizard handler plugins")

    def get_registered_plugins(self):
        """Add choices."""
        return get_registered_form_wizard_handler_plugins()

# *****************************************************************************
# *****************************************************************************
# ******************************** Entry models *******************************
# *****************************************************************************
# *****************************************************************************


@python_2_unicode_compatible
class FormWizardEntry(models.Model):
    """Form wizard entry."""

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE
    )
    name = models.CharField(_("Name"), max_length=255)
    title = models.CharField(
        _("Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Shown in templates if available.")
    )
    slug = AutoSlugField(
        populate_from='name',
        verbose_name=_("Slug"),
        unique=True
    )
    is_public = models.BooleanField(
        _("Is public?"),
        default=False,
        help_text=_("Makes your form wizard visible to the public.")
    )
    is_cloneable = models.BooleanField(
        _("Is cloneable?"),
        default=False,
        help_text=_("Makes your form wizard cloneable by other users.")
    )
    success_page_title = models.CharField(
        _("Success page title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Custom message title to display after valid form is "
                    "submitted")
    )
    success_page_message = models.TextField(
        _("Success page body"),
        null=True,
        blank=True,
        help_text=_("Custom message text to display after valid form is "
                    "submitted")
    )
    show_all_navigation_buttons = models.BooleanField(
        _("Show all navigation buttons?"),
        default=False,
        help_text=_("Show all navigation buttons.")
    )
    # action = models.CharField(
    #     _("Action"), max_length=255, null=True, blank=True,
    #     help_text=_("Custom form action; don't fill this field, unless "
    #                 "really necessary.")
    # )
    wizard_type = models.CharField(
        _("Type"),
        max_length=255,
        null=False,
        blank=False,
        choices=WIZARD_TYPES,
        default=DEFAULT_WIZARD_TYPE,
        help_text=_("Type of the form wizard.")
    )
    created = models.DateTimeField(
        _("Created"),
        null=True,
        blank=True,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        _("Updated"),
        null=True,
        blank=True,
        auto_now=True
    )

    class Meta(object):
        """Meta class."""

        verbose_name = _("Form wizard entry")
        verbose_name_plural = _("Form wizard entries")
        unique_together = (('user', 'slug'), ('user', 'name'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Get absolute URL.

        Absolute URL, which goes to the form-wizard view view.

        :return string:
        """
        return reverse(
            'fobi.view_form_wizard_entry',
            kwargs={'form_wizard_entry_slug': self.slug}
        )


@python_2_unicode_compatible
class FormEntry(models.Model):
    """Form entry."""

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE
    )
    name = models.CharField(_("Name"), max_length=255)
    title = models.CharField(
        _("Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Shown in templates if available.")
    )
    slug = AutoSlugField(
        populate_from='name', verbose_name=_("Slug"), unique=True
    )
    is_public = models.BooleanField(
        _("Public?"),
        default=False,
        help_text=_("Makes your form visible to the public.")
    )
    active_date_from = models.DateTimeField(
        _("Active from"),
        null=True,
        blank=True,
        help_text=_("Date and time when the form becomes active "
                    "in the format: 'YYYY-MM-DD HH:MM'. "
                    "Leave it blank to activate immediately.")
    )
    active_date_to = models.DateTimeField(
        _("Active until"),
        null=True,
        blank=True,
        help_text=_("Date and time when the form becomes inactive "
                    "in the format: 'YYYY-MM-DD HH:MM'. "
                    "Leave it blank to keep active forever.")
    )
    inactive_page_title = models.CharField(
        _("Inactive form page title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Custom message title to display if form is inactive.")
    )
    inactive_page_message = models.TextField(
        _("Inactive form page body"),
        null=True,
        blank=True,
        help_text=_("Custom message text to display if form is inactive.")
    )
    is_cloneable = models.BooleanField(
        _("Cloneable?"),
        default=False,
        help_text=_("Makes your form cloneable by other users.")
    )
    # position = models.PositiveIntegerField(
    #     _("Position"), null=True, blank=True
    # )
    success_page_title = models.CharField(
        _("Success page title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Custom message title to display after valid form is "
                    "submitted")
    )
    success_page_message = models.TextField(
        _("Success page body"),
        null=True,
        blank=True,
        help_text=_("Custom message text to display after valid form is "
                    "submitted")
    )
    action = models.CharField(
        _("Action"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Custom form action; don't fill this field, unless really "
                    "necessary.")
    )
    created = models.DateTimeField(
        _("Created"),
        null=True,
        blank=True,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        _("Updated"),
        null=True,
        blank=True,
        auto_now=True
    )

    class Meta(object):
        """Meta class."""

        verbose_name = _("Form entry")
        verbose_name_plural = _("Form entries")
        unique_together = (('user', 'slug'), ('user', 'name'),)

    def __str__(self):
        return self.name

    @property
    def is_active(self):
        active_from_ok = True
        active_to_ok = True
        now = timezone.now()

        if self.active_date_from and now < self.active_date_from:
            active_from_ok = False
        if self.active_date_to and now > self.active_date_to:
            active_to_ok = False

        if active_from_ok and active_to_ok:
            return True
        else:
            return False

    def get_absolute_url(self):
        """Get absolute URL.

        Absolute URL, which goes to the form-entry view view page.

        :return string:
        """
        return reverse(
            'fobi.view_form_entry',
            kwargs={'form_entry_slug': self.slug}
        )


@python_2_unicode_compatible
class FormWizardFormEntry(models.Model):
    """Form wizard form entry.

    A coupling point between `FormWizardEntry` and `FormEntry`."""

    form_wizard_entry = models.ForeignKey(
        FormWizardEntry,
        verbose_name=_("Form wizard entry"),
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    form_entry = models.ForeignKey(
        FormEntry,
        verbose_name=_("Form entry"),
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    position = models.PositiveIntegerField(
        _("Position"),
        null=True,
        blank=True
    )

    class Meta(object):
        """Meta class."""

        abstract = False
        verbose_name = _("Form wizard form entry")
        verbose_name_plural = _("Form wizard form entries")
        ordering = ['position']
        unique_together = (('form_wizard_entry', 'form_entry'),)

    def __str__(self):
        return "{0} - {1}".format(self.form_wizard_entry, self.form_entry)


@python_2_unicode_compatible
class FormFieldsetEntry(models.Model):
    """Form fieldset entry."""

    form_entry = models.ForeignKey(
        FormEntry,
        verbose_name=_("Form"),
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(_("Name"), max_length=255)
    is_repeatable = models.BooleanField(
        _("Is repeatable?"),
        default=False,
        help_text=_("Makes your form fieldset repeatable.")
    )

    class Meta(object):
        """Meta class."""

        verbose_name = _("Form fieldset entry")
        verbose_name_plural = _("Form fieldset entries")
        unique_together = (('form_entry', 'name'),)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class BaseAbstractPluginEntry(models.Model):
    """Base for AbstractPluginEntry.

    :Properties:

        - `plugin_data` (str): JSON formatted string with plugin data.
    """

    plugin_data = models.TextField(
        verbose_name=_("Plugin data"),
        null=True,
        blank=True
    )

    class Meta(object):
        """Meta class."""

        abstract = True

    def __str__(self):
        return "{0} plugin for user {1}".format(
            self.plugin_uid, self.entry_user
        )

    @property
    def entry_user(self):
        """Get user from the parent container."""

        raise NotImplementedError(
            "You should implement ``entry_user`` property!"
        )

    def get_registered_plugins(self):
        """Get registered plugins."""
        raise NotImplementedError(
            "You should implement ``get_registered_plugins`` method!"
        )

    def get_registry(self):
        """Get registry."""
        raise NotImplementedError(
            "You should implement ``get_registry`` method!"
        )

    def plugin_uid_code(self):
        """Plugin uid code.

        Mainly used in admin.
        """
        return self.plugin_uid

    plugin_uid_code.allow_tags = True
    plugin_uid_code.short_description = _('UID')

    def plugin_name(self):
        """Plugin name."""
        return dict(self.get_registered_plugins()).get(self.plugin_uid, '')

    def get_plugin(self, fetch_related_data=False, request=None):
        """Get plugin.

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
        plugin = cls(user=self.entry_user)

        # So that plugin has the request object
        plugin.request = request

        return plugin.process(
            self.plugin_data, fetch_related_data=fetch_related_data
        )


class AbstractPluginEntry(BaseAbstractPluginEntry):
    """Abstract plugin entry.

    :Properties:

    - `form_entry` (fobi.models.FormEntry): Form to which the field plugin
      belongs to.
    - `plugin_uid` (str): Plugin UID.
    - `plugin_data` (str): JSON formatted string with plugin data.
    """

    form_entry = models.ForeignKey(
        FormEntry,
        verbose_name=_("Form"),
        on_delete=models.CASCADE
    )

    class Meta(object):
        """Meta class."""

        abstract = True

    # def __init__(self, *args, **kwargs):
    #    """
    #    Add choices.
    #    """
    #    super(AbstractPluginEntry, self).__init__(*args, **kwargs)
    #    plugin_uid = self._meta.get_field('plugin_uid')
    #    plugin_uid._choices = self.get_registered_plugins()

    @property
    def entry_user(self):
        """Get user."""
        return self.form_entry.user


class FormElementEntry(AbstractPluginEntry):
    """Form field entry.

    :Properties:

    - `form` (fobi.models.FormEntry): Form to which the field plugin
      belongs to.
    - `plugin_uid` (str): Plugin UID.
    - `plugin_data` (str): JSON formatted string with plugin data.
    - `form_fieldset_entry`: Fieldset.
    - `position` (int): Entry position.
    """

    plugin_uid = models.CharField(
        _("Plugin name"), max_length=255,
        # choices=get_registered_form_element_plugins()
    )
    form_fieldset_entry = models.ForeignKey(
        FormFieldsetEntry,
        verbose_name=_("Form fieldset"),
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    position = models.PositiveIntegerField(
        _("Position"),
        null=True,
        blank=True
    )

    class Meta(object):
        """Meta class."""

        abstract = False
        verbose_name = _("Form element entry")
        verbose_name_plural = _("Form element entries")
        ordering = ['position']

    def get_registered_plugins(self):
        """Gets registered plugins."""
        return get_registered_form_element_plugins()

    def get_registry(self):
        """Get registry."""
        return form_element_plugin_registry


class FormHandlerEntry(AbstractPluginEntry):
    """Form handler entry.

    :Properties:

        - `form_entry` (fobi.models.FormEntry): Form to which the handler
          plugin belongs to.
        - `plugin_uid` (str): Plugin UID.
        - `plugin_data` (str): JSON formatted string with plugin data.
    """

    plugin_uid = models.CharField(
        _("Plugin name"),
        max_length=255,
        # choices=get_registered_form_handler_plugins()
    )

    class Meta(object):
        """Meta class."""

        abstract = False
        verbose_name = _("Form handler entry")
        verbose_name_plural = _("Form handler entries")

    def get_registered_plugins(self):
        """Gets registered plugins."""
        return get_registered_form_handler_plugins()

    def get_registry(self):
        """Get registry."""
        return form_handler_plugin_registry


class AbstractFormWizardPluginEntry(BaseAbstractPluginEntry):
    """Abstract form wizard plugin entry.

    :Properties:

        - `form_entry` (fobi.models.FormWizardEntry): FormWizard to which the
          plugin belongs to.
        - `plugin_uid` (str): Plugin UID.
        - `plugin_data` (str): JSON formatted string with plugin data.
    """

    form_wizard_entry = models.ForeignKey(
        FormWizardEntry,
        verbose_name=_("Form wizard"),
        on_delete=models.CASCADE
    )

    class Meta(object):
        """Meta class."""

        abstract = True

    @property
    def entry_user(self):
        """Get user."""
        return self.form_wizard_entry.user


class FormWizardHandlerEntry(AbstractFormWizardPluginEntry):
    """Form wizard handler entry.

    :Properties:

        - `form_wizard_entry` (fobi.models.FormWizardEntry): FormWizard to
          which the handler plugin belongs to.
        - `plugin_uid` (str): Plugin UID.
        - `plugin_data` (str): JSON formatted string with plugin data.
    """

    plugin_uid = models.CharField(
        _("Plugin name"),
        max_length=255,
        # choices=get_registered_form_handler_plugins()
    )

    class Meta(object):
        """Meta class."""

        abstract = False
        verbose_name = _("Form wizard handler entry")
        verbose_name_plural = _("Form wizard handler entries")

    def get_registered_plugins(self):
        """Gets registered plugins."""
        return get_registered_form_wizard_handler_plugins()

    def get_registry(self):
        """Get registry."""
        return form_wizard_handler_plugin_registry
