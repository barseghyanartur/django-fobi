__title__ = 'fobi.contrib.apps.mezzanine_integration.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('get_form_template_choices', 'get_success_page_template_choices',)

from django.utils.translation import ugettext_lazy as _

from fobi.base import get_theme
from fobi.contrib.apps.mezzanine_integration.settings import (
    FORM_TEMPLATE_CHOICES, SUCCESS_PAGE_TEMPLATE_CHOICES
)

def get_template_choices(choices, theme_specific_choices_key):
    """
    Gets the template choices. It's possible to provide theme templates
    per theme or just per project.

    :param tuple or list choices:
    :param str theme_specific_choices_key:
    :return list:
    """
    template_choices = []
    if choices:
        #template_choices += [(None, _("--- General templates ---"))]
        #template_choices += (_("General templates"), list(FORM_TEMPLATE_CHOICES))
        template_choices += list(choices)

    theme = get_theme(as_instance=True)
    theme_template_choices = []
    try:
        theme_template_choices = list(
            theme.custom_data['mezzanine_integration'][theme_specific_choices_key]
            )
        #template_choices += [(None, _("--- Theme templates ---"))]
        #template_choices += (_("Theme templates"), theme_template_choices)
        template_choices += theme_template_choices
    except KeyError:
        pass

    return template_choices

def get_form_template_choices():
    """
    Gets the form template choices. It's possible to provide theme templates
    per theme or just per project.

    :return list:
    """
    return get_template_choices(FORM_TEMPLATE_CHOICES, 'form_template_choices')

def get_success_page_template_choices():
    """
    :return list:
    """
    return get_template_choices(
        SUCCESS_PAGE_TEMPLATE_CHOICES,
        'success_page_template_choices'
        )
