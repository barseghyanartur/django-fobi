# from django.utils.html import format_html
from django.forms.widgets import HiddenInput
from django.utils.safestring import mark_safe

from fobi.base import FormElementPluginWidget

from . import UID
from .conf import get_setting

__title__ = 'fobi.contrib.plugins.form_elements.security.' \
            'invisible_recaptcha.widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'InvisibleRecaptchaWidget',
    'BaseInvisibleRecaptchaWidget',
)


class InvisibleRecaptchaWidget(HiddenInput):
    """Invisible recaptcha widget."""

    def __init__(self, *args, **kwargs):
        attrs = kwargs.get('attrs', {})
        attrs.update({'data-customforms': 'disabled'})
        kwargs.update({'attrs': attrs})
        super(InvisibleRecaptchaWidget, self).__init__(*args, **kwargs)

    def render(self, *args, **kwargs):
        """Returns this Widget rendered as HTML, as a Unicode string."""
        html = super(InvisibleRecaptchaWidget, self).render(*args, **kwargs)
        g_recaptcha_sitekey = get_setting('SITE_KEY')
        invisible_recaptcha_html = """
            <script>
                var InvisibleRecaptchaSiteKey = "{g_recaptcha_sitekey}";
            </script>
        """.format(
            g_recaptcha_sitekey=g_recaptcha_sitekey
        )
        return html + mark_safe(invisible_recaptcha_html)


class BaseInvisibleRecaptchaWidget(FormElementPluginWidget):
    """Base invisible recaptcha form element plugin widget."""

    plugin_uid = UID
    html_classes = ['invisible-recaptcha']
    media_js = [
        'https://www.google.com/recaptcha/api.js',
        'invisible_recaptcha/fobi.plugin.invisible_recaptcha.js',
    ]
