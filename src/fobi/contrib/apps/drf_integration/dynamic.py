from __future__ import unicode_literals

import copy
from collections import Mapping, OrderedDict
from django.core.exceptions import ValidationError as DjangoValidationError

from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from rest_framework.compat import unicode_to_repr
from rest_framework.exceptions import ErrorDetail, ValidationError
from rest_framework.fields import (
    empty,
    get_error_detail,
    set_value,
    SkipField,
)
from rest_framework.relations import PKOnlyObject
from rest_framework.settings import api_settings
from rest_framework.serializers import BaseSerializer
from rest_framework.utils import html, representation
from rest_framework.utils.serializer_helpers import (
    BindingDict,
    BoundField,
    NestedBoundField,
    ReturnDict,
)

import six

from . import UID as INTEGRATE_WITH_UID


__title__ = 'fobi.contrib.apps.drf_integration.dynamic'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'assemble_serializer_class',
    'get_declared_fields',
)

# ****************************************************************************
# ****************************************************************************
# ************************ Serializer generator ******************************
# ****************************************************************************
# ****************************************************************************


def get_declared_fields(form_entry,
                        request=None,
                        origin=None,
                        origin_kwargs_update_func=None,
                        origin_return_func=None,
                        form_element_entries=None,
                        has_value=None):
    """Get declared fields."""
    declared_fields = []
    declared_fields_metadata = []
    if form_element_entries is None:
        form_element_entries = form_entry.formelemententry_set.all()

    for creation_counter, form_element_entry \
            in enumerate(form_element_entries):
        plugin = form_element_entry.get_plugin(request=request)

        # We simply make sure the plugin exists. We don't handle
        # exceptions relate to the non-existent plugins here. They
        # are instead handled in registry.
        if plugin:
            plugin_custom_field_instances = \
                plugin._get_custom_field_instances(
                    integrate_with=INTEGRATE_WITH_UID,
                    form_element_entry=form_element_entry,
                    origin=origin,
                    kwargs_update_func=origin_kwargs_update_func,
                    return_func=origin_return_func,
                    extra={'counter': creation_counter},
                    request=request,
                    has_value=has_value
                )
            for plugin_custom_field_instance \
                    in plugin_custom_field_instances:

                # The serializer field class
                custom_field_class = plugin_custom_field_instance.field_class(
                    **plugin_custom_field_instance.field_kwargs
                )

                # Since serializer fields do not accept **kwargs, we need
                # to assign `declared_fields_metadata` in the same way as we
                # do with `declared_fields`.
                declared_fields_metadata.append(
                    (
                        plugin_custom_field_instance.data.name,
                        plugin_custom_field_instance.field_metadata
                    )
                )

                declared_fields.append(
                    (
                        plugin_custom_field_instance.data.name,
                        custom_field_class,
                    )
                )

    return OrderedDict(declared_fields), OrderedDict(declared_fields_metadata)


