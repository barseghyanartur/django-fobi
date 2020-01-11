from __future__ import absolute_import

from django.forms.fields import DateField
from django.forms.widgets import DateInput
from django.utils.translation import gettext_lazy as _

from fobi.base import FormFieldPlugin, get_theme

from . import UID
from .forms import DateInputForm

__title__ = 'fobi.contrib.plugins.form_elements.fields.date.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DateInputPlugin',)

theme = get_theme(request=None, as_instance=True)


class DateInputPlugin(FormFieldPlugin):
    """Date field plugin."""

    uid = UID
    name = _("Date")
    group = _("Fields")
    form = DateInputForm

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        widget_attrs = {
            'class': theme.form_element_html_class,
            'type': 'date',
        }

        field_kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            # 'input_formats': self.data.input_formats,
            'required': self.data.required,
            'widget': DateInput(attrs=widget_attrs),
        }
        # if self.data.input_formats:
        #     kwargs['input_formats'] = self.data.input_formats

        return [(self.data.name, DateField, field_kwargs)]

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

        # Get the object
        value = form.cleaned_data.get(self.data.name, None)
        try:
            value = value.strftime("%Y-%m-%d")
        except Exception as err:
            pass

        # Overwrite ``cleaned_data`` of the ``form`` with object qualifier.
        form.cleaned_data[self.data.name] = value

        return form
