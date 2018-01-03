from __future__ import absolute_import

from collections import OrderedDict
from uuid import uuid4

from django.utils.translation import ugettext_lazy as _

from nonefield.fields import NoneField

from fobi.base import FormElementPlugin
from fobi.reusable.markdown_widget.helpers import convert_to_markdown

from . import UID
from .forms import ContentMarkdownForm

__title__ = 'fobi.contrib.plugins.form_elements.content.content_richtext.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ContentMarkdownPlugin',)


class ContentMarkdownPlugin(FormElementPlugin):
    """Content markdown plugin."""

    uid = UID
    name = _('Content markdown')
    group = _('Content')
    form = ContentMarkdownForm
    html_classes = ['content-markdown']

    def post_processor(self):
        self.data.name = '{0}_{1}'.format(self.uid, uuid4())

    def get_raw_data(self):
        return OrderedDict(
            (
                ('text', self.data.text),
            )
        )

    def get_rendered_text(self):
        """Get rendered text."""
        rendered_text = "<div>{0}</div>".format(
            convert_to_markdown(self.data.text)
        )
        return rendered_text

    def get_form_field_instances(self,
                                 request=None,
                                 form_entry=None,
                                 form_element_entries=None,
                                 **kwargs):
        field_kwargs = {
            'initial': convert_to_markdown(self.data.text),
            'required': False,
            'label': '',
        }

        return [(self.data.name, NoneField, field_kwargs)]
