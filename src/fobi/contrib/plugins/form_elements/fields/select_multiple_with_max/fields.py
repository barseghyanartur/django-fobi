from django.core.exceptions import ValidationError
from django.forms.fields import MultipleChoiceField
from django.utils.translation import gettext_lazy as _

__title__ = 'fobi.contrib.plugins.form_elements.fields.' \
            'select_multiple_with_max.fields'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('MultipleChoiceWithMaxField',)


class MultipleChoiceWithMaxField(MultipleChoiceField):
    """Multiple choice with max field."""

    def __init__(self, max_choices=None, choices=(), required=True,
                 widget=None, label=None, initial=None, help_text='', *args,
                 **kwargs):
        """Constructor."""
        super(MultipleChoiceWithMaxField, self).__init__(
            choices=choices, required=required, widget=widget, label=label,
            initial=initial, help_text=help_text, *args, **kwargs
        )
        self.max_choices = max_choices

    def validate(self, value):
        """Validate."""
        super(MultipleChoiceWithMaxField, self).validate(value)
        if self.max_choices:
            if len(value) > self.max_choices:
                raise ValidationError(_("You must choose no more than {0} "
                                        "values.".format(self.max_choices)))
