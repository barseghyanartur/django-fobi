from __future__ import absolute_import

from fobi.base import FormElementPluginWidget

from . import UID

__title__ = 'fobi.contrib.plugins.form_elements.content.' \
            'content_markdown.widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'BaseContentMarkdownPluginWidget',
)


class BaseContentMarkdownPluginWidget(FormElementPluginWidget):
    """Base content markdown form element plugin widget."""

    plugin_uid = UID
    html_classes = ['content-markdown']
