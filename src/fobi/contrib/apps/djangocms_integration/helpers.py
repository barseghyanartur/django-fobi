from fobi.integration.helpers import get_template_choices

from .settings import FORM_TEMPLATE_CHOICES, SUCCESS_PAGE_TEMPLATE_CHOICES

__title__ = 'fobi.contrib.apps.djangocms_integration.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'get_form_template_choices',
    'get_success_page_template_choices',
)


def get_form_template_choices():
    """Get the form template choices.

    It's possible to provide theme templates per theme or just per project.

    :return list:
    """
    return get_template_choices(
        'djangocms_integration',
        FORM_TEMPLATE_CHOICES,
        'form_template_choices'
    )


def get_success_page_template_choices():
    """Get success page template choices.

    :return list:
    """
    return get_template_choices(
        'djangocms_integration',
        SUCCESS_PAGE_TEMPLATE_CHOICES,
        'success_page_template_choices'
    )
