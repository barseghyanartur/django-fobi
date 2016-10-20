from django.forms.fields import ChoiceField
from django.forms.widgets import TextInput, Select
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme

from . import UID
from .forms import SliderInputForm
from .settings import INITIAL, MAX_VALUE, MIN_VALUE, STEP

__title__ = 'fobi.contrib.plugins.form_elements.fields.' \
            'slider_percentage.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('SliderInputPlugin',)

theme = get_theme(request=None, as_instance=True)


class SliderInputPlugin(FormFieldPlugin):
    """Slider field plugin."""

    uid = UID
    name = _("Slider")
    group = _("Fields")
    form = SliderInputForm
    html_classes = ['slider']

    def get_form_field_instances(self, request=None):
        """Get form field instances."""
        initial = self.data.initial if self.data.initial else INITIAL
        max_value = self.data.max_value if self.data.max_value else MAX_VALUE
        min_value = self.data.min_value if self.data.min_value else MIN_VALUE
        step = self.data.step if self.data.step else STEP

        _choices = range(min_value, max_value, step)
        choices = zip(_choices, _choices)

        kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': initial,
            'required': self.data.required,
            'choices': choices,
            'widget': Select(
                attrs={
                    'class': "slider {0}".format(
                        theme.form_element_html_class
                    ),
                    'data-slider-min': min_value,
                    'data-slider-max': max_value,
                    'data-slider-step': step,
                    'data-slider-value': initial,
                }
            ),
        }

        return [(self.data.name, ChoiceField, kwargs)]


form_element_plugin_registry.register(SliderInputPlugin)
