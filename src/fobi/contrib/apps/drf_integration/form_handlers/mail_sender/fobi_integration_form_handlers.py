from ......base import integration_form_handler_plugin_registry
from .base import MailSenderHandlerPlugin

__title__ = 'fobi.contrib.apps.drf_integration.' \
            'fobi_integration_form_handlers.mail_sender.fobi_form_handlers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'MailSenderHandlerPlugin',
)


integration_form_handler_plugin_registry.register(MailSenderHandlerPlugin)
