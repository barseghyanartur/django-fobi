from __future__ import absolute_import

from django.forms.fields import NullBooleanField
from django.forms.widgets import NullBooleanSelect
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, get_theme

from . import UID
from .forms import NullBooleanSelectForm

__title__ = 'fobi.contrib.plugins.form_elements.fields.null_boolean.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('NullBooleanSelectPlugin',)

theme = get_theme(request=None, as_instance=True)


class NullBooleanSelectPlugin(FormFieldPlugin):
    """Null boolean select plugin."""

    uid = UID
    name = _("Null boolean")
    group = _("Fields")
    form = NullBooleanSelectForm

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        field_kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'widget': NullBooleanSelect(
                attrs={'class': theme.form_element_html_class}
            ),
        }

        return [(self.data.name, NullBooleanField, field_kwargs)]
