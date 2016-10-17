from django.forms.widgets import RadioSelect
from django.utils.translation import ugettext_lazy as _

# Safe import of ``NumberInput``
try:
    from django.forms.widgets import NumberInput
except ImportError:
    from django.forms.widgets import TextInput

    class NumberInput(TextInput):
        """Number input."""

        input_type = 'number'

__title__ = 'fobi.widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'NumberInput',
    'BooleanRadioSelect',
)


BOOLEAN_CHOICES = (
    (True, _("Yes")),
    (False, _("No"))
)


class BooleanRadioSelect(RadioSelect):
    """Boolean radio select for Django.

    :example:

    >>> class DummyForm(forms.Form):
    >>>     agree = forms.BooleanField(label=_("Agree?"),
    >>>                                required=False,
    >>>                                widget=BooleanRadioSelect)
    """

    def __init__(self, *args, **kwargs):
        """Constructor."""
        # Override the default renderer if we were passed one.
        renderer = kwargs.pop('renderer', None)
        if renderer:
            self.renderer = renderer

        if 'choices' not in kwargs:
            kwargs['choices'] = BOOLEAN_CHOICES

        super(BooleanRadioSelect, self).__init__(*args, **kwargs)
