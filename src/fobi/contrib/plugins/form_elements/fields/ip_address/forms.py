__title__ = 'fobi.contrib.plugins.form_elements.fields.ip_address.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('TextInputForm',)

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.validators import ip_address_validator_map

from fobi.base import BaseFormFieldPluginForm, get_theme
from fobi.settings import DEFAULT_MAX_LENGTH

theme = get_theme(request=None, as_instance=True)

class IPAddressInputForm(forms.Form, BaseFormFieldPluginForm):
    """
    Form for ``IPAddressInputPlugin``.
    """
    plugin_data_fields = [
        ("label", ""),
        ("name", ""),
        ("help_text", ""),
        ("initial", ""),
        ("protocol", ""),
        ("unpack_ipv4", False),
        ("max_length", "255"),
        ("required", False),
        ("placeholder", ""),
    ]

    label = forms.CharField(
        label = _("Label"),
        required = True,
        widget = forms.widgets.TextInput(attrs={'class': theme.form_element_html_class})
        )
    name = forms.CharField(
        label = _("Name"),
        required = True,
        widget = forms.widgets.TextInput(attrs={'class': theme.form_element_html_class})
        )
    help_text = forms.CharField(
        label = _("Help text"),
        required = False,
        widget = forms.widgets.Textarea(attrs={'class': theme.form_element_html_class})
        )
    initial = forms.CharField(
        label = _("Initial"),
        required = False,
        widget = forms.widgets.TextInput(attrs={'class': theme.form_element_html_class})
        )
    protocol = forms.ChoiceField(
        label = _("Protocol"),
        choices = [(pr, pr) for pr in ip_address_validator_map.keys()],
        required = True,
        widget = forms.widgets.Select(attrs={'class': theme.form_element_html_class})
        )
    unpack_ipv4 = forms.BooleanField(
        label = _("Unpack IPV4"),
        required = False,
        widget = forms.widgets.CheckboxInput(attrs={'class': theme.form_element_checkbox_html_class})
        )
    max_length = forms.IntegerField(
        label = _("Max length"),
        required = True,
        widget = forms.widgets.TextInput(attrs={'class': theme.form_element_html_class}),
        initial = DEFAULT_MAX_LENGTH
        )
    required = forms.BooleanField(
        label = _("Required"),
        required = False,
        widget = forms.widgets.CheckboxInput(attrs={'class': theme.form_element_checkbox_html_class})
        )
    placeholder = forms.CharField(
        label = _("Placeholder"),
        required = False,
        widget = forms.widgets.TextInput(attrs={'class': theme.form_element_html_class})
        )