def assemble_serializer_class(form_entry,
                              request=None,
                              origin=None,
                              origin_kwargs_update_func=None,
                              origin_return_func=None,
                              form_element_entries=None,
                              has_value=None,
                              declared_fields=None,
                              declared_fields_metadata=None):
    """Assemble a serializer class by given entry.

    :param form_entry:
    :param base_class:
    :param django.http.HttpRequest request:
    :param string origin:
    :param callable origin_kwargs_update_func:
    :param callable origin_return_func:
    :param iterable form_element_entries: If given, used instead of
        ``form_entry.formelemententry_set.all`` (no additional database hit).
    :param bool has_value:
    """
    # if form_element_entries is None:
    #     form_element_entries = form_entry.formelemententry_set.all()

    # class DeclarativeFieldsSerializerMetaclass(SerializerMetaclass):
    #     """Meta-class for setting ``_declared_fields`` dictionary.
    #
    #     Any instances of ``Field`` included as attributes on either the class
    #     or on any of its superclasses will be include in the
    #     ``_declared_fields`` dictionary.
    #     """
    #
    #     def __new__(cls, name, bases, attrs):
    #
    #         # Get the declared fields dict.
    #         declared_fields = get_declared_fields(
    #             form_entry,
    #             origin=origin,
    #             origin_kwargs_update_func=origin_kwargs_update_func,
    #             origin_return_func=origin_return_func,
    #             request=request,
    #             form_element_entries=form_element_entries,
    #         )
    #         attrs['_declared_fields'] = declared_fields
    #
    #         new_class = super(
    #             DeclarativeFieldsSerializerMetaclass, cls
    #         ).__new__(
    #             cls, name, bases, attrs
    #         )
    #
    #         if 'media' not in attrs:
    #             new_class.media = media_property(new_class)
    #
    #         return new_class
    #
    # class DynamicSerializer(
    #     with_metaclass(DeclarativeFieldsSerializerMetaclass, base_class)
    # ):
    #     """Dynamically created form element plugin class."""
    #
    # return DynamicSerializer

    if declared_fields is None:
        declared_fields, declared_fields_metadata = get_declared_fields(
            form_entry,
            origin=origin,
            origin_kwargs_update_func=origin_kwargs_update_func,
            origin_return_func=origin_return_func,
            request=request,
            form_element_entries=form_element_entries,
            has_value=has_value
        )

    # Most of the code below has been copied from rest_framework.serializers
    # module with a few modifications. Simplifying this is a TODO,
    # thus if you know a better way of doing this (reducing the code),
    # please do not hesitate to make a pull request.

    class SerializerMetaclass(type):
        """
        This metaclass sets a dictionary named `_declared_fields` on the class.

        Any instances of `Field` included as attributes on either the class
        or on any of its superclasses will be include in the
        `_declared_fields` dictionary.
        """

        @classmethod
        def _get_declared_fields(cls, bases, attrs):
            """Modified version of the original _get_declared_fields."""
            fields = [
                 (field_name, obj) for field_name, obj
                 in declared_fields.items()
                 if field_name not in attrs
             ]

            return OrderedDict(fields)

        @classmethod
        def _get_declared_fields_metadata(cls, bases, attrs):
            """Similar to _get_declared_fields, but for metadata."""
            fields = [
                (field_name, obj) for field_name, obj
                in declared_fields_metadata.items()
                if field_name not in attrs
            ]

            return OrderedDict(fields)

        def __new__(cls, name, bases, attrs):
            """Modified version of the original __new__."""
            attrs['_declared_fields'] = cls._get_declared_fields(bases, attrs)
            attrs['_declared_fields_metadata'] = \
                cls._get_declared_fields_metadata(bases, attrs)
            return super(SerializerMetaclass, cls).__new__(cls,
                                                           name,
                                                           bases,
                                                           attrs)

    def as_serializer_error(exc):
        assert isinstance(exc, (ValidationError, DjangoValidationError))

        if isinstance(exc, DjangoValidationError):
            detail = get_error_detail(exc)
        else:
            detail = exc.detail

        if isinstance(detail, Mapping):
            # If errors may be a dict we use the standard
            # {key: list of values}. Here we ensure that all the values are
            # *lists* of errors.
            return {
                key: value if isinstance(value, (list, Mapping)) else [value]
                for key, value in detail.items()
            }
        elif isinstance(detail, list):
            # Errors raised as a list are non-field errors.
            return {
                api_settings.NON_FIELD_ERRORS_KEY: detail
            }
        # Errors raised as a string are non-field errors.
        return {
            api_settings.NON_FIELD_ERRORS_KEY: [detail]
        }

    @six.add_metaclass(SerializerMetaclass)
    class Serializer(BaseSerializer):
        default_error_messages = {
            'invalid': _(
                'Invalid data. Expected a dictionary, but got {datatype}.')
        }

        @property
        def fields(self):
            """
            A dictionary of {field_name: field_instance}.
            """
            # `fields` is evaluated lazily. We do this to ensure that we don't
            # have issues importing modules that use ModelSerializers as
            # fields, even if Django's app-loading stage has not yet run.
            if not hasattr(self, '_fields'):
                self._fields = BindingDict(self)
                for key, value in self.get_fields().items():
                    self._fields[key] = value
            return self._fields

        @cached_property
        def _writable_fields(self):
            return [
                field for field in self.fields.values()
                if (not field.read_only) or (field.default is not empty)
            ]

        @cached_property
        def _readable_fields(self):
            return [
                field for field in self.fields.values() if not field.write_only
            ]

        def get_fields(self):
            """
            Returns a dictionary of {field_name: field_instance}.
            """
            # Every new serializer is created with a clone of the field
            # instances. This allows users to dynamically modify the fields
            # on a serializer instance without affecting every other
            # serializer class.
            return copy.deepcopy(self._declared_fields)

        def get_fields_metadata(self, field_name=None):
            """
            Returns a dictionary of {field_name: field_instance}.
            """
            # Every new serializer is created with a clone of the field
            # instances. This allows users to dynamically modify the fields
            # on a serializer instance without affecting every other
            # serializer class.
            fields_metadata = copy.deepcopy(self._declared_fields_metadata)
            if field_name is not None:
                return fields_metadata.get(field_name)
            return fields_metadata

        def get_validators(self):
            """
            Returns a list of validator callables.
            """
            # Used by the lazily-evaluated `validators` property.
            meta = getattr(self, 'Meta', None)
            validators = getattr(meta, 'validators', None)
            return validators[:] if validators else []

        def get_initial(self):
            if hasattr(self, 'initial_data'):
                return OrderedDict(
                    [
                        (
                            field_name,
                            field.get_value(self.initial_data)
                        )
                        for field_name, field
                        in self.fields.items()
                        if (
                            field.get_value(self.initial_data) is not empty
                        ) and not field.read_only
                    ]
                )

            return OrderedDict(
                [
                    (
                        field.field_name, field.get_initial()
                    )
                    for field
                    in self.fields.values()
                    if not field.read_only
                ]
            )

        def get_value(self, dictionary):
            # We override the default field access in order to support
            # nested HTML forms.
            if html.is_html_input(dictionary):
                return html.parse_html_dict(
                    dictionary, prefix=self.field_name
                ) or empty
            return dictionary.get(self.field_name, empty)

        def run_validation(self, data=empty):
            """
            We override the default `run_validation`, because the validation
            performed by validators and the `.validate()` method should
            be coerced into an error dictionary with a 'non_fields_error' key.
            """
            (is_empty_value, data) = self.validate_empty_values(data)
            if is_empty_value:
                return data

            value = self.to_internal_value(data)
            try:
                self.run_validators(value)
                value = self.validate(value)
                assert value is not None, '.validate() should return the ' \
                                          'validated data'
            except (ValidationError, DjangoValidationError) as exc:
                raise ValidationError(detail=as_serializer_error(exc))

            return value

        def to_internal_value(self, data):
            """
            Dict of native values <- Dict of primitive datatypes.
            """
            if not isinstance(data, Mapping):
                message = self.error_messages['invalid'].format(
                    datatype=type(data).__name__
                )
                raise ValidationError({
                    api_settings.NON_FIELD_ERRORS_KEY: [message]
                }, code='invalid')

            ret = OrderedDict()
            errors = OrderedDict()
            fields = self._writable_fields

            for field in fields:
                validate_method = getattr(self,
                                          'validate_' + field.field_name,
                                          None)
                primitive_value = field.get_value(data)
                try:
                    validated_value = field.run_validation(primitive_value)
                    if validate_method is not None:
                        validated_value = validate_method(validated_value)
                except ValidationError as exc:
                    errors[field.field_name] = exc.detail
                except DjangoValidationError as exc:
                    errors[field.field_name] = get_error_detail(exc)
                except SkipField:
                    pass
                else:
                    set_value(ret, field.source_attrs, validated_value)

            if errors:
                raise ValidationError(errors)

            return ret

        def to_representation(self, instance):
            """
            Object instance -> Dict of primitive datatypes.
            """
            ret = OrderedDict()
            fields = self._readable_fields

            for field in fields:
                try:
                    attribute = field.get_attribute(instance)
                except SkipField:
                    continue

                # We skip `to_representation` for `None` values so that
                # fields do not have to explicitly deal with that case.
                #
                # For related fields with `use_pk_only_optimization` we need to
                # resolve the pk value.
                check_for_none = attribute.pk \
                    if isinstance(attribute, PKOnlyObject) \
                    else attribute

                if check_for_none is None:
                    ret[field.field_name] = None
                else:
                    ret[field.field_name] = field.to_representation(attribute)

            return ret

        def validate(self, attrs):
            return attrs

        def __repr__(self):
            return unicode_to_repr(
                representation.serializer_repr(self, indent=1))

        # The following are used for accessing `BoundField` instances on the
        # serializer, for the purposes of presenting a form-like API onto the
        # field values and field errors.

        def __iter__(self):
            for field in self.fields.values():
                yield self[field.field_name]

        def __getitem__(self, key):
            field = self.fields[key]
            value = self.data.get(key)
            error = self.errors.get(key) if hasattr(self, '_errors') else None
            if isinstance(field, Serializer):
                return NestedBoundField(field, value, error)
            return BoundField(field, value, error)

        # Include a backlink to the serializer class on return objects.
        # Allows renderers such as HTMLFormRenderer to get the full field info.

        @property
        def data(self):
            ret = super(Serializer, self).data
            return ReturnDict(ret, serializer=self)

        @property
        def errors(self):
            ret = super(Serializer, self).errors
            if isinstance(ret, list) \
                    and len(ret) == 1 \
                    and getattr(ret[0], 'code', None) == 'null':

                # Edge case. Provide a more descriptive error than
                # "this field may not be null", when no data is passed.
                detail = ErrorDetail('No data provided', code='null')
                ret = {api_settings.NON_FIELD_ERRORS_KEY: [detail]}
            return ReturnDict(ret, serializer=self)

        def update(self, instance, validated_data):
            """Update method."""
            # It's critical to assign the validated data to the instance,
            # however we SHOULD NOT save it, since it will obviously make
            # things break. All of this is done to trick the rest_framework
            # to make a profit of all the nice things that it provides
            # with lowest cost possible.
            for key, value in validated_data.items():
                setattr(instance, key, value)
            return instance

    return Serializer
