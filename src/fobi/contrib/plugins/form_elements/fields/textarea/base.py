from __future__ import absolute_import

from django.forms.fields import CharField
from django.forms.widgets import Textarea
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, get_theme

from . import UID
from .forms import TextareaForm

__title__ = 'fobi.contrib.plugins.form_elements.fields.textarea.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('TextareaPlugin',)

theme = get_theme(request=None, as_instance=True)


class TextareaPlugin(FormFieldPlugin):
    """Textarea field plugin."""

    uid = UID
    name = _("Textarea")
    group = _("Fields")
    form = TextareaForm

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        widget_attrs = {
            'class': theme.form_element_html_class,
            'placeholder': self.data.placeholder,
        }
        field_kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'widget': Textarea(attrs=widget_attrs)
        }

        if self.data.max_length:
            try:
                field_kwargs['max_length'] = int(self.data.max_length)
            except ValueError:
                field_kwargs['max_length'] = None
        else:
            field_kwargs['max_length'] = None

        field_kwargs['min_length'] = None

        return [(self.data.name, CharField, field_kwargs)]
