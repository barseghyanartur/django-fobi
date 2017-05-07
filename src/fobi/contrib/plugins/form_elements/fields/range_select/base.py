from __future__ import absolute_import

from django.forms.fields import ChoiceField
from django.forms.widgets import Select
from django.utils.translation import ugettext_lazy as _

from six import PY3

from ......base import FormFieldPlugin, get_theme

from . import UID
from .forms import RangeSelectInputForm
from .settings import (
    INITIAL,
    INITIAL_MAX_VALUE,
    INITIAL_MIN_VALUE,
    # MAX_VALUE,
    # MIN_VALUE,
    STEP
)

__title__ = 'fobi.contrib.plugins.form_elements.fields.range_select.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
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
        initial = self.get_initial()
        choices = self.get_choices()

        field_kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': initial,
            'required': self.data.required,
            'choices': choices,
            'widget': Select(attrs={'class': theme.form_element_html_class}),
        }

        return [(self.data.name, ChoiceField, field_kwargs)]

    def get_initial(self):
        """Get initial value.

        Might be used in integration plugins.
        """
        return int(self.data.initial) if self.data.initial else INITIAL

    def get_choices(self):
        """Get choices.

        Might be used in integration plugins.
        """
        max_value = int(self.data.max_value) \
            if self.data.max_value \
            else INITIAL_MAX_VALUE
        min_value = int(self.data.min_value) \
            if self.data.min_value \
            else INITIAL_MIN_VALUE
        step = int(self.data.step) if self.data.step else STEP

        if PY3:
            _choices = [__r for __r in range(min_value, max_value + 1, step)]
            choices = [(__k, __v) for __k, __v in zip(_choices, _choices)]
        else:
            _choices = range(min_value, max_value + 1, step)
            choices = zip(_choices, _choices)

        return choices
