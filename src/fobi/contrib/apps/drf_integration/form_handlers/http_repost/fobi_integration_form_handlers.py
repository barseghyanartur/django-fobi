from ......base import integration_form_handler_plugin_registry
from .base import HTTPRepostHandlerPlugin

__title__ = 'fobi.contrib.apps.drf_integration.' \
            'fobi_integration_form_handlers.http_repost.fobi_form_handlers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'HTTPRepostHandlerPlugin',
)


integration_form_handler_plugin_registry.register(HTTPRepostHandlerPlugin)
