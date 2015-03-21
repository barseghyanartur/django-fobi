from __future__ import absolute_import

__title__ = 'fobi.contrib.plugins.form_elements.fields.date.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DateInputForm',)

from django import forms
from django.utils.translation import ugettext_lazy as _

from fobi.base import BaseFormFieldPluginForm, get_theme

theme = get_theme(request=None, as_instance=True)

class DateInputForm(forms.Form, BaseFormFieldPluginForm):
    """
    Form for ``DateInputPlugin``.
    """
    plugin_data_fields = [
        ("label", ""),
        ("name", ""),
        ("help_text", ""),
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
    initial = forms.DateField(
        label = _("Initial"),
        required = False,
        widget = forms.widgets.DateInput(attrs={'class': theme.form_element_html_class,
                                                'type': 'date',})
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

    def clean_initial(self):
        """
        Clean the initial value.
        """
        initial = self.cleaned_data['initial']
        try:
            return initial.strftime("%Y-%m-%d")
        except Exception as err:
            return initial
