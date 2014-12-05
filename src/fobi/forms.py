__title__ = 'fobi.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'FormEntryForm', 'FormFieldsetEntryForm', 'FormElementEntryFormSet',
    'BulkChangeFormElementPluginsForm', 'BulkChangeFormHandlerPluginsForm',
)

from django.forms.models import modelformset_factory
from django import forms
from django.utils.translation import ugettext_lazy as _

from fobi.models import (
    # Plugins
    FormElement, FormHandler,

    # Entries
    FormEntry, FormFieldsetEntry, FormElementEntry
    )
from fobi.constants import ACTION_CHOICES
from fobi.base import get_theme

# *****************************************************************************
# *****************************************************************************
# ******************************* Entry forms *********************************
# *****************************************************************************
# *****************************************************************************

class FormEntryForm(forms.ModelForm):
    """
    Form for ``fobi.models.FormEntry`` model.
    """
    class Meta:
        model = FormEntry
        fields = ('name', 'is_public', 'success_page_title',
                  'success_page_message', 'action',) #'is_cloneable',

    def __init__(self, *args, **kwargs):
        super(FormEntryForm, self).__init__(*args, **kwargs)
        theme = get_theme(request=None, as_instance=True)

        self.fields['name'].widget = forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
            )

        self.fields['success_page_title'].widget = forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
            )

        self.fields['success_page_message'].widget = forms.widgets.Textarea(
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
        #self.fields['is_cloneable'].widget = forms.widgets.CheckboxInput(
        #    attrs={'data-customforms': 'disabled'}
        #    )

class FormFieldsetEntryForm(forms.ModelForm):
    """
    Form for ``fobi.models.FormFieldsetEntry`` model.
    """
    class Meta:
        model = FormFieldsetEntry
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super(FormFieldsetEntry, self).__init__(*args, **kwargs)
        theme = get_theme(request=None, as_instance=True)
        self.fields['name'].widget = forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
            )


FormElementEntryFormSet = modelformset_factory(
    FormElementEntry, fields=('position',), extra=0
    )

# *****************************************************************************
# *****************************************************************************
# *********************************** Base ************************************
# *****************************************************************************
# *****************************************************************************


class BaseBulkChangePluginsForm(forms.ModelForm):
    """
    Bulk change plugins form.

    - `selected_dashboard_plugins` (str): List of comma separated values to be
       changed.
    - `users_action` (int): For indicating wheither the users shall be appended
      to the dashbard plugins or replaced.
    - `groups_action` (int): For indicating wheither the groups shall be
      appended to the dashboard plugins or replaced.
    """
    selected_dashboard_plugins = forms.CharField(
        required=True, label=_("Selected plugins"),
        widget=forms.widgets.HiddenInput
        )
    users_action = forms.ChoiceField(
        required = False,
        label = _("Users action"),
        choices = ACTION_CHOICES,
        help_text = _("If set to ``replace``, the groups are replaced; "
                      "otherwise - appended.")
        )
    groups_action = forms.ChoiceField(
        required = False,
        label = _("Groups action"),
        choices = ACTION_CHOICES,
        help_text = _("If set to ``replace``, the groups are replaced; "
                      "otherwise - appended.")
        )

    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }

    def __init__(self, *args, **kwargs):
        super(BaseBulkChangePluginsForm, self).__init__(*args, **kwargs)
        self.fields['users'].required = False
        self.fields['groups'].required = False


class BulkChangeFormElementPluginsForm(BaseBulkChangePluginsForm):
    """
    """
    class Meta:
        model = FormElement
        fields = ['groups', 'groups_action', 'users', 'users_action',]


class BulkChangeFormHandlerPluginsForm(BaseBulkChangePluginsForm):
    """
    """
    class Meta:
        model = FormHandler
        fields = ['groups', 'groups_action', 'users', 'users_action',]
