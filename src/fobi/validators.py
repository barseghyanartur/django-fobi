import requests

from requests.exceptions import (
    ConnectionError,
    ConnectTimeout,
    ReadTimeout,
    SSLError,
    ProxyError,
    RetryError
)

from django.conf import settings
from django.core.urlresolvers import resolve, Resolver404

try:
    from localeurl.utils import strip_path
except ImportError as err:
    strip_path = None

__title__ = 'fobi.validators'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('url_exists',)


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
                ProxyError, RetryError) as err:
            return False

    else:
        if 'localeurl' in settings.INSTALLED_APPS and callable(strip_path):
            url = strip_path(url)[1]

        try:
            resolve(url)
            return True
        except Resolver404 as err:
            return False
