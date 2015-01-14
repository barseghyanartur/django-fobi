__title__ = 'fobi.contrib.plugins.form_elements.fields.radio.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('RadioInputPlugin',)

from django.forms.fields import ChoiceField
from django.forms.widgets import RadioSelect
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme
from fobi.helpers import get_select_field_choices
from fobi.contrib.plugins.form_elements.fields.radio import UID
from fobi.contrib.plugins.form_elements.fields.radio.forms import RadioInputForm

theme = get_theme(request=None, as_instance=True)

class RadioInputPlugin(FormFieldPlugin):
    """
    Radio field plugin.
    """
    uid = UID
    name = _("Radio")
    group = _("Fields")
    form = RadioInputForm

    def get_form_field_instances(self):
        """
        Get form field instances.
        """
        choices = get_select_field_choices(self.data.choices)

        widget_attrs = {'class': theme.form_radio_element_html_class}
        kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'choices': choices,
            'widget': RadioSelect(attrs=widget_attrs),
        }

        return [(self.data.name, ChoiceField, kwargs)]


form_element_plugin_registry.register(RadioInputPlugin)
