from django.forms.fields import MultipleChoiceField
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


class MultipleChoiceWithMaxField(MultipleChoiceField):

    def __init__(self, max_choices=None, choices=(), required=True, widget=None,
                 label=None, initial=None, help_text='', *args, **kwargs):
        super(MultipleChoiceWithMaxField, self).__init__(
            choices=choices, required=required, widget=widget, label=label,
            initial=initial, help_text=help_text, *args, **kwargs
        )
        self.max_choices = max_choices

    def validate(self, value):
        super(MultipleChoiceWithMaxField, self).validate(value)
        if self.max_choices:
            if len(value) > self.max_choices:
                raise ValidationError(_("You must choose no more than {0} "
                                        "values.".format(self.max_choices)))
