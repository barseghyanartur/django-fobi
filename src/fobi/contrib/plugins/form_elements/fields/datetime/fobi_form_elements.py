__title__ = 'fobi.contrib.plugins.form_elements.fields.datetime.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DateTimeInputPlugin',)

from django.forms.fields import DateTimeField
from django.forms.widgets import DateTimeInput #, TextInput, SplitDateTimeWidget
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme
from fobi.contrib.plugins.form_elements.fields.datetime import UID
from fobi.contrib.plugins.form_elements.fields.datetime.forms \
    import DateTimeInputForm

theme = get_theme(request=None, as_instance=True)

class DateTimeInputPlugin(FormFieldPlugin):
    """
    DateTime field plugin.
    """
    uid = UID
    name = _("DateTime")
    group = _("Fields")
    form = DateTimeInputForm

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
            'widget': DateTimeInput(attrs=widget_attrs),
        }
        #if self.data.input_formats:
        #    kwargs['input_formats'] = self.data.input_formats

        return [(self.data.name, DateTimeField, kwargs)]


form_element_plugin_registry.register(DateTimeInputPlugin)
