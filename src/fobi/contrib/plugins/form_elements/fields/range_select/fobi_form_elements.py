from django.forms.fields import ChoiceField
from django.forms.widgets import Select
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme

from . import UID
from .forms import RangeSelectInputForm
from .settings import INITIAL, MAX_VALUE, MIN_VALUE, STEP

__title__ = 'fobi.contrib.plugins.form_elements.fields.range_select.' \
            'fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('RangeSelectInputPlugin',)

theme = get_theme(request=None, as_instance=True)


class RangeSelectInputPlugin(FormFieldPlugin):
    """Range select input plugin."""

    uid = UID
    name = _("Range select")
    group = _("Fields")
    form = RangeSelectInputForm

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        initial = self.data.initial if self.data.initial else INITIAL
        max_value = self.data.max_value if self.data.max_value else MAX_VALUE
        min_value = self.data.min_value if self.data.min_value else MIN_VALUE
        step = self.data.step if self.data.step else STEP

        _choices = range(min_value, max_value+1, step)
        choices = zip(_choices, _choices)

        field_kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': initial,
            'required': self.data.required,
            'choices': choices,
            'widget': Select(attrs={'class': theme.form_element_html_class}),
        }

        return [(self.data.name, ChoiceField, field_kwargs)]


form_element_plugin_registry.register(RangeSelectInputPlugin)
