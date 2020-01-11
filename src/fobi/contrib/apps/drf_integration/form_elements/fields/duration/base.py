import copy
import datetime

from django.utils.dateparse import parse_duration
from django.utils.encoding import force_text
from django.utils.translation import gettext_lazy as _

from rest_framework.fields import DurationField

from .......base import IntegrationFormFieldPlugin
from .... import UID as INTEGRATE_WITH_UID
from ....base import (
    DRFIntegrationFormElementPluginProcessor,
    DRFSubmitPluginFormDataMixin,
)
from . import UID

__title__ = 'fobi.contrib.apps.drf_integration.form_elements.fields.' \
            'duration.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DurationInputPlugin',)


class DurationInputPlugin(IntegrationFormFieldPlugin,
                          DRFSubmitPluginFormDataMixin):
    """DurationField plugin."""

    uid = UID
    integrate_with = INTEGRATE_WITH_UID
    name = _("Duration")
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
            # 'initial': form_element_plugin.data.initial,
            'label': form_element_plugin.data.label,
            'help_text': form_element_plugin.data.help_text,
        }

        if form_element_plugin.data.initial:
            data_initial = force_text(form_element_plugin.data.initial)
            if not isinstance(data_initial, datetime.timedelta):
                parsed_initial = parse_duration(data_initial)
                if parsed_initial is not None:
                    data_initial = parsed_initial

            field_kwargs.update({'initial': data_initial})

        field_metadata = {
            'placeholder': form_element_plugin.data.placeholder
        }

        return [
            DRFIntegrationFormElementPluginProcessor(
                field_class=DurationField,
                field_kwargs=field_kwargs,
                field_metadata=field_metadata
            )
        ]

    def submit_plugin_form_data(self,
                                form_element_plugin,
                                form_entry,
                                request,
                                serializer,
                                form_element_entries=None,
                                **kwargs):
        """Submit plugin form data.

        Called on form submission (when user actually
        posts the data to assembled form).

        :param form_element_plugin:
        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param rest_framework.serializers.Serializer serializer:
        :param iterable form_element_entries:
        """
        validated_data = copy.copy(serializer.validated_data)

        validated_data = form_element_plugin.prepare_plugin_form_data(
            validated_data
        )
        if validated_data:
            serializer._validated_data = validated_data

        return serializer
