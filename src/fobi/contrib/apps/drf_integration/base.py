import copy
import logging

from ....base import (
    clean_dict,
    get_ignorable_form_fields,
    get_ordered_form_handler_plugins,
    integration_form_callback_registry,
    integration_form_element_plugin_registry,
    IntegrationFormElementPluginProcessor,
)
from ....helpers import get_ignorable_form_values

from . import UID
from .helpers import map_field_name_to_label

__title__ = 'fobi.contrib.apps.drf_integration.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'DRFIntegrationFormElementPluginProcessor',
    'DRFSubmitPluginFormDataMixin',
    'get_cleaned_data',
    'get_field_name_to_label_map',
    'get_processed_serializer_data',
    'run_form_handlers',
    'submit_plugin_form_data',
)


DEBUG = True
LOGGER = logging.getLogger(__name__)


class DRFIntegrationFormElementPluginProcessor(
    IntegrationFormElementPluginProcessor
):
    """Django REST framework field instance processor."""

    def __init__(self, *args, **kwargs):
        super(DRFIntegrationFormElementPluginProcessor, self).__init__(
            *args,
            **kwargs
        )
        self.field_class = kwargs.get('field_class')
        self.field_kwargs = kwargs.get('field_kwargs', {})
        self.field_metadata = kwargs.get('field_metadata', {})
        self.form_element_plugin = kwargs.get('form_element_plugin')
        self.data = self.form_element_plugin.data \
            if self.form_element_plugin \
            else {}

    def process_custom_form_field_instance(self,
                                           form_element_entry,
                                           form_entry,
                                           request,
                                           form_element_plugin=None):
        """Process."""
        if form_element_plugin:
            self.form_element_plugin = form_element_plugin
            self.data = form_element_plugin.data

        return self


class DRFSubmitPluginFormDataMixin(object):
    """Submit plugin form data mixin."""

    def _submit_plugin_form_data(self,
                                 form_element_plugin,
                                 form_entry,
                                 request,
                                 serializer,
                                 form_element_entries=None,
                                 **kwargs):
        """Submit plugin form data (internal method).

        Do not override this method. Use ``submit_plugin_form_data``,
        instead.

        Submit plugin form data. Called on form submission (when user actually
        posts the data to assembled form).

        :param form_element_plugin:
        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param rest_framework.serializers.Serializer serializer:
        :param iterable form_element_entries:
        """
        if DEBUG:
            return self.submit_plugin_form_data(
                form_element_plugin=form_element_plugin,
                form_entry=form_entry,
                request=request,
                serializer=serializer,
                form_element_entries=form_element_entries,
                **kwargs
            )
        else:
            try:
                return self.submit_plugin_form_data(
                    form_element_plugin=form_element_plugin,
                    form_entry=form_entry,
                    request=request,
                    serializer=serializer,
                    form_element_entries=form_element_entries,
                    **kwargs
                )
            except Exception as err:
                LOGGER.debug(str(err))

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


def fire_form_callbacks(form_entry, request, serializer, stage=None):
    """Fire DRF integration form callbacks.

    :param fobi.models.FormEntry form_entry:
    :param django.http.HttpRequest request:
    :param rest_framework.serializers.Serializer serializer:
    :param string stage:
    :return rest_framework.serializers.Serializer serializer:
    """
    callbacks = integration_form_callback_registry.get_callbacks(
        integrate_with=UID,
        stage=stage
    )
    for callback_cls in callbacks:
        callback = callback_cls()
        updated_serializer = callback.callback(
            form_entry=form_entry,
            request=request,
            serializer=serializer
        )
        if updated_serializer:
            serializer = updated_serializer
    return serializer


