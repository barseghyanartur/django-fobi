from ckeditor.widgets import CKEditorWidget
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from fobi.base import BasePluginForm, get_theme

try:
    import bleach

    BLEACH_INSTALLED = True
    BLEACH_VERSION = bleach.__version__
except ImportError:
    BLEACH_INSTALLED = False
    BLEACH_VERSION = False
   

__title__ = "fobi.contrib.plugins.form_elements.content.content_richtext.forms"
__author__ = "Frantisek Holop <fholop@ripe.net>"
__copyright__ = "RIPE NCC"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = ("ContentRichTextForm",)


theme = get_theme(request=None, as_instance=True)


class ContentRichTextForm(forms.Form, BasePluginForm):
    """ContentRichTextForm."""

    plugin_data_fields = [("text", "")]

    text = forms.CharField(
        label=_("Text"),
        required=True,
        widget=CKEditorWidget(),
    )

    def clean_text(self):
        if not BLEACH_INSTALLED:
            return self.cleaned_data["text"]

        allowed_tags = getattr(
            settings,
            "FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_TAGS",
            bleach.ALLOWED_TAGS,
        )
        allowed_attrs = getattr(
            settings,
            "FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_ATTRIBUTES",
            bleach.ALLOWED_ATTRIBUTES,
        )
        
        if BLEACH_VERSION > '5.0.0':
            from bleach.css_sanitizer import CSSSanitizer
            from bleach.css_sanitizer import ALLOWED_CSS_PROPERTIES
            css_sanitizer = CSSSanitizer(allowed_css_properties=getattr(
                settings,
                "FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_STYLES",
                ALLOWED_CSS_PROPERTIES,
            ))
            return bleach.clean(
                text=self.cleaned_data["text"],
                tags=allowed_tags,
                attributes=allowed_attrs,
                strip=True,
                strip_comments=True,
                css_sanitizer=css_sanitizer
            )
            
        else:
        
            allowed_styles = getattr(
                settings,
                "FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_STYLES",
                bleach.ALLOWED_STYLES,
            )

            return bleach.clean(
                text=self.cleaned_data["text"],
                tags=allowed_tags,
                attributes=allowed_attrs,
                styles=allowed_styles,
                strip=True,
                strip_comments=True,
            )
