from __future__ import absolute_import

from django import forms
from django.utils.translation import gettext_lazy as _

from fobi.base import BaseFormFieldPluginForm, get_theme

__title__ = "fobi.contrib.plugins.form_elements.fields.datetime.forms"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2019 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = ("DateTimeInputForm",)

theme = get_theme(request=None, as_instance=True)


class DateTimeInputForm(forms.Form, BaseFormFieldPluginForm):
    """Form for ``DateTimeInputPlugin``."""

    plugin_data_fields = [
        ("label", ""),
        ("name", ""),
        ("help_text", ""),
        ("initial", ""),
        ("input_formats", ""),
        ("required", False),
    ]

    label = forms.CharField(
        label=_("Label"),
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"class": theme.form_element_html_class}
        ),
    )
    name = forms.CharField(
        label=_("Name"),
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"class": theme.form_element_html_class}
        ),
    )
    help_text = forms.CharField(
        label=_("Help text"),
        required=False,
        widget=forms.widgets.Textarea(
            attrs={"class": theme.form_element_html_class}
        ),
    )
    initial = forms.DateTimeField(
        label=_("Initial"),
        required=False,
        widget=forms.widgets.DateTimeInput(
            attrs={"class": theme.form_element_html_class, "type": "datetime"}
        ),
    )
    input_formats = forms.CharField(
        label=_("Input formats"),
        required=False,
        widget=forms.widgets.TextInput(
            attrs={"class": theme.form_element_html_class}
        ),
    )
    required = forms.BooleanField(
        label=_("Required"),
        required=False,
        widget=forms.widgets.CheckboxInput(
            attrs={"class": theme.form_element_checkbox_html_class}
        ),
    )

    def clean_initial(self):
        """Clean the initial value."""
        initial = self.cleaned_data["initial"]
        try:
            return initial.strftime("%Y-%m-%d %H:%M:%S")
        except Exception as err:
            return initial
