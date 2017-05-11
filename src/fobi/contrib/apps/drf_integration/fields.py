import copy

import six

from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from rest_framework.fields import (
    Field,
    empty,
    MultipleChoiceField,
)

__title__ = 'fobi.contrib.apps.drf_integration.fields'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'ContentImageField',
    'ContentTextField',
    'ContentVideoField',
    'MultipleChoiceWithMaxField',
    'NoneField',
)


class MultipleChoiceWithMaxField(MultipleChoiceField):
    """MultipleChoiceWithMaxField."""

    default_error_messages = copy.copy(
        MultipleChoiceField.default_error_messages
    )
    default_error_messages.update({
        'max_choices': _('Max number of choices reached.'),
    })

    def __init__(self, *args, **kwargs):
        self.max_choices = kwargs.pop('max_choices', None)
        super(MultipleChoiceWithMaxField, self).__init__(*args, **kwargs)

    def to_internal_value(self, data):
        if self.max_choices:
            if len(data) > self.max_choices:
                self.fail('max_choices')

        return super(
            MultipleChoiceWithMaxField,
            self
        ).to_internal_value(data)


class NoneField(Field):
    """NoneField."""

    default_error_messages = {}
    initial = ''
    default_empty_html = ''

    def __init__(self, **kwargs):
        self.allow_blank = True
        self.trim_whitespace = kwargs.pop('trim_whitespace', True)
        self.raw_data = kwargs.pop('raw_data', {})
        super(NoneField, self).__init__(**kwargs)

    def run_validation(self, data=empty):
        return ''

    def to_internal_value(self, data):
        # We're lenient with allowing basic numerics to be coerced into
        # strings, but other types should fail. Eg. unclear if booleans
        # should represent as `true` or `True`, and composites such as lists
        # are likely user error.
        _not_isinstance_str_int_float = not isinstance(
            data, six.string_types + six.integer_types + (float,)
        )
        if isinstance(data, bool) or _not_isinstance_str_int_float:
            self.fail('invalid')
        value = six.text_type(data)
        return value.strip() if self.trim_whitespace else value

    def to_representation(self, value):
        return mark_safe(six.text_type(value))


class ContentTextField(NoneField):
    """Content text field."""


class ContentImageField(NoneField):
    """Content image field."""


class ContentVideoField(NoneField):
    """Content video field."""

