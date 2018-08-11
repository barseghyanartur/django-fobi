from django.forms.widgets import RadioSelect, Select
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from nine import versions

from .helpers import flatatt_inverse_quotes

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
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'BooleanRadioSelect',
    'NumberInput',
    'RichSelect',
    'RichSelectInverseQuotes',
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
                 append_html=None, override_name=None):
        """Constructor.

        :param dict attrs:
        :param tuple choices:
        :param str prepend_html:
        :param str append_html:
        :param str override_name:
        """
        self.prepend_html = prepend_html if prepend_html else ""
        self.append_html = append_html if append_html else ""
        self.override_name = override_name \
            if override_name is not None \
            else None
        super(RichSelect, self).__init__(attrs=attrs, choices=choices)

    def render(self, name, value, attrs=None, **kwargs):
        """Renders the element, having prepended and appended extra parts."""
        if self.override_name is not None:
            name = self.override_name

        rendered_select = super(RichSelect, self).render(
            name=name,
            value=value,
            attrs=attrs,
            **kwargs
        )

        return mark_safe(
            '\n'.join([
                format_html(self.prepend_html),
                rendered_select,
                format_html(self.append_html)
            ])
        )


class RichSelectInverseQuotes(RichSelect):
    """Almost same as original, but uses alternative flatatt function.

    Uses inverse quotes.
    """
    if versions.DJANGO_GTE_1_11:
        template_name = 'fobi/django/forms/widgets/rich_select_inverse.html'
        option_template_name = 'fobi/django/forms/widgets/' \
                               'rich_select_inverse_option.html'

    elif versions.DJANGO_GTE_1_10:
        def render(self, name, value, attrs=None, **kwargs):
            if self.override_name is not None:
                name = self.override_name

            if value is None:
                value = ''

            if not attrs:
                attrs = self.attrs
            else:
                attrs.update(self.attrs)

            if versions.DJANGO_GTE_1_11:
                final_attrs = self.build_attrs(
                    attrs,
                    extra_attrs={'name': name}
                )
            else:
                final_attrs = self.build_attrs(attrs, name=name)

            output = [
                format_html('<select{}>', flatatt_inverse_quotes(final_attrs))
            ]
            options = self.render_options([value])
            if options:
                output.append(options)
            output.append('</select>')
            rendered_select = mark_safe('\n'.join(output))

            return mark_safe(
                '\n'.join([
                    format_html(self.prepend_html),
                    rendered_select,
                    format_html(self.append_html)
                ])
            )

    else:
        def render(self, name, value, attrs=None, choices=()):
            if self.override_name is not None:
                name = self.override_name

            if value is None:
                value = ''

            if not attrs:
                attrs = self.attrs
            else:
                attrs.update(self.attrs)

            if versions.DJANGO_GTE_1_11:
                final_attrs = self.build_attrs(
                    attrs,
                    extra_attrs={'name': name}
                )
            else:
                final_attrs = self.build_attrs(attrs, name=name)

            output = [
                format_html('<select{}>', flatatt_inverse_quotes(final_attrs))
            ]
            options = self.render_options(choices, [value])
            if options:
                output.append(options)
            output.append('</select>')
            rendered_select = mark_safe('\n'.join(output))

            return mark_safe(
                '\n'.join([
                    format_html(self.prepend_html),
                    rendered_select,
                    format_html(self.append_html)
                ])
            )
