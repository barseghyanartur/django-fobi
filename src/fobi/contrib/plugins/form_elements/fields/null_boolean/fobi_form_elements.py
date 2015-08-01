__title__ = 'fobi.contrib.plugins.form_elements.fields.null_boolean.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('NullBooleanSelectPlugin',)

from django.forms.fields import NullBooleanField
from django.forms.widgets import NullBooleanSelect
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme

from . import UID
from .forms import NullBooleanSelectForm

theme = get_theme(request=None, as_instance=True)

class NullBooleanSelectPlugin(FormFieldPlugin):
    """
    Booean select plugin.
    """
    uid = UID
    name = _("Null boolean")
    group = _("Fields")
    form = NullBooleanSelectForm

    def get_form_field_instances(self):
        """
        Get form field instances.
        """
        kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'widget': NullBooleanSelect(attrs={'class': theme.form_element_html_class}),
        }

        return [(self.data.name, NullBooleanField, kwargs)]


form_element_plugin_registry.register(NullBooleanSelectPlugin)
