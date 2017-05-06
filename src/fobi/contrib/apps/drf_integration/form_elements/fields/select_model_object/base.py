import copy

from django.utils.translation import ugettext_lazy as _

from rest_framework.fields import ChoiceField

from .......base import IntegrationFormFieldPlugin
from .... import UID as INTEGRATE_WITH_UID
from ....base import (
    DRFIntegrationFormElementPluginProcessor,
    DRFSubmitPluginFormDataMixin,
)

from . import UID

__title__ = 'fobi.contrib.apps.drf_integration.form_elements.fields.' \
            'select_model_object.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('SelectModelObjectInputPlugin',)


class SelectModelObjectInputPlugin(IntegrationFormFieldPlugin,
                                   DRFSubmitPluginFormDataMixin):
    """ChoiceField plugin."""

    uid = UID
    integrate_with = INTEGRATE_WITH_UID
    name = _("Select model object")
    group = _("Fields")

    def get_custom_field_instances(self,
                                   form_element_plugin,
                                   request=None,
                                   form_entry=None,
                                   form_element_entries=None,
                                   **kwargs):
        """Get form field instances."""
        queryset = form_element_plugin.get_queryset()

        field_kwargs = {
            'required': form_element_plugin.data.required,
            'initial': form_element_plugin.data.initial,
            'label': form_element_plugin.data.label,
            'help_text': form_element_plugin.data.help_text,
            'queryset': queryset,
        }
        # TODO: this does not work yet. It's either needed to make a dedicated
        # ModelChoiceField for Django REST framework, or transform the
        # queryset into to easily handle the data. Leave for now.
        return [
            DRFIntegrationFormElementPluginProcessor(
                field_class=ChoiceField,
                field_kwargs=field_kwargs
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
