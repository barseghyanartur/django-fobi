from fobi.base import form_element_plugin_widget_registry
from fobi.contrib.plugins.form_elements.security.invisible_recaptcha.widgets import (
    BaseInvisibleRecaptchaWidget,
)
from fobi.contrib.themes.foundation5 import UID

__title__ = (
    "fobi.contrib.themes.foundation5.widgets.form_elements."
    "invisible_recaptcha_foundation5_widget.fobi_form_elements"
)
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2019 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = ("InvisibleRecaptchaWidget",)


class InvisibleRecaptchaWidget(BaseInvisibleRecaptchaWidget):
    """Invisible reCAPTCHA widget plugin widget for  Foundation 5."""

    theme_uid = UID


# Registering the widget
form_element_plugin_widget_registry.register(InvisibleRecaptchaWidget)
