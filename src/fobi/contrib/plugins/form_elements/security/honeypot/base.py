from __future__ import absolute_import

from django.forms.widgets import HiddenInput
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormElementPlugin, get_theme

from . import UID
from .fields import HoneypotField
from .forms import HoneypotInputForm

__title__ = 'fobi.contrib.plugins.form_elements.security.honeypot.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
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

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""

        field_kwargs = {
            'label': self.data.label,
            'initial': self.data.initial,
            # 'help_text': self.data.help_text,
            'required': self.data.required,
            'widget': HiddenInput(
                attrs={'class': theme.form_element_html_class}
            ),
        }

        if self.data.max_length is not None:
            field_kwargs['max_length'] = self.data.max_length

        # return [(self.data.name, (HoneypotField, TextInput), kwargs)]
        return [(self.data.name, HoneypotField, field_kwargs)]
