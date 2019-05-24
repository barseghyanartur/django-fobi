from django.apps import AppConfig

__title__ = 'fobi.contrib.plugins.form_elements.security.captcha.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)


class Config(AppConfig):
    """Config."""

    name = 'fobi.contrib.plugins.form_elements.security.captcha'
    label = 'fobi_contrib_plugins_form_elements_security_captcha'
