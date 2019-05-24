__title__ = 'fobi.contrib.plugins.form_handlers.mail_sender.defaults'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'AUTO_MAIL_BODY',
    'AUTO_MAIL_FROM',
    'AUTO_MAIL_SUBJECT',
    'AUTO_MAIL_TO',
    'MULTI_EMAIL_FIELD_VALUE_SPLITTER',
)


MULTI_EMAIL_FIELD_VALUE_SPLITTER = ','  # But can be '\n'
AUTO_MAIL_TO = []
AUTO_MAIL_SUBJECT = 'Automatic email'
AUTO_MAIL_BODY = 'Automatic email'
AUTO_MAIL_FROM = ''
