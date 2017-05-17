from __future__ import absolute_import

from collections import OrderedDict
from uuid import uuid4

from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from nonefield.fields import NoneField

from fobi.base import FormElementPlugin

from . import UID
from .forms import ContentImageURLForm
from .settings import (
    FIT_METHOD_FIT_WIDTH,
    FIT_METHOD_FIT_HEIGHT,
)

__title__ = 'fobi.contrib.plugins.form_elements.content.content_image_url.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ContentImageURLPlugin',)


class ContentImageURLPlugin(FormElementPlugin):
    """Content image plugin."""

    uid = UID
    name = _("Content image URL")
    group = _("Content")
    form = ContentImageURLForm

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
                ('url', self.data.url),
                ('alt', self.data.alt),
                ('fit_method', self.data.fit_method),
                ('size', self.data.size),
            )
        )

    def get_rendered_image(self):
        """Get rendered image."""
        width, height = self.data.size.split('x')

        if FIT_METHOD_FIT_WIDTH == self.data.fit_method:
            thumb_size = (width, 0)
        elif FIT_METHOD_FIT_HEIGHT == self.data.fit_method:
            thumb_size = (0, height)
        else:
            thumb_size = (width, height)

        context = {
            'plugin': self,
            'thumb_size': thumb_size,
        }
        rendered_image = render_to_string(
            'content_image_url/render.html',
            context
        )
        return rendered_image

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        field_kwargs = {
            'initial': self.get_rendered_image(),
            'required': False,
            'label': '',
        }

        return [(self.data.name, NoneField, field_kwargs)]
