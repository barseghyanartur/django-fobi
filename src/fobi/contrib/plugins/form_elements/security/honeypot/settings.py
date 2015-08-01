"""
- ``HONEYPOT_VALUE`` (string)
"""

__title__ = 'fobi.contrib.plugins.form_elements.security.honeypot.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('HONEYPOT_VALUE',)

from .conf import get_setting

HONEYPOT_VALUE = get_setting('HONEYPOT_VALUE')
