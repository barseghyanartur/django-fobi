from .dynamic import assemble_serializer_class

__title__ = 'fobi.contrib.apps.drf_integration.utils'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('get_serializer_class',)


def get_serializer_class(form_entry,
                         request=None,
                         has_value=None,
                         declared_fields=None):
    """Get assembled serializer class.

    :param fobi.models.FormEntry form_entry:
    :param django.http.HttpRequest request:
    :param bool has_value:
    :param list declared_fields:
    :return django.forms.Form:
    """
    return assemble_serializer_class(form_entry,
                                     request=request,
                                     has_value=has_value,
                                     declared_fields=declared_fields)
