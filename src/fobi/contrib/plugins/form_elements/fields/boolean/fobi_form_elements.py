from django.forms.fields import BooleanField
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry

from . import UID
from .forms import BooleanSelectForm

__title__ = 'fobi.contrib.plugins.form_elements.fields.boolean.' \
            'fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BooleanSelectPlugin',)


class BooleanSelectPlugin(FormFieldPlugin):
    """Boolean select plugin."""

    uid = UID
    name = _("Boolean")
    group = _("Fields")
    form = BooleanSelectForm

    def get_form_field_instances(self, request=None):
        """Get form field instances."""
        kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
        }

        return [(self.data.name, BooleanField, kwargs)]


form_element_plugin_registry.register(BooleanSelectPlugin)
