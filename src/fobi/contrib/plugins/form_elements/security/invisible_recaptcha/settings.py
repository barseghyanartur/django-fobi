"""
- ``SITE_KEY`` (string)
- ``SITE_SECRET`` (string)
"""
from .conf import get_setting

__title__ = 'fobi.contrib.plugins.form_elements.security.' \
            'invisible_recaptcha.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'SITE_KEY',
    'SITE_SECRET',
)

SITE_KEY = get_setting('SITE_KEY')
SITE_SECRET = get_setting('SITE_SECRET')
