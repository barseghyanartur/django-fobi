__title__ = 'fobi.dynamic'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('assemble_form_class',)

#import logging

from six import with_metaclass

from django.utils.datastructures import SortedDict
from django.forms.forms import BaseForm#, get_declared_fields
from django.forms.widgets import media_property

#logger = logging.getLogger(__file__)

# ****************************************************************************
# ****************************************************************************
# **************************** Form generator ********************************
# ****************************************************************************
# ****************************************************************************

def assemble_form_class(form_entry, base_class=BaseForm, request=None,
                        origin=None, origin_kwargs_update_func=None,
                        origin_return_func=None, form_element_entries=None):
    """
    Assembles a form class by given entry.

    :param form_entry:
    :param base_class:
    :param django.http.HttpRequest request:
    :param string origin:
    :param callable origin_kwargs_update_func:
    :param callable origin_return_func:
    :param iterable form_element_entries: If given, used instead of
        ``form_entry.formelemententry_set.all`` (no additional database hit).
    """
    if form_element_entries is None:
        form_element_entries = form_entry.formelemententry_set.all()

    class DeclarativeFieldsMetaclass(type):
        """
        Copied from ``django.forms.forms.DeclarativeFieldsMetaclass``.

        Metaclass that converts Field attributes to a dictionary called
        `base_fields`, taking into account parent class 'base_fields' as well.
        """
        def __new__(cls, name, bases, attrs):
            base_fields = []

            for creation_counter, form_element_entry in enumerate(form_element_entries):
                plugin = form_element_entry.get_plugin(request=request)

                # We simply make sure the plugin exists. We don't handle
                # exceptions relate to the non-existent plugins here. They
                # are instead handled in registry.
                if plugin:
                    plugin_form_field_instances = plugin._get_form_field_instances(
                        form_element_entry = form_element_entry,
                        origin = origin,
                        kwargs_update_func = origin_kwargs_update_func,
                        return_func = origin_return_func,
                        extra = {'counter': creation_counter},
                        request = request
                        )
                    for form_field_name, form_field_instance in plugin_form_field_instances:
                        base_fields.append((form_field_name, form_field_instance))

            attrs['base_fields'] = SortedDict(base_fields)
            new_class = super(DeclarativeFieldsMetaclass, cls).__new__(
                cls, name, bases, attrs
                )

            if 'media' not in attrs:
                new_class.media = media_property(new_class)

            return new_class

    class DynamicForm(with_metaclass(DeclarativeFieldsMetaclass, base_class)):
        """
        Dynamically created form element plugin class.
        """

    return DynamicForm
