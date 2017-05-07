from __future__ import absolute_import

from django.forms.fields import FloatField
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, get_theme
from fobi.widgets import NumberInput

from . import UID
from .forms import FloatInputForm

__title__ = 'fobi.contrib.plugins.form_elements.fields.float.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('FloatInputPlugin',)

theme = get_theme(request=None, as_instance=True)


class FloatInputPlugin(FormFieldPlugin):
    """Float input plugin."""

    uid = UID
    name = _("Float")
    group = _("Fields")
    form = FloatInputForm

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        widget_attrs = {
            'class': theme.form_element_html_class,
            'type': 'number',
            'placeholder': self.data.placeholder,
        }

        field_kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
        }

        if self.data.max_value:
            data_max_value = float(self.data.max_value)
            field_kwargs['max_value'] = data_max_value
            widget_attrs['max'] = data_max_value

        if self.data.min_value:
            data_min_value = float(self.data.min_value)
            field_kwargs['min_value'] = data_min_value
            widget_attrs['min'] = data_min_value

        field_kwargs['widget'] = NumberInput(attrs=widget_attrs)

        return [(self.data.name, FloatField, field_kwargs)]
