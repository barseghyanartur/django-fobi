import socket

from six.moves.urllib.parse import urlparse

from django import forms
from django.forms.models import modelformset_factory
from django.utils.translation import gettext, gettext_lazy as _

# from nonefield.fields import NoneField

try:
    from ckeditor.widgets import CKEditorWidget
    CKEDITOR_INSTALLED = True
except ImportError:
    CKEDITOR_INSTALLED = False

from .base import (
    get_registered_form_element_plugins,
    get_registered_form_handler_plugins,
    # get_registered_form_wizard_handler_plugins,
    get_theme,
)
from .constants import ACTION_CHOICES
from .exceptions import ImproperlyConfigured
from .models import (
    # Form plugins
    FormElement,
    FormHandler,
    FormWizardHandler,

    # Form entries
    FormEntry,
    FormFieldsetEntry,
    FormElementEntry,
    FormHandlerEntry,

    # Form wizard entries
    FormWizardEntry,
    FormWizardHandlerEntry,
    FormWizardFormEntry
)
from .validators import url_exists

__title__ = 'fobi.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'BulkChangeFormElementPluginsForm',
    'BulkChangeFormHandlerPluginsForm',
    'BulkChangeFormWizardHandlerPluginsForm',
    'FormElementEntryForm',
    'FormElementEntryFormSet',
    'FormEntryForm',
    'FormFieldsetEntryForm',
    'FormHandlerEntryForm',
    'FormHandlerForm',
    'FormWizardEntryForm',
    'FormWizardFormEntryForm',
    'FormWizardFormEntryFormSet',
    'FormWizardHandlerEntryForm',
    'ImportFormEntryForm',
    'ImportFormWizardEntryForm',
)

# *****************************************************************************
# *****************************************************************************
# ******************************* Entry forms *********************************
# *****************************************************************************
# *****************************************************************************


class FormEntryForm(forms.ModelForm):
    """Form for ``fobi.models.FormEntry`` model."""

    class Meta(object):
        """Meta class."""

        model = FormEntry
        fields = (
            'name',
            'title',
            'is_public',
            'active_date_from',
            'active_date_to',
            'inactive_page_title',
            'inactive_page_message',
            'success_page_title',
            'success_page_message',
            'action',
            # 'is_cloneable',
        )

    def __init__(self, *args, **kwargs):
        """Constructor."""
        self.request = kwargs.pop('request', None)
        if self.request is None:
            raise ImproperlyConfigured(
                gettext(
                    "The {0} form requires a "
                    "request argument.".format(self.__class__.__name__)
                )
            )

        super(FormEntryForm, self).__init__(*args, **kwargs)
        theme = get_theme(request=None, as_instance=True)

        self.fields['name'].widget = forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )

        self.fields['title'].widget = forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )

        self.fields['success_page_title'].widget = forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )

        self.fields['inactive_page_title'].widget = forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )

        self.fields['active_date_from'].widget = forms.widgets.DateTimeInput(
            format='%Y-%m-%d %H:%M',
            attrs={'class': theme.form_element_html_class}
        )

        self.fields['active_date_to'].widget = forms.widgets.DateTimeInput(
            format='%Y-%m-%d %H:%M',
            attrs={'class': theme.form_element_html_class}
        )

        if CKEDITOR_INSTALLED:
            self.fields['success_page_message'].widget = CKEditorWidget(
                attrs={'class': theme.form_element_html_class}
            )
            self.fields['inactive_page_message'].widget = CKEditorWidget(
                attrs={'class': theme.form_element_html_class}
            )
        else:
            self.fields['success_page_message'].widget = \
                forms.widgets.Textarea(
                    attrs={'class': theme.form_element_html_class}
                )
            self.fields['inactive_page_message'].widget = \
                forms.widgets.Textarea(
                    attrs={'class': theme.form_element_html_class}
                )

        self.fields['action'].widget = forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )

        # At the moment this is done for Foundation 5 theme. Remove this once
        # it's possible for a theme to override this form. Alternatively, add
        # the attrs to the theme API.
        self.fields['is_public'].widget = forms.widgets.CheckboxInput(
            attrs={'data-customforms': 'disabled'}
        )
        # self.fields['is_cloneable'].widget = forms.widgets.CheckboxInput(
        #    attrs={'data-customforms': 'disabled'}
        # )

    def clean_action(self):
        """Validate the action (URL).

        Checks if URL exists.
        """
        url = self.cleaned_data['action']
        if url:
            full_url = url

            if not (url.startswith('http://') or url.startswith('https://')):
                full_url = self.request.build_absolute_uri(url)

            parsed_url = urlparse(full_url)

            local = False

            try:
                localhost = socket.gethostbyname('localhost')
            except Exception as err:
                localhost = '127.0.0.1'

            if parsed_url.hostname == 'testserver':
                local = True
            else:
                try:
                    host = socket.gethostbyname(parsed_url.hostname)

                    local = (localhost == host)
                except socket.gaierror as err:
                    pass

            if local:
                full_url = parsed_url.path

            if not url_exists(full_url, local=local):
                raise forms.ValidationError(
                    gettext("Invalid action URL {0}.").format(full_url)
                )

        return url


