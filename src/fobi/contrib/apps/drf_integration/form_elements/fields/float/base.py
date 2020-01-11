from django.utils.translation import gettext_lazy as _

from rest_framework.fields import FloatField

from .......base import IntegrationFormFieldPlugin
from .... import UID as INTEGRATE_WITH_UID
from ....base import (
    DRFIntegrationFormElementPluginProcessor,
    DRFSubmitPluginFormDataMixin,
)
from . import UID

__title__ = 'fobi.contrib.apps.drf_integration.form_elements.fields.' \
            'float.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('FloatInputPlugin',)


class FloatInputPlugin(IntegrationFormFieldPlugin,
                       DRFSubmitPluginFormDataMixin):
    """FloatField plugin."""

    uid = UID
    integrate_with = INTEGRATE_WITH_UID
    name = _("Float")
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
            'label': form_element_plugin.data.label,
            'help_text': form_element_plugin.data.help_text,
        }
        field_metadata = {
            'placeholder': form_element_plugin.data.placeholder
        }

        if form_element_plugin.data.initial:
            field_kwargs['initial'] = float(form_element_plugin.data.initial)

        if form_element_plugin.data.max_value:
            data_max_value = float(form_element_plugin.data.max_value)
            field_kwargs['max_value'] = data_max_value

        if form_element_plugin.data.min_value:
            data_min_value = float(form_element_plugin.data.min_value)
            field_kwargs['min_value'] = data_min_value

        return [
            DRFIntegrationFormElementPluginProcessor(
                field_class=FloatField,
                field_kwargs=field_kwargs,
                field_metadata=field_metadata
            )
        ]
