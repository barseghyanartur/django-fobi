__title__ = 'fobi.templatetags.future_compat'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('firstof',)

try:
    # We're using the Django 1.6 admin templates, that make use of new
    # things. One of the new additions (changed) was the ``firstof``
    # template tag. If we can't import it, we simply define it ourselves.
    from django.template.deafulttags import firstof
except ImportError:
    import warnings

    from django.template.base import Node, TemplateSyntaxError
    from django.template import Library
    from django.utils.timezone import template_localtime
    from django.utils.formats import localize
    from django.utils.encoding import force_text
    from django.utils.html import escape
    from django.utils.safestring import mark_safe, EscapeData, SafeData

    register = Library()

    def render_value_in_context(value, context):
        """Render value in context.

        Converts any value to a string to become part of a rendered template.
        This means escaping, if required, and conversion to a unicode object.
        If value is a string, it is expected to have already been translated.
        """
        value = template_localtime(value, use_tz=context.use_tz)
        value = localize(value, use_l10n=context.use_l10n)
        value = force_text(value)
        if ((context.autoescape and not isinstance(value, SafeData)) or
                isinstance(value, EscapeData)):
            return escape(value)
        else:
            return value

    class FirstOfNode(Node):
        """First of node."""

        def __init__(self, variables, escape=False):
            """Constructor."""
            self.vars = variables
            self.escape = escape  # only while the "future" version exists

        def render(self, context):
            """Render."""
            for var in self.vars:
                value = var.resolve(context, True)
                if value:
                    if not self.escape:
                        value = mark_safe(value)
                    return render_value_in_context(value, context)
            return ''

    @register.tag
    def firstof(parser, token, escape=False):
        """Outputs the first variable passed that is not False.

        Outputs the first variable passed that is not False, without escaping.

        Outputs nothing if all the passed variables are False.

        Sample usage::

            {% firstof var1 var2 var3 %}

        This is equivalent to::

            {% if var1 %}
                {{ var1|safe }}
            {% elif var2 %}
                {{ var2|safe }}
            {% elif var3 %}
                {{ var3|safe }}
            {% endif %}

        but obviously much cleaner!

        You can also use a literal string as a fallback value in case all
        passed variables are False::

            {% firstof var1 var2 var3 "fallback value" %}

        If you want to escape the output, use a filter tag::

            {% filter force_escape %}
                {% firstof var1 var2 var3 "fallback value" %}
            {% endfilter %}

        """
        if not escape:
            warnings.warn(
                "'The `firstof` template tag is changing to escape its "
                "arguments; the non-autoescaping version is deprecated. Load "
                "it from the `future` tag library to start using the new "
                "behavior.",
                DeprecationWarning, stacklevel=2)

        bits = token.split_contents()[1:]
        if len(bits) < 1:
            raise TemplateSyntaxError("'firstof' statement requires at least "
                                      "one argument")
        return FirstOfNode([parser.compile_filter(bit) for bit in bits],
                           escape=escape)
