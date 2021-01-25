from django import forms
from django.utils.translation import gettext_lazy as _

from fobi.base import BaseFormFieldPluginForm, get_theme

__title__ = 'fobi.contrib.plugins.form_elements.security.' \
            'invisible_recaptcha.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('InvisibleRecaptchaInputForm',)

theme = get_theme(request=None, as_instance=True)


class InvisibleRecaptchaInputForm(forms.Form, BaseFormFieldPluginForm):
    """Form for ``InvisibleRecaptchaInputPlugin``."""

    plugin_data_fields = [
        ("label", ""),
        ("name", ""),
        ("required", True),
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
    required = forms.BooleanField(
        label=_("Required"),
        required=False,
        widget=forms.widgets.CheckboxInput(
            attrs={'class': theme.form_element_checkbox_html_class}
        )
    )
