__title__ = 'fobi.discover'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('autodiscover',)

import imp
import logging

from django.conf import settings
from fobi.conf import get_setting

logger = logging.getLogger(__file__)

def autodiscover():
    """
    Autodiscovers files that should be found by fobi.
    """
    FORM_ELEMENT_PLUGINS_MODULE_NAME = get_setting('FORM_ELEMENT_PLUGINS_MODULE_NAME')
    FORM_HANDLER_PLUGINS_MODULE_NAME = get_setting('FORM_HANDLER_PLUGINS_MODULE_NAME')
    FORM_IMPORTER_PLUGINS_MODULE_NAME = get_setting('FORM_IMPORTER_PLUGINS_MODULE_NAME')
    THEMES_MODULE_NAME = get_setting('THEMES_MODULE_NAME')
    FORM_CALLBACKS_MODULE_NAME = get_setting('FORM_CALLBACKS_MODULE_NAME')

    def do_discover(module_name):
        for app in settings.INSTALLED_APPS:
            try:
                app = str(app)
                app_path = __import__(app, {}, {}, [app.split('.')[-1]]).__path__
            except (AttributeError, TypeError) as e:
                logger.debug(str(e))
                #import ipdb; ipdb.set_trace()
                continue

            try:
                imp.find_module(module_name, app_path)
            except ImportError as e:
                logger.debug(str(e))
                continue
            __import__('{0}.{1}'.format(app, module_name))

    # Discover plugins
    do_discover(FORM_ELEMENT_PLUGINS_MODULE_NAME)
    do_discover(FORM_HANDLER_PLUGINS_MODULE_NAME)
    do_discover(THEMES_MODULE_NAME)
    do_discover(FORM_CALLBACKS_MODULE_NAME)

    # Do not yet discover form importers
    #do_discover(FORM_IMPORTER_PLUGINS_MODULE_NAME)
