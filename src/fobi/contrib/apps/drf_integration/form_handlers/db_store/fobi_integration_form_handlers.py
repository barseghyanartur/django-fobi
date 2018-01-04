from ......base import integration_form_handler_plugin_registry
from .base import DBStoreHandlerPlugin

__title__ = 'fobi.contrib.apps.drf_integration.' \
            'fobi_integration_form_handlers.db_store.fobi_form_handlers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'DBStoreHandlerPlugin',
)


integration_form_handler_plugin_registry.register(DBStoreHandlerPlugin)
