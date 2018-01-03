import copy

import six

from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from rest_framework.fields import (
    ChoiceField,
    Field,
    empty,
    # ModelField,
    MultipleChoiceField,
)

__title__ = 'fobi.contrib.apps.drf_integration.fields'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'ContentImageField',
    'ContentMarkdownField',
    'ContentRichTextField',
    'ContentTextField',
    'ContentVideoField',
    'ModelChoiceField',
    'ModelMultipleChoiceField',
    'MultipleChoiceWithMaxField',
    'NoneField',
)

# *****************************************************************************
# *****************************************************************************
# ************************** Additional DRF fields ****************************
# *****************************************************************************
# *****************************************************************************

# *****************************************************************************
# *************************** Traditional fields ******************************


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


class ModelChoiceFieldMixin(object):
    """Model choice field mixin."""

    def get_choices(self):
        """Get choices."""
        choices = []
        if self.model_attr:
            for _choice in self.queryset:
                choices.append((_choice.pk, getattr(_choice, self.model_attr)))
        else:
            for _choice in self.queryset:
                choices.append((_choice.pk, six.text_type(_choice)))
        return choices


class ModelChoiceField(ChoiceField, ModelChoiceFieldMixin):
    """Model choice field."""

    def __init__(self, *args, **kwargs):
        self.queryset = kwargs.pop('queryset', None)
        self.model_attr = kwargs.pop('model_attr', None)
        choices = self.get_choices()
        kwargs.update({'choices': choices})
        super(ModelChoiceField, self).__init__(*args, **kwargs)


class ModelMultipleChoiceField(MultipleChoiceField, ModelChoiceFieldMixin):
    """Model choice field."""

    def __init__(self, *args, **kwargs):
        self.queryset = kwargs.pop('queryset', None)
        self.model_attr = kwargs.pop('model_attr', None)
        choices = self.get_choices()
        kwargs.update({'choices': choices})
        super(ModelMultipleChoiceField, self).__init__(*args, **kwargs)

# *****************************************************************************
# ************************* Presentational fields *****************************
# *****************************************************************************


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


class ContentRichTextField(NoneField):
    """Content rich text field."""


class ContentMarkdownField(NoneField):
    """Content markdown field."""


class ContentImageField(NoneField):
    """Content image field."""


class ContentVideoField(NoneField):
    """Content video field."""
