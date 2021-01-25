import datetime

from django import forms
from django.utils.translation import gettext_lazy as _
from django.utils.dateparse import parse_duration
from django.utils.duration import duration_string
from django.utils.encoding import force_text

from fobi.base import BaseFormFieldPluginForm, get_theme

__title__ = 'fobi.contrib.plugins.form_elements.fields.duration.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DurationInputForm',)

theme = get_theme(request=None, as_instance=True)


class DurationInputForm(forms.Form, BaseFormFieldPluginForm):
    """Form for ``DurationInputPlugin``."""

    plugin_data_fields = [
        ("label", ""),
        ("name", ""),
        ("help_text", ""),
        ("initial", ""),
        ("required", False),
        ("weeks", ""),
        ("days", ""),
        ("hours", ""),
        ("minutes", ""),
        ("seconds", ""),
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
    initial = forms.DurationField(
        label=_("Initial"),
        required=False,
        help_text=_("Enter string values. Example:<code><br/>"
                    "&nbsp;&nbsp;&nbsp;&nbsp;3 days, 23:10:53<br/>"
                    "&nbsp;&nbsp;&nbsp;&nbsp;09:30:00<br/>"
                    "</code><br/>"),
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

    placeholder = forms.CharField(
        label=_("Placeholder"),
        required=False,
        widget=forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )
    )

    def clean(self):
        """Validation."""
        cleaned_data = super(DurationInputForm, self).clean()

        initial = cleaned_data.get('initial')

        if initial not in forms.Field.empty_values:
            if not isinstance(initial, datetime.timedelta):
                if parse_duration(force_text(initial)) is None:
                    self.add_error(
                        'initial',
                        _("Enter a valid duration.")
                    )
            else:
                cleaned_data['initial'] = duration_string(initial)
        return cleaned_data
