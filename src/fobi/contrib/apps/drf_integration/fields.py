import copy

# import six
#
# from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from rest_framework.fields import (
    # Field,
    # empty,
    MultipleChoiceField,
)

__title__ = 'fobi.contrib.apps.drf_integration.fields'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'MultipleChoiceWithMaxField',
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
