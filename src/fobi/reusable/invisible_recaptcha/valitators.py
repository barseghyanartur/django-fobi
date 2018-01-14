import logging

from django.conf import settings

import requests

__title__ = 'fobi.reusablbe.invisible_recaptcha.validators'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('validate_invisible_recaptcha',)


LOGGER = logging.getLogger(__name__)


def validate_invisible_recaptcha(data):
    RECAPTCHA_FIELD = 'g-recaptcha-response'
    SITE_VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'
    site_secret = getattr(settings, 'FOBI_INVISIBLE_RECAPTCHA_SITE_SECRET', '')
    recaptcha_response = data.get(RECAPTCHA_FIELD)
    if not (site_secret and recaptcha_response):
        return False, 'Captcha validation error'

    response = requests.post(
        SITE_VERIFY_URL,
        data={
            'secret': site_secret,
            'response': recaptcha_response,
        }
    )

    if response.status_code != requests.codes.ok:
        LOGGER.error(
            'recaptcha: Error: %s: %s',
            response.status_code,
            response.reason
        )
        return False, 'Captcha validation error'
    else:
        response = response.json()

    error_codes = response.get('error-codes')
    if error_codes:
        LOGGER.error('recaptcha verification error: %s', error_codes)

    result = response.get('success')
    if result:
        return True, ''

    return False, 'Incorrect captcha, please try again'
