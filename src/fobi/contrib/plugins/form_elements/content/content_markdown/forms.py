from django import forms
from django.utils.translation import ugettext_lazy as _

from fobi.base import BasePluginForm, get_theme
from fobi.reusable.markdown_widget.widgets import MarkdownWidget

__title__ = 'fobi.contrib.plugins.form_elements.content.content_richtext.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ContentMarkdownForm',)


theme = get_theme(request=None, as_instance=True)


class ContentMarkdownForm(forms.Form, BasePluginForm):
    """ContentMarkDownForm."""

    plugin_data_fields = [
        ('text', '')
    ]

    text = forms.CharField(
        label=_('Text'),
        required=True,
        widget=MarkdownWidget(
            attrs={
                'class': '{} content-markdown'.format(
                    theme.form_element_html_class
                )
            }
        ),
    )
