from __future__ import absolute_import

from collections import OrderedDict
from uuid import uuid4

from django.utils.encoding import smart_str
from django.utils.translation import gettext_lazy as _

from nonefield.fields import NoneField

from fobi.base import FormElementPlugin

from . import UID
from .forms import ContentRichTextForm

__title__ = 'fobi.contrib.plugins.form_elements.content.content_richtext.base'
__author__ = 'Frantisek Holop <fholop@ripe.net>'
__copyright__ = 'RIPE NCC'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ContentRichTextPlugin',)


class ContentRichTextPlugin(FormElementPlugin):
    """Content rich text plugin."""

    uid = UID
    name = _('Content rich text')
    group = _('Content')
    form = ContentRichTextForm

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
        rendered_text = "<div>{0}</div>".format(smart_str(self.data.text))
        return rendered_text

    def get_form_field_instances(self,
                                 request=None,
                                 form_entry=None,
                                 form_element_entries=None,
                                 **kwargs):
        field_kwargs = {
            'initial': smart_str(self.data.text),
            'required': False,
            'label': '',
        }

        return [(self.data.name, NoneField, field_kwargs)]
