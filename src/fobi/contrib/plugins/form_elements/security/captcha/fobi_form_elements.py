__title__ = 'fobi.contrib.plugins.form_elements.security.captcha.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('CaptchaInputPlugin',)

import logging

from django.utils.translation import ugettext_lazy as _

logger = logging.getLogger(__name__)

DJANGO_RECAPTCHA_INSTALLED = False
DJANGO_SIMPLE_CAPTCHA_INSTALLED = False

try:
    from captcha.fields import CaptchaField, CaptchaTextInput
    DJANGO_SIMPLE_CAPTCHA_INSTALLED = True
except ImportError as e:
    # Logging original exception
    logger.error(e)

    # Trying to identify the problem
    try:
        import pip
        installed_packages = pip.get_installed_distributions()
        for installed_package in installed_packages:
            if "django-recaptcha" == str(installed_package.key):
                DJANGO_RECAPTCHA_INSTALLED = True
                logger.error(
                    "You have installed  the `django-recaptcha` in your "
                    "environment. At the moment you can't have both "
                    "`django-recaptcha` and `django-simple-captcha` installed "
                    "alongside due to app name collision (captcha). Remove "
                    "both packages using pip uninstall and reinstall the "
                    "`django-simple-captcha` if you want to make use of the "
                    "`fobi.contrib.plugins.form_elements.security.captcha` "
                    "package."
                    )
            if "django-simple-captcha" == str(installed_package.key):
                DJANGO_SIMPLE_CAPTCHA_INSTALLED = True

        if DJANGO_SIMPLE_CAPTCHA_INSTALLED and not DJANGO_RECAPTCHA_INSTALLED:
            logger.error(
                "You have installed  the `django-simple-captcha` in your "
                "environment, but imports seem to be broken.  Remove "
                "the package using pip uninstall and reinstall the "
                "`django-simple-captcha` if you want to make use of the "
                "`fobi.contrib.plugins.form_elements.security.captcha` "
                "package."
                )

    except ImportError:
        logger.error(
            "Likely you didn't yet install the"
            "`django-simple-captcha` package. Note, that at "
            "the moment you can't have both `django-recaptcha` "
            "and `django-simple-captcha` installed alongside "
            "due to app name collision (captcha)."
            )

from fobi.base import FormElementPlugin, form_element_plugin_registry, get_theme

from . import UID
from .forms import CaptchaInputForm

theme = get_theme(request=None, as_instance=True)

class CaptchaInputPlugin(FormElementPlugin):
    """
    Captcha field plugin.
    """
    uid = UID
    name = _("Captcha")
    group = _("Security")
    form = CaptchaInputForm

    def get_form_field_instances(self):
        """
        Get form field instances.
        """
        widget_attrs = {
            'class': theme.form_element_html_class,
            #'placeholder': self.data.placeholder,
        }

        kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            #'initial': self.data.initial,
            'required': self.data.required,
            'widget': CaptchaTextInput(attrs=widget_attrs),
        }

        return [(self.data.name, CaptchaField, kwargs)]


# Register only if safe to use.
if DJANGO_SIMPLE_CAPTCHA_INSTALLED and not DJANGO_RECAPTCHA_INSTALLED:
    form_element_plugin_registry.register(CaptchaInputPlugin)
