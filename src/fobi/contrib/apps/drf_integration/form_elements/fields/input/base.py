from django.utils.translation import ugettext_lazy as _

from rest_framework.fields import CharField

from .......base import IntegrationFormFieldPlugin
from .... import UID as INTEGRATE_WITH_UID
from ....base import (
    DRFIntegrationFormElementPluginProcessor,
    DRFSubmitPluginFormDataMixin,
)
from . import UID

__title__ = 'fobi.contrib.apps.drf_integration.form_elements.fields.' \
            'input.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('InputPlugin',)


class InputPlugin(IntegrationFormFieldPlugin,
                  DRFSubmitPluginFormDataMixin):
    """CharField plugin."""

    uid = UID
    integrate_with = INTEGRATE_WITH_UID
    name = _("Text")
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

        if form_element_plugin.data.autocomplete_value:
            field_metadata.update({'autocomplete': 'on'})

        if form_element_plugin.data.autofocus_value:
            field_metadata.update({'autofocus': 'autofocus'})

        if form_element_plugin.data.disabled_value:
            field_metadata.update({'disabled': 'disabled'})

        if form_element_plugin.data.list_value:
            field_metadata.update(
                {'list': form_element_plugin.data.list_value}
            )

        if form_element_plugin.data.max_value:
            field_metadata.update({'max': form_element_plugin.data.max_value})

        if form_element_plugin.data.min_value:
            field_metadata.update({'min': form_element_plugin.data.min_value})

        if form_element_plugin.data.multiple_value:
            field_metadata.update({'multiple': 'multiple'})

        if form_element_plugin.data.pattern_value:
            field_metadata.update(
                {'pattern': form_element_plugin.data.pattern_value}
            )

        if form_element_plugin.data.readonly_value:
            field_kwargs.update({'read_only': True})

        if form_element_plugin.data.step_value:
            field_metadata.update(
                {'step': form_element_plugin.data.step_value}
            )

        if form_element_plugin.data.type_value \
                and form_element_plugin.data.type_value in ('submit',
                                                            'button',
                                                            'reset',):
            field_metadata.update({'value': form_element_plugin.data.label})

        if form_element_plugin.data.max_length:
            field_kwargs.update(
                {'max_length': int(form_element_plugin.data.max_length)}
            )

        return [
            DRFIntegrationFormElementPluginProcessor(
                field_class=CharField,
                field_kwargs=field_kwargs,
                field_metadata=field_metadata
            )
        ]
