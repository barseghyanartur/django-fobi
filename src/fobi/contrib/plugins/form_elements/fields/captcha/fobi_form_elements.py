__title__ = 'fobi.contrib.plugins.form_elements.fields.captcha.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('CaptchaInputPlugin',)

from django.utils.translation import ugettext_lazy as _

from captcha.fields import CaptchaField, CaptchaTextInput

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme
from fobi.contrib.plugins.form_elements.fields.captcha import UID
from fobi.contrib.plugins.form_elements.fields.captcha.forms import CaptchaInputForm

theme = get_theme(request=None, as_instance=True)

class CaptchaInputPlugin(FormFieldPlugin):
    """
    Char field plugin.
    """
    uid = UID
    name = _("Captcha")
    group = _("Fields")
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


form_element_plugin_registry.register(CaptchaInputPlugin)
