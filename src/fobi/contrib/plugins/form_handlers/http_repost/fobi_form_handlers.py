from .....base import (
    form_handler_plugin_registry,
    form_wizard_handler_plugin_registry
)
from .base import HTTPRepostHandlerPlugin, HTTPRepostWizardHandlerPlugin

__title__ = 'fobi.contrib.plugins.form_handlers.http_repost.fobi_form_handlers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'HTTPRepostHandlerPlugin',
    'HTTPRepostWizardHandlerPlugin',
)


form_handler_plugin_registry.register(HTTPRepostHandlerPlugin)
form_wizard_handler_plugin_registry.register(HTTPRepostWizardHandlerPlugin)
