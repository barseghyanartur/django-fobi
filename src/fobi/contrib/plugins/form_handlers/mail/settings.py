__title__ = 'fobi.contrib.plugins.form_handlers.mail.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'MULTI_EMAIL_FIELD_VALUE_SPLITTER',
)

from .conf import get_setting

MULTI_EMAIL_FIELD_VALUE_SPLITTER = get_setting(
    'MULTI_EMAIL_FIELD_VALUE_SPLITTER'
    )
