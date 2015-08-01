__title__ = 'fobi.contrib.plugins.form_elements.content.content_video.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ContentVideoPlugin',)

from uuid import uuid4

from django.utils.translation import ugettext_lazy as _

from vishap import render_video

from nonefield.fields import NoneField

from fobi.base import FormElementPlugin, form_element_plugin_registry

from . import UID
from .forms import ContentVideoForm

class ContentVideoPlugin(FormElementPlugin):
    """
    Content video plugin.
    """
    uid = UID
    name = _("Content video")
    group = _("Content")
    form = ContentVideoForm

    def post_processor(self):
        """
        Always the same.
        """
        self.data.name = "{0}_{1}".format(self.uid, uuid4())

    def get_form_field_instances(self):
        """
        Get form field instances.
        """
        width, height = self.data.size.split('x')

        kwargs = {
            'initial': '<div class="video-wrapper">{0}</div>'.format(
                render_video(self.data.url, width, height)
                ),
            'required': False,
            'label': '',
        }

        form_field_instances = []

        form_field_instances.append((self.data.name, NoneField, kwargs))
        return form_field_instances


form_element_plugin_registry.register(ContentVideoPlugin)
