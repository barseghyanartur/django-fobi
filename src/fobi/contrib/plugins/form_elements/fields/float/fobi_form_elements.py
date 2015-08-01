__title__ = 'fobi.contrib.plugins.form_elements.fields.float.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('FloatInputPlugin',)

from django.forms.fields import FloatField
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme
from fobi.widgets import NumberInput

from . import UID
from .forms import FloatInputForm

theme = get_theme(request=None, as_instance=True)

class FloatInputPlugin(FormFieldPlugin):
    """
    Float input plugin.
    """
    uid = UID
    name = _("Float")
    group = _("Fields")
    form = FloatInputForm

    def get_form_field_instances(self):
        """
        Get form field instances.
        """
        widget_attrs = {
            'class': theme.form_element_html_class,
            'type': 'number',
            'placeholder': self.data.placeholder,
        }
        kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
        }
        if self.data.max_value:
            kwargs['max_value'] = self.data.max_value
            widget_attrs['max'] = self.data.max_value
        if self.data.min_value:
            kwargs['min_value'] = self.data.min_value
            widget_attrs['min'] = self.data.min_value

        kwargs['widget'] = NumberInput(attrs=widget_attrs)

        return [(self.data.name, FloatField, kwargs)]


form_element_plugin_registry.register(FloatInputPlugin)
