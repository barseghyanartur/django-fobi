from ......base import integration_form_handler_plugin_registry
from .base import MailHandlerPlugin

__title__ = 'fobi.contrib.apps.drf_integration.' \
            'fobi_integration_form_handlers.mail.fobi_form_handlers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'MailHandlerPlugin',
)


integration_form_handler_plugin_registry.register(MailHandlerPlugin)
