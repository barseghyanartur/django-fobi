__title__ = 'fobi.contrib.apps.mezzanine_integration.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('get_form_template_choices', 'get_success_page_template_choices',)

from fobi.integration.helpers import get_template_choices

from .settings import FORM_TEMPLATE_CHOICES, SUCCESS_PAGE_TEMPLATE_CHOICES

def get_form_template_choices():
    """
    Gets the form template choices. It's possible to provide theme templates
    per theme or just per project.

    :return list:
    """
    return get_template_choices(
        'mezzanine_integration',
        FORM_TEMPLATE_CHOICES,
        'form_template_choices'
        )

def get_success_page_template_choices():
    """
    :return list:
    """
    return get_template_choices(
        'mezzanine_integration',
        SUCCESS_PAGE_TEMPLATE_CHOICES,
        'success_page_template_choices'
        )
