from markdown import markdown

__title__ = 'fobi.reusable.markdown_widget.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('convert_to_markdown',)


def convert_to_markdown(content):
    """
    Trans-compiles Markdown text to HTML.

    :param content: Markdown text.
    :type content: str
    :return: HTML encoded text.
    :rtype: str
    """
    md = markdown(
        text=content
    )
    return md
