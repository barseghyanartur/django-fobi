from __future__ import absolute_import

from django.forms.fields import URLField

try:
    from django.forms.widgets import URLInput
except ImportError:
    from django.forms.widgets import TextInput

    class URLInput(TextInput):
        """URL input."""

        input_type = 'url'

from django.utils.translation import gettext_lazy as _

from fobi.base import FormFieldPlugin, get_theme

from . import UID
from .forms import URLInputForm

__title__ = 'fobi.contrib.plugins.form_elements.fields.url.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('URLInputPlugin',)

theme = get_theme(request=None, as_instance=True)


class URLInputPlugin(FormFieldPlugin):
    """URL input plugin."""

    uid = UID
    name = _("URL")
    group = _("Fields")
    form = URLInputForm

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        widget_attrs = {
            'class': theme.form_element_html_class,
            'type': 'url',
            'placeholder': self.data.placeholder,
        }

        field_kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'widget': URLInput(attrs=widget_attrs),
        }

        if self.data.max_length:
            try:
                field_kwargs['max_length'] = int(self.data.max_length)
            except ValueError:
                field_kwargs['max_length'] = None
        else:
            field_kwargs['max_length'] = None

        field_kwargs['min_length'] = None

        return [(self.data.name, URLField, field_kwargs)]
