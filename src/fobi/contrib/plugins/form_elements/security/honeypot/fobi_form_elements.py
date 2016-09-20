from django.forms.widgets import HiddenInput
from django.utils.translation import ugettext_lazy as _

from fobi.base import (
    FormElementPlugin, form_element_plugin_registry, get_theme
)

from . import UID
from .fields import HoneypotField
from .forms import HoneypotInputForm

__title__ = 'fobi.contrib.plugins.form_elements.security.' \
            'honeypot.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('HoneypotInputPlugin',)

theme = get_theme(request=None, as_instance=True)


class HoneypotInputPlugin(FormElementPlugin):
    """Honeypot field plugin."""

    uid = UID
    name = _("Honeypot")
    group = _("Security")
    form = HoneypotInputForm
    is_hidden = True

    def get_form_field_instances(self, request=None):
        """Get form field instances."""

        kwargs = {
            'label': self.data.label,
            'initial': self.data.initial,
            # 'help_text': self.data.help_text,
            'required': self.data.required,
            'widget': HiddenInput(
                attrs={'class': theme.form_element_html_class}
            ),
        }

        if self.data.max_length:
            kwargs['max_length'] = self.data.max_length

        # return [(self.data.name, (HoneypotField, TextInput), kwargs)]
        return [(self.data.name, HoneypotField, kwargs)]


form_element_plugin_registry.register(HoneypotInputPlugin)
