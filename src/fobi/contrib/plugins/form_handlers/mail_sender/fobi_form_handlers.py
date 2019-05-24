from .....base import (
    form_handler_plugin_registry,
    form_wizard_handler_plugin_registry,
)
from .base import MailSenderHandlerPlugin, MailSenderWizardHandlerPlugin

__title__ = 'fobi.contrib.plugins.form_handlers.mail_sender.fobi_form_handlers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'MailSenderHandlerPlugin',
    'MailSenderWizardHandlerPlugin',
)


form_handler_plugin_registry.register(MailSenderHandlerPlugin)
form_wizard_handler_plugin_registry.register(MailSenderWizardHandlerPlugin)
