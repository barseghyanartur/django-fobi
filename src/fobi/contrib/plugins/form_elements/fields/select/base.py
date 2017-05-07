from __future__ import absolute_import

from django.forms.fields import ChoiceField
from django.forms.widgets import Select
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, get_theme
from fobi.constants import (
    SUBMIT_VALUE_AS_VAL,
    SUBMIT_VALUE_AS_REPR,
)
from fobi.helpers import get_select_field_choices, safe_text

from . import UID
from .forms import SelectInputForm
from .settings import SUBMIT_VALUE_AS

__title__ = 'fobi.contrib.plugins.form_elements.fields.select.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('SelectInputPlugin',)

theme = get_theme(request=None, as_instance=True)


class SelectInputPlugin(FormFieldPlugin):
    """Select field plugin."""

    uid = UID
    name = _("Select")
    group = _("Fields")
    form = SelectInputForm

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        choices = self.get_choices()

        field_kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'choices': choices,
            'widget': Select(attrs={'class': theme.form_element_html_class}),
        }

        return [(self.data.name, ChoiceField, field_kwargs)]

    def get_choices(self):
        """Get choices.

        Might be used in integration plugins.
        """
        return get_select_field_choices(self.data.choices)

    def submit_plugin_form_data(self, form_entry, request, form,
                                form_element_entries=None, **kwargs):
        """Submit plugin form data/process.

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        """
        # In case if we should submit value as is, we don't return anything.
        # In other cases, we proceed further.
        if SUBMIT_VALUE_AS != SUBMIT_VALUE_AS_VAL:
            # Get the object
            value = form.cleaned_data.get(self.data.name, None)

            # Get choices
            choices = dict(self.get_choices())

            if value in choices:
                # Handle the submitted form value

                label = safe_text(choices.get(value))

                # Should be returned as repr
                if SUBMIT_VALUE_AS == SUBMIT_VALUE_AS_REPR:
                    value = label
                # Should be returned as mix
                else:
                    value = "{0} ({1})".format(label, value)

                # Overwrite ``cleaned_data`` of the ``form`` with object
                # qualifier.
                form.cleaned_data[self.data.name] = value

                # It's critically important to return the ``form`` with
                # updated ``cleaned_data``
                return form
