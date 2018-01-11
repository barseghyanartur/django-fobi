import logging

from django.conf import settings

from nine import versions

import requests

from requests.exceptions import (
    ConnectionError,
    ConnectTimeout,
    ReadTimeout,
    SSLError,
    ProxyError,
    RetryError
)

if versions.DJANGO_LTE_1_11:
    from django.core.urlresolvers import resolve, Resolver404
else:
    from django.urls import resolve, Resolver404

try:
    from localeurl.utils import strip_path
except ImportError as err:
    strip_path = None

__title__ = 'fobi.validators'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('url_exists', 'validate_invisible_recaptcha')

logger = logging.getLogger(__name__)


def url_exists(url, local=False):
    """Check if URL exists.

    :param str url:
    :param bool local:
    :return bool:
    """
    if not local:
        try:
            r = requests.head(url)
            return r.status_code == requests.codes.ok
        except (ConnectionError, ConnectTimeout, ReadTimeout, SSLError,
                ProxyError, RetryError):
            return False

    else:
        if 'localeurl' in settings.INSTALLED_APPS and callable(strip_path):
            url = strip_path(url)[1]

        try:
            resolve(url)
            return True
        except Resolver404:
            return False


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
        logger.error(
            'recaptcha: Error: %s: %s',
            response.status_code,
            response.reason
        )
        return False, 'Captcha validation error'
    else:
        response = response.json()

    error_codes = response.get('error-codes')
    if error_codes:
        logger.error('recaptcha verification error: %s', error_codes)

    result = response.get('success')
    if result:
        return True, ''

    return False, 'Incorrect captcha, please try again'
