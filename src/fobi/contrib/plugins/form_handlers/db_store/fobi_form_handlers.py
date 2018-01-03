from .....base import (
    form_handler_plugin_registry,
    form_wizard_handler_plugin_registry,
)
from .base import DBStoreHandlerPlugin, DBStoreWizardHandlerPlugin

__title__ = 'fobi.contrib.plugins.form_handlers.db_store.fobi_form_handlers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'DBStoreHandlerPlugin',
    'DBStoreWizardHandlerPlugin',
)


form_handler_plugin_registry.register(DBStoreHandlerPlugin)
form_wizard_handler_plugin_registry.register(DBStoreWizardHandlerPlugin)
