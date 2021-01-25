from __future__ import absolute_import

import decimal

from django.forms.fields import DecimalField
from django.utils.translation import gettext_lazy as _

from fobi.base import FormFieldPlugin, get_theme
from fobi.widgets import NumberInput

from . import UID
from .forms import DecimalInputForm

__title__ = 'fobi.contrib.plugins.form_elements.fields.' \
            'decimal.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DecimalInputPlugin',)

theme = get_theme(request=None, as_instance=True)


class DecimalInputPlugin(FormFieldPlugin):
    """Decimal input plugin."""

    uid = UID
    name = _("Decimal")
    group = _("Fields")
    form = DecimalInputForm

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
            'required': self.data.required,
        }

        if self.data.initial is not None:
            data_initial = decimal.Decimal(str(self.data.initial))
            field_kwargs.update({'initial': data_initial})

        if self.data.max_value is not None:
            data_max_value = decimal.Decimal(str(self.data.max_value))
            field_kwargs['max_value'] = data_max_value
            widget_attrs['max'] = data_max_value

        if self.data.min_value is not None:
            data_min_value = decimal.Decimal(str(self.data.min_value))
            field_kwargs['min_value'] = data_min_value
            widget_attrs['min'] = data_min_value

        if self.data.max_digits is not None:
            data_max_digits = int(self.data.max_digits)
            field_kwargs['max_digits'] = data_max_digits

        if self.data.decimal_places is not None:
            data_decimal_places = int(self.data.decimal_places)
            field_kwargs['decimal_places'] = data_decimal_places

        field_kwargs['widget'] = NumberInput(attrs=widget_attrs)

        return [(self.data.name, DecimalField, field_kwargs)]
