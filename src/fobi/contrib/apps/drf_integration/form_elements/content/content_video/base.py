import logging

from django.utils.translation import ugettext_lazy as _

from .......base import IntegrationFormElementPlugin
from .... import UID as INTEGRATE_WITH_UID
from ....base import (
    DRFIntegrationFormElementPluginProcessor,
    DRFSubmitPluginFormDataMixin,
)
from ....fields import ContentVideoField
from . import UID

__title__ = 'fobi.contrib.apps.drf_integration.form_elements.content.' \
            'content_video.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ContentVideoPlugin',)


LOGGER = logging.getLogger(__name__)


class ContentVideoPlugin(IntegrationFormElementPlugin,
                         DRFSubmitPluginFormDataMixin):
    """CharField plugin."""

    uid = UID
    integrate_with = INTEGRATE_WITH_UID
    name = _("Content image")
    group = _("Content")

    def get_custom_field_instances(self,
                                   form_element_plugin,
                                   request=None,
                                   form_entry=None,
                                   form_element_entries=None,
                                   has_value=None,
                                   **kwargs):
        """Get form field instances."""
        rendered_video = form_element_plugin.get_rendered_video()
        raw_data = form_element_plugin.get_raw_data()

        field_kwargs = {
            'initial': rendered_video,
            'default': rendered_video,
            'required': False,
            'label': '',
            'read_only': True,
            'raw_data': raw_data,
        }
        field_metadata = {
            'type': 'content',
            'contenttype': 'video',
            'content': rendered_video,
            'raw_data': raw_data
        }

        return [
            DRFIntegrationFormElementPluginProcessor(
                field_class=ContentVideoField,
                field_kwargs=field_kwargs,
                field_metadata=field_metadata
            )
        ]
