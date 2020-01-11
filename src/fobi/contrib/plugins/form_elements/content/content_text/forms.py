from django import forms
from django.forms.widgets import Textarea
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _

from fobi.base import BasePluginForm, get_theme

from .settings import ALLOWED_TAGS, ALLOWED_ATTRIBUTES

try:
    import bleach
    BLEACH_INSTALLED = True
except ImportError as err:
    BLEACH_INSTALLED = False

__title__ = 'fobi.contrib.plugins.form_elements.content.content_text.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ContentTextForm',)


theme = get_theme(request=None, as_instance=True)


class ContentTextForm(forms.Form, BasePluginForm):
    """Form for ``ContentTextPlugin``."""

    plugin_data_fields = [
        ("text", "")
    ]

    text = forms.CharField(
        label=_("Text"),
        required=True,
        widget=Textarea(attrs={'class': theme.form_element_html_class})
    )

    def clean_text(self):
        """Clean text value."""
        if BLEACH_INSTALLED:
            return bleach.clean(
                text=self.cleaned_data['text'],
                tags=ALLOWED_TAGS,
                attributes=ALLOWED_ATTRIBUTES,
                strip=True,
                strip_comments=True
            )
        else:
            return strip_tags(self.cleaned_data['text'])
