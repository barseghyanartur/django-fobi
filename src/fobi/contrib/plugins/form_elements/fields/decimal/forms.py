from __future__ import absolute_import

__title__ = 'fobi.contrib.plugins.form_elements.fields.decimal.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DecimalInputForm',)

from django import forms
from django.utils.translation import ugettext_lazy as _

from fobi.base import BaseFormFieldPluginForm, get_theme
from fobi.widgets import NumberInput

theme = get_theme(request=None, as_instance=True)

class DecimalInputForm(forms.Form, BaseFormFieldPluginForm):
    """
    Form for ``DecimalInputPlugin``.
    """
    plugin_data_fields = [
        ("label", ""),
        ("name", ""),
        ("help_text", ""),
        ("initial", ""),
        ("max_digits", ""),
        ("decimal_places", ""),
        ("min_value", None),
        ("max_value", None),
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
    initial = forms.DecimalField(
        label = _("Initial"),
        required = False,
        widget = NumberInput(attrs={'class': theme.form_element_html_class})
        )
    max_digits = forms.IntegerField(
        label = _("Max digits"),
        required=False,
        widget = NumberInput(attrs={'class': theme.form_element_html_class})
        )
    decimal_places = forms.IntegerField(
        label = _("Decimal places"),
        required=False,
        widget = NumberInput(attrs={'class': theme.form_element_html_class})
        )
    min_value = forms.DecimalField(
        label = _("Min value"),
        required=False,
        widget = NumberInput(attrs={'class': theme.form_element_html_class})
        )
    max_value = forms.DecimalField(
        label = _("Max value"),
        required=False,
        widget = NumberInput(attrs={'class': theme.form_element_html_class})
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
