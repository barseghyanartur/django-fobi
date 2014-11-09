__title__ = 'fobi.contrib.plugins.form_elements.fields.date.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DateInputPlugin',)

from django.forms.fields import DateField
from django.forms.widgets import DateInput#, TextInput
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme
from fobi.contrib.plugins.form_elements.fields.date import UID
from fobi.contrib.plugins.form_elements.fields.date.forms import DateInputForm

theme = get_theme(request=None, as_instance=True)

class DateInputPlugin(FormFieldPlugin):
    """
    Date field plugin.
    """
    uid = UID
    name = _("Date")
    group = _("Fields")
    form = DateInputForm

    def get_form_field_instances(self):
        """
        Get form field instances.
        """
        widget_attrs = {
            'class': theme.form_element_html_class,
            'type': 'date',
        }

        kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            #'input_formats': self.data.input_formats,
            'required': self.data.required,
            'widget': DateInput(attrs=widget_attrs),
        }
        #if self.data.input_formats:
        #    kwargs['input_formats'] = self.data.input_formats

        return [(self.data.name, DateField, kwargs)]


form_element_plugin_registry.register(DateInputPlugin)
