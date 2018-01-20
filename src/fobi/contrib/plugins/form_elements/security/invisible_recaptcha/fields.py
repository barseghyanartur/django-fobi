import logging

from django import forms
from django.utils.translation import ugettext_lazy as _

import requests

from .conf import get_setting
from .constants import SITE_VERIFY_URL
from .widgets import InvisibleRecaptchaWidget

__title__ = 'fobi.contrib.plugins.form_elements.security.' \
            'invisible_recaptcha.fields'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('InvisibleRecaptchaField',)

LOGGER = logging.getLogger(__name__)


class InvisibleRecaptchaField(forms.CharField):
    """Invisible reCAPTCHA field"""

    default_error_messages = {
        'invalid': _('Field value was tampered with.'),
        'validation_error': _('Invisible reCAPTCHA validation error'),
        'incorrect_captcha': _('Incorrect CAPTCHA, please try again'),
    }
    widget = InvisibleRecaptchaWidget

    def __init__(self, recaptcha_response=None, *args, **kwargs):
        self.recaptcha_response = recaptcha_response
        super(InvisibleRecaptchaField, self).__init__(*args, **kwargs)

    def clean(self, value):
        """Validation."""

        site_secret = get_setting('SITE_SECRET')

        if not (site_secret and self.recaptcha_response):
            raise forms.ValidationError(
                self.error_messages['validation_error'], code='invalid'
            )

        response = requests.post(
            SITE_VERIFY_URL,
            data={
                'secret': site_secret,
                'response': self.recaptcha_response,
            }
        )

        if response.status_code != requests.codes.ok:
            LOGGER.error(
                'Invisible reCAPTCHA error: %s: %s',
                response.status_code,
                response.reason
            )
            raise forms.ValidationError(
                self.error_messages['validation_error'], code='invalid'
            )
        else:
            response = response.json()

        error_codes = response.get('error-codes')
        if error_codes:
            LOGGER.error(
                'Invisible reCAPTCHA verification error: %s', error_codes
            )

        result = response.get('success')
        if result:
            LOGGER.info(response)
            return value

        raise forms.ValidationError(
            self.error_messages['incorrect_captcha'], code='invalid'
        )
