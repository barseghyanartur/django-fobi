from __future__ import absolute_import

from collections import OrderedDict
from uuid import uuid4

from django.utils.encoding import smart_str
from django.utils.translation import ugettext_lazy as _

from nonefield.fields import NoneField

from fobi.base import FormElementPlugin

from . import UID
from .forms import ContentTextForm

__title__ = 'fobi.contrib.plugins.form_elements.content.content_text.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ContentTextPlugin',)


class ContentTextPlugin(FormElementPlugin):
    """Content text plugin."""

    uid = UID
    name = _("Content text")
    group = _("Content")
    form = ContentTextForm

    def post_processor(self):
        """Post process data.

        Always the same.
        """
        self.data.name = "{0}_{1}".format(self.uid, uuid4())

    def get_raw_data(self):
        """Get raw data.

        Might be used in integration plugins.
        """
        return OrderedDict(
            (
                ('text', self.data.text),
            )
        )

    def get_rendered_text(self):
        """Get rendered text."""
        rendered_text = "<p>{0}</p>".format(smart_str(self.data.text))
        return rendered_text

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        field_kwargs = {
            'initial': self.get_rendered_text(),
            'required': False,
            'label': '',
        }

        return [(self.data.name, NoneField, field_kwargs)]
