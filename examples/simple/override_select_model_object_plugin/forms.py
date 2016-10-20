from django import forms
from django.utils.translation import ugettext_lazy as _

from fobi.base import BaseFormFieldPluginForm, get_theme
from fobi.helpers import get_registered_models
from fobi.contrib.plugins.form_elements.fields.select_model_object.settings \
    import IGNORED_MODELS

theme = get_theme(request=None, as_instance=True)

__all__ = ('SelectModelObjectInputForm',)


class SelectModelObjectInputForm(forms.Form, BaseFormFieldPluginForm):
    """Form for ``SelectModelObjectPlugin``."""

    plugin_data_fields = [
        ("label", ""),
        ("name", ""),
        ("model", ""),
        ("help_text", ""),
        ("initial", ""),
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
    model = forms.ChoiceField(
        label=_("Model"),
        choices=[],
        required=False,
        widget=forms.widgets.Select(
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
    initial = forms.CharField(
        label=_("Initial"),
        required=False,
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

    def __init__(self, *args, **kwargs):
        """In order to avoid static calls to `get_registered_models`."""
        super(SelectModelObjectInputForm, self).__init__(*args, **kwargs)
        self.fields['model'].choices = get_registered_models(
            ignore=IGNORED_MODELS
        )
