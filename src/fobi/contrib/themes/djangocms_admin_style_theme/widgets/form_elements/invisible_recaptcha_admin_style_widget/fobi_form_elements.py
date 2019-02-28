from fobi.base import form_element_plugin_widget_registry
from fobi.contrib.plugins.form_elements.security.invisible_recaptcha.widgets \
    import (
        BaseInvisibleRecaptchaWidget
    )
from fobi.contrib.themes.simple import UID

__title__ = 'fobi.contrib.themes.djangocms_admin_style_theme.widgets.' \
            'form_elements.invisible_recaptcha_admin_style_widget.s' \
            'fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('InvisibleRecaptchaWidget',)


class InvisibleRecaptchaWidget(BaseInvisibleRecaptchaWidget):
    """Invisible reCAPTCHA widget plugin widget for Simple theme."""

    theme_uid = UID


# Registering the widget
form_element_plugin_widget_registry.register(InvisibleRecaptchaWidget)
