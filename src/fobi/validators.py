from django.urls import resolve, Resolver404

import requests

from requests.exceptions import (
    ConnectionError,
    ConnectTimeout,
    ReadTimeout,
    SSLError,
    ProxyError,
    RetryError,
)

__title__ = 'fobi.validators'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2019 Artur Barseghyan'
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
        try:
            resolve(url)
            return True
        except Resolver404 as err:
            return False
