from __future__ import absolute_import

from django.forms.fields import RegexField
from django.forms.widgets import TextInput
from django.utils.translation import gettext_lazy as _

from fobi.base import FormFieldPlugin, get_theme

from . import UID
from .forms import RegexInputForm

__title__ = 'fobi.contrib.plugins.form_elements.fields.regex.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('RegexInputPlugin',)

theme = get_theme(request=None, as_instance=True)


class RegexInputPlugin(FormFieldPlugin):
    """Regex field plugin."""

    uid = UID
    name = _("Regex")
    group = _("Fields")
    form = RegexInputForm

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        widget_attrs = {
            'class': theme.form_element_html_class,
            'placeholder': self.data.placeholder,
        }

        field_kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'regex': self.data.regex,
            'initial': self.data.initial,
            'required': self.data.required,
            'widget': TextInput(attrs=widget_attrs),
        }

        if self.data.max_length is not None:
            field_kwargs['max_length'] = self.data.max_length

        return [(self.data.name, RegexField, field_kwargs)]
