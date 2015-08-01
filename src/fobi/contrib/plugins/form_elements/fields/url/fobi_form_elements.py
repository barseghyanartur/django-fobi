__title__ = 'fobi.contrib.plugins.form_elements.fields.url.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('URLInputPlugin',)

from django.forms.fields import URLField

try:
    from django.forms.widgets import URLInput
except ImportError:
    from django.forms.widgets import TextInput
    class URLInput(TextInput):
        input_type = 'url'

from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme

from . import UID
from .forms import URLInputForm

theme = get_theme(request=None, as_instance=True)

class URLInputPlugin(FormFieldPlugin):
    """
    URL input plugin.
    """
    uid = UID
    name = _("URL")
    group = _("Fields")
    form = URLInputForm

    def get_form_field_instances(self):
        """
        Get form field instances.
        """
        widget_attrs = {
            'class': theme.form_element_html_class,
            'type': 'url',
            'placeholder': self.data.placeholder,
        }

        kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'widget': URLInput(attrs=widget_attrs),
        }
        if self.data.max_length:
            kwargs['max_length'] = self.data.max_length

        return [(self.data.name, URLField, kwargs)]


form_element_plugin_registry.register(URLInputPlugin)
