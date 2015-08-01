"""
- `WIDGET_FORM_SENT_GET_PARAM` (str): Name of the GET param indicating that 
  form has been successfully sent.
"""
__title__ = 'fobi.contrib.apps.mezzanine_integration.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'WIDGET_FORM_SENT_GET_PARAM', 'FORM_TEMPLATE_CHOICES',
    'SUCCESS_PAGE_TEMPLATE_CHOICES',
)

from .conf import get_setting

# **************************************************************
# **************************************************************
# *************************** Core *****************************
# **************************************************************
# **************************************************************

WIDGET_FORM_SENT_GET_PARAM = get_setting('WIDGET_FORM_SENT_GET_PARAM')
FORM_TEMPLATE_CHOICES = get_setting('FORM_TEMPLATE_CHOICES')
SUCCESS_PAGE_TEMPLATE_CHOICES = get_setting('SUCCESS_PAGE_TEMPLATE_CHOICES')
