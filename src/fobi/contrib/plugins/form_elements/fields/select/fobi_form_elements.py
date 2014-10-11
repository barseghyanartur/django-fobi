__title__ = 'fobi.contrib.plugins.form_elements.fields.select.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('SelectInputPlugin',)

from django.forms.fields import ChoiceField
from django.forms.widgets import Select
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme
from fobi.contrib.plugins.form_elements.fields.select import UID
from fobi.contrib.plugins.form_elements.fields.select.forms import SelectInputForm

theme = get_theme(request=None, as_instance=True)

class SelectInputPlugin(FormFieldPlugin):
    """
    Select field plugin.
    """
    uid = UID
    name = _("Select")
    group = _("Fields")
    form = SelectInputForm

    def get_form_field_instances(self):
        """
        Get form field instances.
        """
        choices = []
        for choice in self.data.choices.split('\n'):
            choice = choice.strip()
            if ',' in choice:
                key, value = choice.split(',', 1)
                choices.append((key.strip(), value.strip()))
            else:
                choices.append((choice, choice))

        kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'choices': choices,
            'widget': Select(attrs={'class': theme.form_element_html_class}),
        }

        return [(self.data.name, ChoiceField, kwargs)]


form_element_plugin_registry.register(SelectInputPlugin)
