import logging

from django.utils.translation import gettext_lazy as _

from .......base import IntegrationFormElementPlugin
from .... import UID as INTEGRATE_WITH_UID
from ....base import (
    DRFIntegrationFormElementPluginProcessor,
    DRFSubmitPluginFormDataMixin,
)
from ....fields import ContentImageField
from . import UID

__title__ = 'fobi.contrib.apps.drf_integration.form_elements.content.' \
            'content_image_url.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ContentImageURLPlugin',)


LOGGER = logging.getLogger(__name__)


class ContentImageURLPlugin(IntegrationFormElementPlugin,
                            DRFSubmitPluginFormDataMixin):
    """CharField plugin."""

    uid = UID
    integrate_with = INTEGRATE_WITH_UID
    name = _("Content image URL")
    group = _("Content")

    def get_custom_field_instances(self,
                                   form_element_plugin,
                                   request=None,
                                   form_entry=None,
                                   form_element_entries=None,
                                   has_value=None,
                                   **kwargs):
        """Get form field instances."""

        rendered_image = form_element_plugin.get_rendered_image()
        raw_data = form_element_plugin.get_raw_data()

        field_kwargs = {
            'initial': rendered_image,
            'default': rendered_image,
            'required': False,
            'label': '',
            'read_only': True,
            'raw_data': raw_data,
        }
        field_metadata = {
            'type': 'content',
            'contenttype': 'image',
            'content': rendered_image,
            'raw_data': raw_data
        }

        return [
            DRFIntegrationFormElementPluginProcessor(
                field_class=ContentImageField,
                field_kwargs=field_kwargs,
                field_metadata=field_metadata
            )
        ]