def run_form_handlers(form_entry,
                      request,
                      serializer,
                      form_element_entries=None):
    """Run form handlers.

    :param fobi.models.FormEntry form_entry:
    :param django.http.HttpRequest request:
    :param rest_framework.serializers.Serializer serializer:
    :param iterable form_element_entries:
    :return tuple: List of success responses, list of error responses
    """
    # Errors list
    errors = []

    # Responses of successfully processed handlers
    responses = []

    # Getting form handler plugins in their execution order.
    ordered_form_handlers = get_ordered_form_handler_plugins()

    # Getting the form handlers to be executed.
    form_handlers = form_entry.formhandlerentry_set.order_by('plugin_uid')[:]

    # Assembling a new dictionary of the form handlers to iterate later.
    for form_handler in form_handlers:
        ordered_form_handlers[form_handler.plugin_uid].append(form_handler)

    # Iterating through the form handlers in the order
    # specified in the settings.
    for uid, form_handlers in ordered_form_handlers.items():
        # logger.debug("UID: {0}".format(uid))
        for form_handler in form_handlers:
            # Get the form handler plugin
            form_handler_plugin = form_handler.get_plugin(request=request)

            # Run the form handler
            success, response = \
                form_handler_plugin._run_integration_handler(
                    integrate_with=UID,
                    form_entry=form_entry,
                    request=request,
                    serializer=serializer,
                    form_element_entries=form_element_entries,
                )

            if success:
                responses.append((form_handler_plugin, response))
            else:
                errors.append((form_handler_plugin, response))

    return responses, errors


def submit_plugin_form_data(form_entry,
                            request,
                            serializer,
                            form_element_entries=None,
                            **kwargs):
    """Submit plugin form data for all plugins.

    :param fobi.models.FormEntry form_entry: Instance of
        ``fobi.models.FormEntry``.
    :param django.http.HttpRequest request:
    :param rest_framework.serializers.Serializer serializer:
    :param iterable form_element_entries:
    """
    if not form_element_entries:
        form_element_entries = form_entry.formelemententry_set.all()
    for form_element_entry in form_element_entries:
        # Get the plugin.
        form_element_plugin = form_element_entry.get_plugin(request=request)
        custom_plugin_cls = integration_form_element_plugin_registry.get(
            integrate_with=UID,
            uid=form_element_plugin.uid
        )
        if custom_plugin_cls:
            custom_plugin = custom_plugin_cls()
            updated_serializer = \
                custom_plugin._submit_plugin_form_data(
                    form_element_plugin=form_element_plugin,
                    form_entry=form_entry,
                    request=request,
                    serializer=serializer,
                    form_element_entries=form_element_entries,
                    **kwargs
                )
            if updated_serializer:
                serializer = updated_serializer

    return serializer


def get_processed_serializer_data(serializer, form_element_entries):
    """Gets processed serializer data.

    Simply fires both ``fobi.base.get_cleaned_data`` and
    ``fobi.base.get_field_name_to_label_map`` functions and returns the
    result.

    :param serializer:
    :param iterable form_element_entries: Iterable of form element entries.
    :return tuple:
    """
    keys_to_remove = get_ignorable_form_fields(form_element_entries)
    values_to_remove = get_ignorable_form_values()

    field_name_to_label_map = \
        get_field_name_to_label_map(serializer,
                                    keys_to_remove,
                                    values_to_remove)

    keys_to_remove = list(field_name_to_label_map.keys())

    return (
        field_name_to_label_map,
        get_cleaned_data(serializer, keys_to_remove, values_to_remove)
    )


def get_field_name_to_label_map(serializer,
                                keys_to_remove=[],
                                values_to_remove=[]):
    """Get field name to label map.

    :param serializer:
    :param iterable keys_to_remove:
    :param iterable values_to_remove:
    :return dict:
    """
    if not keys_to_remove:
        keys_to_remove = get_ignorable_form_fields([])

    if not values_to_remove:
        values_to_remove = get_ignorable_form_values()

    field_name_to_label_map = clean_dict(
        map_field_name_to_label(serializer),
        keys_to_remove,
        values_to_remove
    )

    return field_name_to_label_map


def get_cleaned_data(serializer, keys_to_remove=[], values_to_remove=[]):
    """Get cleaned data.

    Gets cleaned data, having the trash (fields without values) filtered
    out.

    :param serializer:
    :param iterable keys_to_remove:
    :param iterable values_to_remove:
    :return dict:
    """
    if not values_to_remove:
        values_to_remove = get_ignorable_form_values()

    cleaned_data = copy.copy(serializer.validated_data)
    cleaned_data = clean_dict(
        cleaned_data,
        keys=list(set(cleaned_data.keys()) - set(keys_to_remove)),
        values=values_to_remove
    )

    return cleaned_data
