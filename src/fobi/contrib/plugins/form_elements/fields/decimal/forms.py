from __future__ import absolute_import

import decimal

from django import forms
from django.utils.translation import ugettext_lazy as _

from fobi.base import BaseFormFieldPluginForm, get_theme
from fobi.widgets import NumberInput

__title__ = 'fobi.contrib.plugins.form_elements.fields.decimal.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DecimalInputForm',)

theme = get_theme(request=None, as_instance=True)


class DecimalInputForm(forms.Form, BaseFormFieldPluginForm):
    """Form for ``DecimalInputPlugin``."""

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
    initial = forms.DecimalField(
        label=_("Initial"),
        required=False,
        widget=NumberInput(attrs={'class': theme.form_element_html_class})
    )
    max_digits = forms.IntegerField(
        label=_("Max digits"),
        required=False,
        widget=NumberInput(attrs={'class': theme.form_element_html_class})
    )
    decimal_places = forms.IntegerField(
        label=_("Decimal places"),
        required=False,
        widget=NumberInput(attrs={'class': theme.form_element_html_class})
    )
    min_value = forms.DecimalField(
        label=_("Min value"),
        required=False,
        widget=NumberInput(attrs={'class': theme.form_element_html_class})
    )
    max_value = forms.DecimalField(
        label=_("Max value"),
        required=False,
        widget=NumberInput(attrs={'class': theme.form_element_html_class})
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

    def clean(self):
        """Validating the values."""
        super(DecimalInputForm, self).clean()

        max_value = self.cleaned_data['max_value']
        min_value = self.cleaned_data['min_value']
        decimal_places = self.cleaned_data['decimal_places']
        max_digits = self.cleaned_data['max_digits']
        initial = self.cleaned_data['initial']

        if (
            max_value is not None and min_value is not None and
            max_value < min_value
        ):
            self.add_error(
                'max_value',
                _("`max_value` should be > than `min_value`.")
            )

        if max_value is not None and initial and max_value < initial:
            self.add_error(
                'initial',
                _("`max_value` should be >= than `initial`.")
            )

        if min_value is not None and initial and min_value > initial:
            self.add_error(
                'min_value',
                _("`initial` should be >= than `min_value`.")
            )

        try:
            self.quantize(initial, decimal_places, max_digits)
        except decimal.InvalidOperation as err:
            self.add_error(
                'max_digits',
                _("Quantize result has too many digits for current context")
            )

    def quantize(self, value, decimal_places, max_digits):
        """Quantize the decimal value to the configured precision."""
        if decimal_places is None or value is None:
            return value

        context = decimal.getcontext().copy()
        if max_digits is not None:
            context.prec = max_digits
        return value.quantize(
            decimal.Decimal('.1') ** decimal_places,
            context=context
        )
