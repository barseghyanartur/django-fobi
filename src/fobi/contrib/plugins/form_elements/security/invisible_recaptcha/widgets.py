from django.forms.widgets import HiddenInput

from fobi.base import FormElementPluginWidget

from . import UID
from .conf import get_setting

__title__ = 'fobi.contrib.plugins.form_elements.security.' \
            'invisible_recaptcha.widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'InvisibleRecaptchaWidget',
    'BaseInvisibleRecaptchaWidget',
)


class InvisibleRecaptchaWidget(HiddenInput):
    """Invisible recaptcha widget."""

    def __init__(self, *args, **kwargs):
        site_key = get_setting("SITE_KEY")
        if not site_key:
            raise ValueError("SITE_KEY not set")

        attrs = kwargs.get("attrs", {})
        attrs["data-customforms"] = "disabled"
        attrs["data-recaptcha-field"] = "true"
        attrs["value"] = site_key

        kwargs["attrs"] = attrs
        super(InvisibleRecaptchaWidget, self).__init__(*args, **kwargs)


class BaseInvisibleRecaptchaWidget(FormElementPluginWidget):
    """Base invisible recaptcha form element plugin widget."""

    plugin_uid = UID
    html_classes = ['invisible-recaptcha']
    media_js = [
        'https://www.google.com/recaptcha/api.js',
        'invisible_recaptcha/fobi.plugin.invisible_recaptcha.js',
    ]
