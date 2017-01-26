from .conf import get_setting

__title__ = 'fobi.contrib.plugins.form_handlers.mail.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'MULTI_EMAIL_FIELD_VALUE_SPLITTER',
)

MULTI_EMAIL_FIELD_VALUE_SPLITTER = get_setting(
    'MULTI_EMAIL_FIELD_VALUE_SPLITTER'
)
