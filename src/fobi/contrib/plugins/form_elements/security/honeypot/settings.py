"""
- ``HONEYPOT_VALUE`` (string)
"""
from .conf import get_setting

__title__ = 'fobi.contrib.plugins.form_elements.security.honeypot.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('HONEYPOT_VALUE',)

HONEYPOT_VALUE = get_setting('HONEYPOT_VALUE')
