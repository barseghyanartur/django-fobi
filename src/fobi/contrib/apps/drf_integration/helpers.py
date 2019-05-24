__title__ = 'fobi.contrib.apps.drf_integration.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'map_field_name_to_label',
)


def map_field_name_to_label(serializer):
    """Takes a form and creates label to field name map.

    :param serializer: Instance of ``rest_framework.serializers.Serializer``.
    :return dict:
    """
    return dict([(field_name, field.label)
                 for (field_name, field)
                 in serializer.fields.items()])
