__title__ = 'fobi.contrib.plugins.form_elements.fields.slug.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('SlugInputPlugin',)

from django.forms.fields import SlugField
from django.forms.widgets import TextInput
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme

from . import UID
from .forms import SlugInputForm

theme = get_theme(request=None, as_instance=True)

class SlugInputPlugin(FormFieldPlugin):
    """
    Slug field plugin.
    """
    uid = UID
    name = _("Slug")
    group = _("Fields")
    form = SlugInputForm

    def get_form_field_instances(self):
        """
        Get form field instances.
        """
        widget_attrs = {
            'class': theme.form_element_html_class,
            'placeholder': self.data.placeholder,
        }

        kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'widget': TextInput(attrs=widget_attrs),
        }
        if self.data.max_length:
            kwargs['max_length'] = self.data.max_length

        return [(self.data.name, SlugField, kwargs)]


form_element_plugin_registry.register(SlugInputPlugin)
