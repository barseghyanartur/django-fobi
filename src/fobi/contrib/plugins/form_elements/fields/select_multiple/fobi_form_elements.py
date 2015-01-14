__title__ = 'fobi.contrib.plugins.form_elements.fields.select_multiple.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('SelectMultipleInputPlugin',)

from django.forms.fields import MultipleChoiceField
from django.forms.widgets import SelectMultiple
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme
from fobi.helpers import get_select_field_choices
from fobi.contrib.plugins.form_elements.fields.select_multiple import UID
from fobi.contrib.plugins.form_elements.fields.select_multiple.forms import (
    SelectMultipleInputForm
)

theme = get_theme(request=None, as_instance=True)

class SelectMultipleInputPlugin(FormFieldPlugin):
    """
    Select multiple field plugin.
    """
    uid = UID
    name = _("Select multiple")
    group = _("Fields")
    form = SelectMultipleInputForm

    def get_form_field_instances(self):
        """
        Get form field instances.
        """
        choices = get_select_field_choices(self.data.choices)

        kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'choices': choices,
            'widget': SelectMultiple(attrs={'class': theme.form_element_html_class}),
        }

        return [(self.data.name, MultipleChoiceField, kwargs)]


form_element_plugin_registry.register(SelectMultipleInputPlugin)
