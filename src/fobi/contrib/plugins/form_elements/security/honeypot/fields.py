from django import forms
from django.utils.translation import ugettext_lazy as _

# from fobi.contrib.plugins.form_elements.security.honeypot.settings import (
#     HONEYPOT_VALUE
# )

__title__ = 'fobi.contrib.plugins.form_elements.security.honeypot.fields'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('HoneypotField',)


class HoneypotField(forms.CharField):
    """HoneypotField"""

    default_error_messages = {
        'invalid': _('Field value was tampered with.'),
    }
    widget = forms.HiddenInput

    def clean(self, value):
        """Check that honeypot value remained the same."""
        if value != self.initial:
            raise forms.ValidationError(
                self.error_messages['invalid'], code='invalid'
            )
        return value
