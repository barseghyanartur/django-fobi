import copy

from rest_framework.metadata import SimpleMetadata
from rest_framework.utils.field_mapping import ClassLookupDict

from .fields import (
    MultipleChoiceWithMaxField,
    ContentImageField,
    ContentTextField,
    ContentVideoField,
)

__title__ = 'fobi.contrib.apps.drf_integration.metadata'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'FobiMetaData',
    'FobiJSONSchemaMetaData',
)


class FobiMetaData(SimpleMetadata):
    """Meta data for better representation of the form elements."""

    __mapping = copy.copy(SimpleMetadata.label_lookup.mapping)
    __mapping.update(
        {
            MultipleChoiceWithMaxField: 'multiple choice',
            ContentImageField: 'content',
            ContentTextField: 'content',
            ContentVideoField: 'content',
        }
    )

    label_lookup = ClassLookupDict(__mapping)

    def get_field_info(self, field):
        """Get field info.

        Given an instance of a serializer field, return a dictionary
        of metadata about it.
        """
        field_info = super(FobiMetaData, self).get_field_info(field)

        for __key in ['initial', 'max_value', 'min_value']:
            __val = getattr(field, __key, None)
            if __val not in (None, ''):
                field_info[__key] = __val

        field_metadata = field.root.get_fields_metadata().get(
            field.field_name, {}
        )
        if field_metadata:
            for __k, __val in field_metadata.items():
                if __val not in (None, ''):
                    field_info[__k] = __val

        return field_info


class FobiJSONSchemaMetaData(FobiMetaData):
    def get_field_info(self, field):
        default_field_info = super(FobiJSONSchemaMetaData, self).get_field_info(field)
        field_info = {}

        field_mappings = dict(
            type='type',
            title='label',
            default='initial',
            maximum='max_value',
            minimum='min_value',
            minLength='min_length',
            maxLength='max_length',
            # These are schema,but need to be handled differently.
            # required='required',
            # These are not schema, but ui.

        )

        # TODO handle required, needs to be a list on the parent
        # required
        # TODO handle UI
        # readonly='read_only'
        # disabled=None,
        # help_text
        # placeholder
        # TODO Handle choices
        # enum = field.choices
        # uniqueItems = true
        # Set checkboxes ?

        for schema_key, drf_key in field_mappings.items():
            value = default_field_info.get(drf_key)
            if value is not None:
                field_info[schema_key] = value

        return field_info
