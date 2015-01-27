__title__ = 'fobi.contrib.plugins.form_elements.fields.hidden.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('HiddenInputForm',)

from django import forms
from django.utils.translation import ugettext_lazy as _

from fobi.base import BaseFormFieldPluginForm, get_theme
from fobi.settings import DEFAULT_MAX_LENGTH

theme = get_theme(request=None, as_instance=True)

class HiddenInputForm(forms.Form, BaseFormFieldPluginForm):
    """
    Form for ``HiddenInputPlugin``.
    """
    plugin_data_fields = [
        ("label", ""),
        ("name", ""),
        ("initial", ""),
        ("max_length", "255"),
        ("required", False)
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
    initial = forms.CharField(
        label = _("Initial"),
        required = False,
        widget = forms.widgets.TextInput(attrs={'class': theme.form_element_html_class})
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
