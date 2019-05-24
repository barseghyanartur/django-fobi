from ..base import get_theme

__title__ = 'fobi.integration.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('get_template_choices',)


def get_template_choices(source, choices, theme_specific_choices_key):
    """Get the template choices.

    It's possible to provide theme templates per theme or just per project.

    :param str source: Example value 'feincms_integration'.
    :param tuple or list choices:
    :param str theme_specific_choices_key:
    :return list:
    """
    template_choices = []
    if choices:
        # template_choices += [(None, _("--- General templates ---"))]
        # template_choices += (_("General templates"),
        #                      list(FORM_TEMPLATE_CHOICES))
        template_choices += list(choices)

    theme = get_theme(as_instance=True)
    theme_template_choices = []
    try:
        theme_template_choices = list(
            theme.custom_data[source][theme_specific_choices_key]
        )
        # template_choices += [(None, _("--- Theme templates ---"))]
        # template_choices += (_("Theme templates"), theme_template_choices)
        template_choices += theme_template_choices
    except KeyError:
        pass

    return template_choices
