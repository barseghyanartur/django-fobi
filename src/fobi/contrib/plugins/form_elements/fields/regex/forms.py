from __future__ import absolute_import

from django import forms
from django.utils.translation import ugettext_lazy as _

from fobi.base import BaseFormFieldPluginForm, get_theme
from fobi.settings import DEFAULT_MAX_LENGTH

__title__ = 'fobi.contrib.plugins.form_elements.fields.regex.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('RegexInputForm',)

theme = get_theme(request=None, as_instance=True)


class RegexInputForm(forms.Form, BaseFormFieldPluginForm):
    """Form for ``RegexInputPlugin``."""

    plugin_data_fields = [
        ("label", ""),
        ("name", ""),
        ("help_text", ""),
        ("initial", ""),
        ("regex", ""),
        ("max_length", "255"),
        ("required", False),
        ("placeholder", ""),
    ]

    label = forms.CharField(
        label=_("Label"),
        required=True,
        widget=forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )
    )
    name = forms.CharField(
        label=_("Name"),
        required=True,
        widget=forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )
    )
    help_text = forms.CharField(
        label=_("Help text"),
        required=False,
        widget=forms.widgets.Textarea(
            attrs={'class': theme.form_element_html_class}
        )
    )
    regex = forms.RegexField(
        label=_("Regex"),
        required=True,
        widget=forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        ),
        regex="",
        help_text=_("Enter a valid regular expression. A couple of common "
                    "examples are listed below.<br/>"
                    "- Allow a single digit from 1 to 9 (example value 6): "
                    "<code>^[1-9]$</code><br/>"
                    "- Allow any combination of characters from a to z, "
                    "including capitals (example value abcXYZ):"
                    "<code>^([a-zA-Z])+$</code><br/>"
                    "- Allow a hex value (example value #a5c125:"
                    "<code>^#?([a-f0-9]{6}|[a-f0-9]{3})$</code><br/>")
    )
    initial = forms.CharField(
        label=_("Initial"),
        required=False,
        widget=forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )
    )
    max_length = forms.IntegerField(
        label=_("Max length"),
        required=True,
        widget=forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        ),
        initial=DEFAULT_MAX_LENGTH
    )
    required = forms.BooleanField(
        label=_("Required"),
        required=False,
        widget=forms.widgets.CheckboxInput(
            attrs={'class': theme.form_element_checkbox_html_class}
        )
    )
    placeholder = forms.CharField(
        label=_("Placeholder"),
        required=False,
        widget=forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )
    )
