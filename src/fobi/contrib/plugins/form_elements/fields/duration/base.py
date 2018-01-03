from __future__ import absolute_import

import datetime

from django.forms.fields import DurationField
from django.forms.widgets import TextInput
from django.utils.duration import duration_string
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, get_theme

from . import UID
from .forms import DurationInputForm

__title__ = 'fobi.contrib.plugins.form_elements.fields.duration.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DurationInputPlugin',)

theme = get_theme(request=None, as_instance=True)


class DurationInputPlugin(FormFieldPlugin):
    """Duration field plugin."""

    uid = UID
    name = _("Duration")
    group = _("Fields")
    form = DurationInputForm

    def get_form_field_instances(self,
                                 request=None,
                                 form_entry=None,
                                 form_element_entries=None,
                                 **kwargs):
        """Get form field instances."""
        widget_attrs = {
            'class': theme.form_element_html_class,
            'placeholder': self.data.placeholder,
        }

        field_kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'widget': TextInput(attrs=widget_attrs),
        }
        # initial_kwargs = {}
        # if self.data.weeks:
        #     initial_kwargs.update({'weeks': self.data.weeks})
        # if self.data.days:
        #     initial_kwargs.update({'days': self.data.days})
        # if self.data.hours:
        #     initial_kwargs.update({'hours': self.data.hours})
        # if self.data.minutes:
        #     initial_kwargs.update({'minutes': self.data.minutes})
        # if self.data.seconds:
        #     initial_kwargs.update({'seconds': self.data.seconds})
        # initial = datetime.timedelta(**initial_kwargs)

        return [(self.data.name, DurationField, field_kwargs)]

    def prepare_plugin_form_data(self, cleaned_data):
        """Prepare plugin form data.

        Might be used in integration plugins.
        """
        value = cleaned_data.get(self.data.name, None)

        if isinstance(value, datetime.timedelta):
            value = duration_string(value)
            # Overwrite ``cleaned_data`` of the ``form`` with object
            # qualifier.
            cleaned_data[self.data.name] = value

            # It's critically important to return the ``form`` with updated
            # ``cleaned_data``
            return cleaned_data

    def submit_plugin_form_data(self,
                                form_entry,
                                request,
                                form,
                                form_element_entries=None,
                                **kwargs):
        """Submit plugin form data/process.

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        """
        # In case if we should submit value as is, we don't return anything.
        # In other cases, we proceed further.

        # Get the object
        value = form.cleaned_data.get(self.data.name, None)

        if isinstance(value, datetime.timedelta):
            value = duration_string(value)

            # Overwrite ``cleaned_data`` of the ``form`` with object
            # qualifier.
            form.cleaned_data[self.data.name] = value

        # It's critically important to return the ``form`` with
        # updated ``cleaned_data``
        return form
