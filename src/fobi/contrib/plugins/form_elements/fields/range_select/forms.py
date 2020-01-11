from django import forms
from django.utils.translation import gettext_lazy as _

from fobi.base import BaseFormFieldPluginForm, get_theme
from fobi.widgets import NumberInput

from .settings import (
    INITIAL,
    INITIAL_MAX_VALUE,
    INITIAL_MIN_VALUE,
    MAX_VALUE,
    MIN_VALUE,
    STEP
)

__title__ = 'fobi.contrib.plugins.form_elements.fields.range_select.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('RangeSelectInputForm',)

theme = get_theme(request=None, as_instance=True)


class RangeSelectInputForm(forms.Form, BaseFormFieldPluginForm):
    """Form for ``RangeSelectInputPlugin``."""

    plugin_data_fields = [
        ("label", ""),
        ("name", ""),
        ("min_value", INITIAL_MIN_VALUE),
        ("max_value", INITIAL_MAX_VALUE),
        ("step", STEP),
        ("help_text", ""),
        ("initial", INITIAL),
        ("required", False)
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
    min_value = forms.IntegerField(
        label=_("Min value"),
        required=True,
        initial=INITIAL_MIN_VALUE,
        widget=NumberInput(attrs={'class': theme.form_element_html_class}),
        min_value=MIN_VALUE,
        max_value=MAX_VALUE
    )
    max_value = forms.IntegerField(
        label=_("Max value"),
        required=True,
        initial=INITIAL_MAX_VALUE,
        widget=NumberInput(attrs={'class': theme.form_element_html_class}),
        min_value=MIN_VALUE,
        max_value=MAX_VALUE
    )
    step = forms.IntegerField(
        label=_("Step"),
        required=True,
        help_text=_("Step size"),
        widget=NumberInput(attrs={'class': theme.form_element_html_class}),
        min_value=MIN_VALUE,
        max_value=MAX_VALUE
    )
    help_text = forms.CharField(
        label=_("Help text"),
        required=False,
        widget=forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )
    )
    initial = forms.IntegerField(
        label=_("Initial"),
        required=False,
        widget=NumberInput(attrs={'class': theme.form_element_html_class}),
        min_value=MIN_VALUE,
        max_value=MAX_VALUE,
        initial=INITIAL
    )
    required = forms.BooleanField(
        label=_("Required"),
        required=False,
        widget=forms.widgets.CheckboxInput(
            attrs={'class': theme.form_element_checkbox_html_class}
        )
    )

    def clean(self):
        """Validating the values."""
        super(RangeSelectInputForm, self).clean()

        max_value = self.cleaned_data['max_value']
        min_value = self.cleaned_data['min_value']
        initial = self.cleaned_data['initial']
        step = self.cleaned_data['step']

        if max_value < min_value:
            self.add_error(
                'max_value',
                _("`max_value` should be > than `min_value`.")
            )

        if step > max_value - min_value:
            self.add_error(
                'step',
                _("`step` should be > than `max_value` - `min_value`.")
            )

        if max_value < initial:
            self.add_error(
                'initial',
                _("`max_value` should be >= than `initial`.")
            )

        if min_value > initial:
            self.add_error(
                'min_value',
                _("`initial` should be >= than `min_value`.")
            )
