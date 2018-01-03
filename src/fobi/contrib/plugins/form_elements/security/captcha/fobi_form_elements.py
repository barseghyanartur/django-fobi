from __future__ import absolute_import

from fobi.base import form_element_plugin_registry

from .base import (
    CaptchaInputPlugin,
    DJANGO_RECAPTCHA_INSTALLED,
    DJANGO_SIMPLE_CAPTCHA_INSTALLED,
)

__title__ = 'fobi.contrib.plugins.form_elements.security.' \
            'captcha.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('CaptchaInputPlugin',)


# Register only if safe to use.
if DJANGO_SIMPLE_CAPTCHA_INSTALLED and not DJANGO_RECAPTCHA_INSTALLED:
    form_element_plugin_registry.register(CaptchaInputPlugin)
