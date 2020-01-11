from django import forms
from django.utils.translation import gettext_lazy as _

from fobi.base import BasePluginForm, get_theme
# from fobi.widgets import NumberInput

from .settings import (
    FIT_METHODS_CHOICES,
    DEFAULT_FIT_METHOD,
    DEFAULT_SIZE,
    SIZES,
)

__title__ = 'fobi.contrib.plugins.form_elements.content.content_image_url.' \
            'forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ContentImageURLForm',)

theme = get_theme(request=None, as_instance=True)


class ContentImageURLForm(forms.Form, BasePluginForm):
    """Form for ``ContentImageURLPlugin``."""

    plugin_data_fields = [
        ("url", ""),
        ("alt", ""),
        ("fit_method", DEFAULT_FIT_METHOD),
        ("size", DEFAULT_SIZE),
    ]

    url = forms.URLField(
        label=_("URL"),
        required=True,
        widget=forms.widgets.URLInput(
            attrs={'class': theme.form_element_html_class}
        )
    )
    alt = forms.CharField(
        label=_("Alt text"),
        required=True,
        widget=forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )
    )
    fit_method = forms.ChoiceField(
        label=_("Fit method"),
        required=False,
        initial=DEFAULT_FIT_METHOD,
        choices=FIT_METHODS_CHOICES,
        widget=forms.widgets.Select(
            attrs={'class': theme.form_element_html_class}
        )
    )
    # width = forms.IntegerField(
    #     label=_("Width"),
    #     required=False,
    #     widget=NumberInput(
    #         attrs={'class': theme.form_element_html_class}
    #     )
    # )
    # height = forms.IntegerField(
    #     label=_("Height"),
    #     required=False,
    #     widget=NumberInput(
    #         attrs={'class': theme.form_element_html_class}
    #     )
    # )
    size = forms.ChoiceField(
        label=_("Size"),
        required=False,
        initial=DEFAULT_SIZE,
        choices=SIZES,
        widget=forms.widgets.Select(
            attrs={'class': theme.form_element_html_class}
        )
    )
