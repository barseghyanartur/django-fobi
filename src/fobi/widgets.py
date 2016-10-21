from django.forms.widgets import RadioSelect, Select
from django.utils.html import format_html
from django.utils.safestring import mark_safe
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
    'RichSelect',
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


class RichSelect(Select):
    """Rich select widget with some rich enhancements.

    Based on original Select widget and intended to be a drop-off replacement.
    """

    def __init__(self, attrs=None, choices=(), prepend_html=None,
                 append_html=None):
        """Constructor.

        :param dict attrs:
        :param tuple choices:
        :param str prepend_html:
        :param str append_html:
        """
        self.prepend_html = prepend_html if prepend_html else ""
        self.append_html = append_html if append_html else ""
        super(RichSelect, self).__init__(attrs=attrs, choices=choices)

    def render(self, name, value, attrs=None):
        """Renders the element, having prepended and appended extra parts."""
        rendered_select = super(RichSelect, self).render(
            name=name,
            value=value,
            attrs=attrs
        )

        return mark_safe(
            '\n'.join([
                format_html(self.prepend_html),
                rendered_select,
                format_html(self.append_html)
            ])
        )
