from .conf import get_setting

__title__ = 'fobi.contrib.plugins.form_handlers.mail.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'AUTO_MAIL_BODY',
    'AUTO_MAIL_FROM',
    'AUTO_MAIL_SUBJECT',
    'AUTO_MAIL_TO',
    'MULTI_EMAIL_FIELD_VALUE_SPLITTER',
)

MULTI_EMAIL_FIELD_VALUE_SPLITTER = get_setting(
    'MULTI_EMAIL_FIELD_VALUE_SPLITTER'
)

AUTO_MAIL_TO = get_setting(
    'AUTO_MAIL_TO'
)

AUTO_MAIL_SUBJECT = get_setting(
    'AUTO_MAIL_SUBJECT'
)

AUTO_MAIL_BODY = get_setting(
    'AUTO_MAIL_BODY'
)

AUTO_MAIL_FROM = get_setting(
    'AUTO_MAIL_FROM'
)
