from __future__ import absolute_import

from fobi.base import FormElementPluginWidget

from . import UID

__title__ = 'fobi.contrib.plugins.form_elements.content.' \
            'content_richtext.widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'BaseContentRichTextPluginWidget',
)


class BaseContentRichTextPluginWidget(FormElementPluginWidget):
    """Base content rich text form element plugin widget."""

    plugin_uid = UID
    html_classes = ['content-richtext']
    media_js = [
        'ckeditor/ckeditor-init.js',
        'ckeditor/ckeditor/ckeditor.js',
    ]
