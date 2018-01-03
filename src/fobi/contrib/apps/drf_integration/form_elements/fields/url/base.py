from django.utils.translation import ugettext_lazy as _

from rest_framework.fields import URLField

from .......base import IntegrationFormFieldPlugin
from .... import UID as INTEGRATE_WITH_UID
from ....base import (
    DRFIntegrationFormElementPluginProcessor,
    DRFSubmitPluginFormDataMixin,
)
from . import UID

__title__ = 'fobi.contrib.apps.drf_integration.form_elements.fields.' \
            'url.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('URLInputPlugin',)


class URLInputPlugin(IntegrationFormFieldPlugin,
                     DRFSubmitPluginFormDataMixin):
    """URLField plugin."""

    uid = UID
    integrate_with = INTEGRATE_WITH_UID
    name = _("URL")
    group = _("Fields")

    def get_custom_field_instances(self,
                                   form_element_plugin,
                                   request=None,
                                   form_entry=None,
                                   form_element_entries=None,
                                   **kwargs):
        """Get form field instances."""
        field_kwargs = {
            'required': form_element_plugin.data.required,
            'initial': form_element_plugin.data.initial,
            'label': form_element_plugin.data.label,
            'help_text': form_element_plugin.data.help_text,
        }
        field_metadata = {
            'placeholder': form_element_plugin.data.placeholder
        }
        if form_element_plugin.data.max_length:
            field_kwargs.update(
                {'max_length': int(form_element_plugin.data.max_length)}
            )
        return [
            DRFIntegrationFormElementPluginProcessor(
                field_class=URLField,
                field_kwargs=field_kwargs,
                field_metadata=field_metadata
            )
        ]
