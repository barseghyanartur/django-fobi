import decimal

from django.utils.translation import ugettext_lazy as _

from rest_framework.fields import DecimalField

from .......base import IntegrationFormFieldPlugin
from .... import UID as INTEGRATE_WITH_UID
from ....base import (
    DRFIntegrationFormElementPluginProcessor,
    DRFSubmitPluginFormDataMixin,
)
from . import UID

__title__ = 'fobi.contrib.apps.drf_integration.form_elements.fields.' \
            'decimal.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DecimalInputPlugin',)


class DecimalInputPlugin(IntegrationFormFieldPlugin,
                         DRFSubmitPluginFormDataMixin):
    """DecimalField plugin."""

    uid = UID
    integrate_with = INTEGRATE_WITH_UID
    name = _("Decimal")
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
            'initial': decimal.Decimal(form_element_plugin.data.initial),
            'label': form_element_plugin.data.label,
            'help_text': form_element_plugin.data.help_text,
        }

        if form_element_plugin.data.max_value:
            data_max_value = decimal.Decimal(
                form_element_plugin.data.max_value
            )
            field_kwargs.update({'max_value': data_max_value})

        if form_element_plugin.data.min_value:
            data_min_value = decimal.Decimal(
                form_element_plugin.data.min_value
            )
            field_kwargs.update({'min_value': data_min_value})

        if form_element_plugin.data.max_digits:
            data_max_digits = int(form_element_plugin.data.max_digits)
            field_kwargs.update({'max_digits': data_max_digits})

        if form_element_plugin.data.decimal_places:
            data_decimal_places = int(form_element_plugin.data.decimal_places)
            field_kwargs.update({'decimal_places': data_decimal_places})

        return [
            DRFIntegrationFormElementPluginProcessor(
                field_class=DecimalField,
                field_kwargs=field_kwargs
            )
        ]
