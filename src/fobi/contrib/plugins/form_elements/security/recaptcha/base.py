from __future__ import absolute_import

import logging

from django.utils.translation import gettext_lazy as _
from django.conf import settings

from fobi.base import (
    FormElementPlugin,
    get_theme,
)

from ......pip_helpers import check_if_installed, get_installed_packages
from . import UID
from .forms import ReCaptchaInputForm

logger = logging.getLogger(__name__)

DJANGO_RECAPTCHA_INSTALLED = False
DJANGO_SIMPLE_CAPTCHA_INSTALLED = False

try:
    from captcha.fields import ReCaptchaField
    from captcha.widgets import ReCaptchaV2Checkbox as ReCaptchaWidget

    DJANGO_RECAPTCHA_INSTALLED = True
except ImportError as e:
    # Logging original exception
    logger.error(e)

    # Trying to identify the problem
    try:
        installed_packages = get_installed_packages()

        if check_if_installed("django-simple-captcha", installed_packages):
            DJANGO_SIMPLE_CAPTCHA_INSTALLED = True
            logger.error(
                "You have installed  the `django-simple-captcha` in your "
                "environment. At the moment you can't have both "
                "`django-simple-captcha` and `django-recaptcha` installed "
                "alongside due to app name collision (captcha). Remove "
                "both packages using pip uninstall and reinstall the"
                "`django-recaptcha` if you want to make use of the "
                "`fobi.contrib.plugins.form_elements.security.recaptcha` "
                "package."
            )
        if check_if_installed("django-recaptcha", installed_packages):
            DJANGO_RECAPTCHA_INSTALLED = True

        if DJANGO_RECAPTCHA_INSTALLED and not DJANGO_SIMPLE_CAPTCHA_INSTALLED:
            logger.error(
                "You have installed  the `django-recaptcha` in your "
                "environment, but imports seem to be broken.  Remove "
                "the package using pip uninstall and reinstall the "
                "`django-recaptcha` if you want to make use of the "
                "`fobi.contrib.plugins.form_elements.security.recaptcha` "
                "package."
            )

    except ImportError:
        DJANGO_RECAPTCHA_INSTALLED = False
        logger.error(
            "; Likely you didn't yet install the"
            "`django-simple-captcha` package. Note, that at "
            "the moment you can't have both `django-recaptcha` "
            "and `django-simple-captcha` installed alongside "
            "due to app name collision (captcha)."
        )

__title__ = 'fobi.contrib.plugins.form_elements.security.' \
            'recaptcha.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ReCaptchaInputPlugin',)

theme = get_theme(request=None, as_instance=True)


class ReCaptchaInputPlugin(FormElementPlugin):
    """ReCaptcha field plugin."""

    uid = UID
    name = _("ReCaptcha")
    group = _("Security")
    form = ReCaptchaInputForm

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        widget_attrs = {
            'class': theme.form_element_html_class,
            # 'placeholder': self.data.placeholder,
        }

        field_kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            # 'initial': self.data.initial,
            'required': self.data.required,
            'widget': ReCaptchaWidget(attrs=widget_attrs),
        }

        return [(self.data.name, ReCaptchaField, field_kwargs)]