class FormFieldsetEntryForm(forms.ModelForm):
    """Form for ``fobi.models.FormFieldsetEntry`` model."""

    class Meta(object):
        """Meta class."""

        model = FormFieldsetEntry
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        """Constructor."""
        super(FormFieldsetEntryForm, self).__init__(*args, **kwargs)
        theme = get_theme(request=None, as_instance=True)
        self.fields['name'].widget = forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )


class FormElementForm(forms.ModelForm):
    """FormElement form."""

    # plugin_uid = forms.ChoiceField(
    #     choices=get_registered_form_element_plugins()
    # )

    class Meta(object):
        """Meta class."""

        model = FormElement
        fields = ('users', 'groups')


class FormElementEntryForm(forms.ModelForm):
    """FormElementEntry form."""

    plugin_uid = forms.ChoiceField(
        choices=get_registered_form_element_plugins()
    )

    class Meta(object):
        """Meta class."""

        model = FormElementEntry
        fields = ('form_entry', 'plugin_data', 'plugin_uid', 'position')


class _FormElementEntryForm(forms.ModelForm):
    """FormElementEntry form.

    To be used with `FormElementEntryFormSet` only.
    """

    class Meta(object):
        """Meta class."""

        model = FormElementEntry
        fields = ('position',)


FormElementEntryFormSet = modelformset_factory(
    FormElementEntry,
    fields=('position',),
    extra=0,
    form=_FormElementEntryForm
)


class FormHandlerForm(forms.ModelForm):
    """FormHandler form."""

    # plugin_uid = forms.ChoiceField(
    #     choices=get_registered_form_handler_plugins()
    # )

    class Meta(object):
        """Meta class."""

        model = FormHandler
        fields = ('users', 'groups')


class FormHandlerEntryForm(forms.ModelForm):
    """FormHandlerEntry form."""

    plugin_uid = forms.ChoiceField(
        choices=get_registered_form_handler_plugins()
    )

    class Meta(object):
        """Meta class."""

        model = FormHandlerEntry
        fields = ('form_entry', 'plugin_data', 'plugin_uid')


# *****************************************************************************
# *****************************************************************************
# ****************************** Wizard forms *********************************
# *****************************************************************************
# *****************************************************************************

class FormWizardFormEntryForm(forms.ModelForm):
    """FormWizardFormEntryForm form.


    """

    class Meta(object):
        """Meta class."""

        model = FormWizardFormEntry
        fields = ('form_wizard_entry', 'form_entry',)


class _FormWizardFormEntryForm(forms.ModelForm):
    """FormWizardFormEntryForm for formset.

    .. note::
        We have only two fields in the form: `form_entry` and `position`. The
        `form_entry` field is a `nonefield.NoneField`, thus - read only. The
        only changeable field is `position`.

    .. warning::

        To be used in `FormWizardFormEntryFormSet` only. If you need model
        form for `FormWizardFormEntry` model, make another one and leave this
        intact.
    """

    class Meta(object):
        """Meta class."""

        model = FormWizardFormEntry
        fields = ('position',)

    # def __init__(self, *args, **kwargs):
    #     """Constructor."""
    #     super(_FormWizardFormEntryForm, self).__init__(*args, **kwargs)
    #
    #     self.fields['position'].widget = forms.widgets.HiddenInput(
    #         attrs={'class': 'form-element-position'}
    #     )
    #     # self.fields['form_entry'] = NoneField(
    #     #     required=False,
    #     #     label=self.fields['form_entry'].label,
    #     #     initial=self.fields['form_entry'].initial,
    #     #     help_text=self.fields['form_entry'].help_text
    #     # )


FormWizardFormEntryFormSet = modelformset_factory(
    FormWizardFormEntry,
    fields=('position',),
    extra=0,
    form=_FormWizardFormEntryForm
)


