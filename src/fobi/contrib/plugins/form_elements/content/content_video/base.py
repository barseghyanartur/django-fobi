from __future__ import absolute_import

from collections import OrderedDict
from uuid import uuid4

from django.utils.translation import ugettext_lazy as _

from vishap import render_video

from nonefield.fields import NoneField

from fobi.base import FormElementPlugin

from . import UID
from .forms import ContentVideoForm

__title__ = 'fobi.contrib.plugins.form_elements.content.content_video.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ContentVideoPlugin',)


class ContentVideoPlugin(FormElementPlugin):
    """Content video plugin."""

    uid = UID
    name = _("Content video")
    group = _("Content")
    form = ContentVideoForm

    def post_processor(self):
        """Process plugin data.

        Always the same.
        """
        self.data.name = "{0}_{1}".format(self.uid, uuid4())

    def get_raw_data(self):
        """Get raw data.

        Might be used in integration plugins.
        """
        return OrderedDict(
            (
                ('title', self.data.title),
                ('url', self.data.url),
                ('size', self.data.size),
            )
        )

    def get_rendered_video(self):
        """Get rendered video.

        Might be used in integration plugins.
        """
        width, height = self.data.size.split('x')
        return render_video(self.data.url, width, height)

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        field_kwargs = {
            'initial': '<div class="video-wrapper">{0}</div>'.format(
                self.get_rendered_video()
            ),
            'required': False,
            'label': '',
        }

        return [(self.data.name, NoneField, field_kwargs)]
