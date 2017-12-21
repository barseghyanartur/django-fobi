from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from ckeditor.widgets import CKEditorWidget

from fobi.base import BasePluginForm, get_theme

try:
    import bleach
    BLEACH_INSTALLED = True
except ImportError as err:
    BLEACH_INSTALLED = False

__title__ = 'fobi.contrib.plugins.form_elements.content.content_richtext.forms'
__author__ = 'Frantisek Holop <fholop@ripe.net>'
__copyright__ = 'RIPE NCC'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ContentRichTextForm',)


theme = get_theme(request=None, as_instance=True)


class ContentRichTextForm(forms.Form, BasePluginForm):
    """ContentRichTextForm."""

    plugin_data_fields = [
        ('text', '')
    ]

    text = forms.CharField(
        label=_('Text'),
        required=True,
        widget=CKEditorWidget(),
    )

    def clean_text(self):
        if not BLEACH_INSTALLED:
            return self.cleaned_data['text']

        ALLOWED_TAGS = [
            'a', 'abbr', 'acronym', 'b', 'blockquote',
            'code', 'em', 'i', 'li', 'ol', 'strong', 'ul',
        ]

        ALLOWED_ATTRIBUTES = {
            'a': ['href', 'title'],
            'abbr': ['title'],
            'acronym': ['title'],
        }

        allowed_tags = getattr(
            settings,
            'FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_TAGS',
            ALLOWED_TAGS
        )
        allowed_attrs = getattr(
            settings,
            'FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_ATTRIBUTES',
            ALLOWED_ATTRIBUTES
        )

        return bleach.clean(
            text=self.cleaned_data['text'],
            tags=allowed_tags,
            attributes=allowed_attrs,
            strip=True,
            strip_comments=True,
        )
