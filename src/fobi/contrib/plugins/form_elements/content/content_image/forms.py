__title__ = 'fobi.contrib.plugins.form_elements.content.content_image.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ContentImageForm',)

from django import forms
from django.utils.translation import ugettext_lazy as _

from fobi.base import BasePluginForm, get_theme
from fobi.helpers import handle_uploaded_file

from .settings import (
    FIT_METHODS_CHOICES, DEFAULT_FIT_METHOD, DEFAULT_SIZE, SIZES,
    IMAGES_UPLOAD_DIR
    )

theme = get_theme(request=None, as_instance=True)

class ContentImageForm(forms.Form, BasePluginForm):
    """
    Form for ``ContentImagePlugin``.
    """
    plugin_data_fields = [
        ("file", ""),
        ("alt", ""),
        ("fit_method", DEFAULT_FIT_METHOD),
        ("size", DEFAULT_SIZE),
    ]

    file = forms.ImageField(
        label = _("Image"),
        required = True,
        widget = forms.widgets.ClearableFileInput()
        #attrs={'class': theme.form_element_html_class}
        )
    alt = forms.CharField(
        label = _("Alt text"),
        required = True,
        widget = forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
            )
        )
    fit_method = forms.ChoiceField(
        label = _("Fit method"),
        required = False,
        initial = DEFAULT_FIT_METHOD,
        choices = FIT_METHODS_CHOICES,
        widget = forms.widgets.Select(
            attrs={'class': theme.form_element_html_class}
            )
        )
    size = forms.ChoiceField(
        label = _("Size"),
        required = False,
        initial = DEFAULT_SIZE,
        choices = SIZES,
        widget = forms.widgets.Select(
            attrs={'class': theme.form_element_html_class}
            )
        )

    def save_plugin_data(self, request=None):
        """
        Saving the plugin data and moving the file.
        """
        file_path = self.cleaned_data.get('file', None)
        if file_path:
            saved_image = handle_uploaded_file(IMAGES_UPLOAD_DIR, file_path)
            self.cleaned_data['file'] = saved_image