class FormWizardEntryForm(forms.ModelForm):
    """Form for ``fobi.models.FormWizardEntry`` model."""

    class Meta(object):
        """Meta class."""

        model = FormWizardEntry
        fields = ('name', 'title', 'is_public', 'success_page_title',
                  'success_page_message', 'show_all_navigation_buttons',)
        # 'wizard_type'
        # 'action',
        # 'is_cloneable',

    def __init__(self, *args, **kwargs):
        """Constructor."""
        self.request = kwargs.pop('request', None)
        if self.request is None:
            raise ImproperlyConfigured(
                gettext(
                    "The {0} form requires a "
                    "request argument.".format(self.__class__.__name__)
                )
            )

        super(FormWizardEntryForm, self).__init__(*args, **kwargs)
        theme = get_theme(request=None, as_instance=True)

        self.fields['name'].widget = forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )

        self.fields['title'].widget = forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )

        self.fields['show_all_navigation_buttons'].widget = \
            forms.widgets.CheckboxInput(
                attrs={'data-customforms': 'disabled'}
            )

        self.fields['success_page_title'].widget = forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )

        self.fields['success_page_message'].widget = forms.widgets.Textarea(
            attrs={'class': theme.form_element_html_class}
        )

        # self.fields['action'].widget = forms.widgets.TextInput(
        #     attrs={'class': theme.form_element_html_class}
        # )

        # self.fields['wizard_type'].widget.attrs = {
        #     'class': theme.form_element_html_class
        # }

        # At the moment this is done for Foundation 5 theme. Remove this once
        # it's possible for a theme to override this form. Alternatively, add
        # the attrs to the theme API.
        self.fields['is_public'].widget = forms.widgets.CheckboxInput(
            attrs={'data-customforms': 'disabled'}
        )
        # self.fields['is_cloneable'].widget = forms.widgets.CheckboxInput(
        #    attrs={'data-customforms': 'disabled'}
        # )

    # def clean_action(self):
    #     """Validate the action (URL).
    #
    #     Checks if URL exists.
    #     """
    #     url = self.cleaned_data['action']
    #     if url:
    #         full_url = url
    #
    #         if not (url.startswith('http://') or url.startswith('https://')):
    #             full_url = self.request.build_absolute_uri(url)
    #
    #         parsed_url = urlparse(full_url)
    #
    #         local = False
    #
    #         try:
    #             localhost = socket.gethostbyname('localhost')
    #         except Exception as err:
    #             localhost = '127.0.0.1'
    #
    #         try:
    #             host = socket.gethostbyname(parsed_url.hostname)
    #
    #             local = (localhost == host)
    #         except socket.gaierror as err:
    #             pass
    #
    #         if local:
    #             full_url = parsed_url.path
    #
    #         if not url_exists(full_url, local=local):
    #             raise forms.ValidationError(
    #                 gettext("Invalid action URL {0}.").format(full_url)
    #             )
    #
    #     return url


class FormWizardHandlerEntryForm(forms.ModelForm):
    """FormWizardHandlerEntry form."""

    plugin_uid = forms.ChoiceField(
        choices=get_registered_form_handler_plugins()
    )

    class Meta(object):
        """Meta class."""

        model = FormWizardHandlerEntry
        fields = ('form_wizard_entry', 'plugin_data', 'plugin_uid')

# *****************************************************************************
# *****************************************************************************
# *********************************** Base ************************************
# *****************************************************************************
# *****************************************************************************


class BaseBulkChangePluginsForm(forms.ModelForm):
    """Bulk change plugins form.

    - `selected_plugins` (str): List of comma separated values to be
       changed.
    - `users_action` (int): For indicating wheither the users shall be appended
      to the dashbard plugins or replaced.
    - `groups_action` (int): For indicating wheither the groups shall be
      appended to the dashboard plugins or replaced.
    """

    selected_plugins = forms.CharField(
        required=True,
        label=_("Selected plugins"),
        widget=forms.widgets.HiddenInput
    )
    users_action = forms.ChoiceField(
        required=False,
        label=_("Users action"),
        choices=ACTION_CHOICES,
        help_text=_("If set to ``replace``, the groups are replaced; "
                    "otherwise - appended.")
    )
    groups_action = forms.ChoiceField(
        required=False,
        label=_("Groups action"),
        choices=ACTION_CHOICES,
        help_text=_("If set to ``replace``, the groups are replaced; "
                    "otherwise - appended.")
    )

    class Media(object):
        """Media class."""

        css = {
            'all': ('css/admin_custom.css',)
        }

    def __init__(self, *args, **kwargs):
        """Constructor."""
        super(BaseBulkChangePluginsForm, self).__init__(*args, **kwargs)
        self.fields['users'].required = False
        self.fields['groups'].required = False


class BulkChangeFormElementPluginsForm(BaseBulkChangePluginsForm):
    """Bulk change form element plugins form."""

    class Meta(object):
        """Meta class."""

        model = FormElement
        fields = ['groups', 'groups_action', 'users', 'users_action']


class BulkChangeFormHandlerPluginsForm(BaseBulkChangePluginsForm):
    """Bulk change form handler plugins form."""

    class Meta(object):
        """Meta class."""

        model = FormHandler
        fields = ['groups', 'groups_action', 'users', 'users_action']


class BulkChangeFormWizardHandlerPluginsForm(BaseBulkChangePluginsForm):
    """Bulk change form wizard handler plugins form."""

    class Meta(object):
        """Meta class."""

        model = FormWizardHandler
        fields = ['groups', 'groups_action', 'users', 'users_action']

# *****************************************************************************
# *****************************************************************************
# **************************** Import form entry ******************************
# *****************************************************************************
# *****************************************************************************


class ImportFormEntryForm(forms.Form):
    """Import form entry form."""

    file = forms.FileField(required=True, label=_("File"))
    # ignore_broken_form_element_entries = forms.BooleanField(
    #     required=False,
    #     label=_("Ignore broken form element entries"))
    # ignore_broken_form_handler_entries = forms.BooleanField(
    #     required=False,
    #     label=_("Ignore broken form handler entries"))


# *****************************************************************************
# *****************************************************************************
# ************************** Import form wizard entry *************************
# *****************************************************************************
# *****************************************************************************


class ImportFormWizardEntryForm(ImportFormEntryForm):
    """Import form entry wizard form."""
