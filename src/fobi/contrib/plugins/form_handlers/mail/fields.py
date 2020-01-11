from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

from .widgets import MultiEmailWidget
from .settings import MULTI_EMAIL_FIELD_VALUE_SPLITTER

__title__ = 'fobi.contrib.plugins.form_handlers.mail.widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('MultiEmailField',)


class MultiEmailField(forms.Field):
    """MultiEmailField."""

    message = _('Enter valid email addresses.')
    code = 'invalid'
    widget = MultiEmailWidget

    def to_python(self, value):
        """Normalize data to a list of strings."""
        # Return None if no input was given.
        if not value:
            return []
        return [v.strip()
                for v in value.split(MULTI_EMAIL_FIELD_VALUE_SPLITTER)
                if v != ""]

    def validate(self, value):
        """Check if value consists only of valid emails."""

        # Use the parent's handling of required fields, etc.
        super(MultiEmailField, self).validate(value)
        try:
            for email in value:
                validate_email(email)
        except ValidationError:
            raise ValidationError(self.message, code=self.code)
