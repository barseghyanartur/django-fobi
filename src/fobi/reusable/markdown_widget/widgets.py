from django.forms.utils import flatatt
from django.forms.widgets import Textarea
from django.utils.html import format_html

from fobi.helpers import safe_text

__title__ = 'fobi.reusable.markdown_widget.widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('MarkdownWidget',)


class MarkdownWidget(Textarea):
    """Markdown widget based on remarkable."""

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''

        final_attrs = dict(name=name)
        final_attrs.update(self.attrs)

        if attrs is not None:
            final_attrs.update(attrs)

        return format_html(
            '<div class="markdown-widget-wrapper">'
            '<textarea{}>\r\n{}</textarea>'
            '<h6>Preview:</h6>'
            '<div class="markdown-preview"></div>'
            '</div>',
            flatatt(final_attrs),
            safe_text(value)
        )

    class Media(object):
        """Media options."""

        js = [
            'markdown_widget/remarkable.min.js',
            'content_markdown/fobi.plugin.content_markdown.js',
        ]
