__title__ = 'fobi.contrib.plugins.form_handlers.mail.widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('MultiEmailWidget',)

import six

from django.forms.widgets import Textarea
from django.core.exceptions import ValidationError
from django.core import validators

from .settings import MULTI_EMAIL_FIELD_VALUE_SPLITTER

MULTI_EMAIL_FIELD_EMPTY_VALUES = validators.EMPTY_VALUES + ('[]',)

class MultiEmailWidget(Textarea):

    is_hidden = False

    def prep_value(self, value):
        """ Prepare value before effectively render widget """
        if value in MULTI_EMAIL_FIELD_EMPTY_VALUES:
            return ""
        elif isinstance(value, six.string_types):
            return value
        elif isinstance(value, list):
            return MULTI_EMAIL_FIELD_VALUE_SPLITTER.join(value)
        raise ValidationError('Invalid format.')

    def render(self, name, value, attrs=None):
        value = self.prep_value(value)
        return super(MultiEmailWidget, self).render(name, value, attrs)
