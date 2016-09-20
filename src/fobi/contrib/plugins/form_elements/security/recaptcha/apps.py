__title__ = 'fobi.contrib.plugins.form_elements.security.recaptcha.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)

try:
    from django.apps import AppConfig

    class Config(AppConfig):
        """Config."""

        name = 'fobi.contrib.plugins.form_elements.security.recaptcha'
        label = 'fobi_contrib_plugins_form_elements_security_recaptcha'

except ImportError:
    pass
