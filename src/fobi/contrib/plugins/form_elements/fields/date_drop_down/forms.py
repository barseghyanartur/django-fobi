__title__ = 'fobi.contrib.plugins.form_elements.fields.date_drop_down.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DateDropDownInputForm',)

from django import forms
from django.utils.translation import ugettext_lazy as _

from fobi.base import BaseFormFieldPluginForm, get_theme

try:
    from django.forms.widgets import NumberInput
except ImportError:
    from django.forms.widgets import TextInput
    class NumberInput(TextInput):
        input_type = 'number'

theme = get_theme(request=None, as_instance=True)

class DateDropDownInputForm(forms.Form, BaseFormFieldPluginForm):
    """
    Form for ``DateDropDownInputPlugin``.
    """
    plugin_data_fields = [
        ("label", ""),
        ("name", ""),
        ("help_text", ""),
        ("year_min", ""),
        ("year_max", ""),
        ("initial", ""),
        ("input_formats", ""),
        ("required", False),
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
    year_min = forms.IntegerField(
        label = _("Minimum year value"),
        required = False,
        widget = NumberInput(attrs={'class': theme.form_element_html_class})
        )
    year_max = forms.IntegerField(
        label = _("Maximum year value"),
        required = False,
        widget = NumberInput(attrs={'class': theme.form_element_html_class})
        )
    initial = forms.CharField(
        label = _("Initial"),
        required = False,
        widget = forms.widgets.TextInput(attrs={'class': theme.form_element_html_class})
        )
    input_formats = forms.CharField(
        label = _("Input  formats"),
        required = False,
        widget = forms.widgets.TextInput(attrs={'class': theme.form_element_html_class})
        )
    required = forms.BooleanField(
        label = _("Required"),
        required = False,
        widget = forms.widgets.CheckboxInput(attrs={'class': theme.form_element_checkbox_html_class})
        )
