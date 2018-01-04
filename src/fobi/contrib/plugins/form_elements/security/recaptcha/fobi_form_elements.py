from __future__ import absolute_import

from fobi.base import form_element_plugin_registry

from .base import (
    DJANGO_RECAPTCHA_INSTALLED,
    DJANGO_SIMPLE_CAPTCHA_INSTALLED,
    ReCaptchaInputPlugin,
)

__title__ = 'fobi.contrib.plugins.form_elements.security.' \
            'recaptcha.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ReCaptchaInputPlugin',)


# Register only if safe to use.
if DJANGO_RECAPTCHA_INSTALLED and not DJANGO_SIMPLE_CAPTCHA_INSTALLED:
    form_element_plugin_registry.register(ReCaptchaInputPlugin)
