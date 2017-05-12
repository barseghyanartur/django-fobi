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
        if isinstance(
            field,
            (ContentTextField, ContentImageField, ContentVideoField)
        ):
            field_info['type'] = 'content'

            if isinstance(field, ContentTextField):
                field_info['contenttype'] = 'text'
                field_info['content'] = field.initial
                field_info['raw'] = field.raw_data
            elif isinstance(field, ContentImageField):
                field_info['contenttype'] = 'image'
                field_info['content'] = field.initial
                field_info['raw'] = field.raw_data
            else:
                field_info['contenttype'] = 'video'
                field_info['content'] = field.initial
                field_info['raw'] = field.raw_data

        return field_info
