from __future__ import print_function

__title__ = 'fobi.tests.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'PRINT_INFO', 'TRACK_TIME', 'print_info', 'fobi_setup', 'skip',
    'is_fobi_setup_completed', 'mark_fobi_setup_as_completed',
)

from optparse import OptionParser
from time import sleep
from copy import copy

from django.test import TestCase, LiveServerTestCase, Client, RequestFactory
from django.core.management import call_command
from django.contrib.staticfiles.management.commands import collectstatic
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from fobi.base import (
    form_element_plugin_registry, form_handler_plugin_registry,
    form_callback_registry, theme_registry, ensure_autodiscover,
    get_registered_form_element_plugins, get_registered_form_handler_plugins,
    get_registered_themes, get_registered_form_callbacks
    )
from fobi.models import FormEntry, FormElementEntry, FormHandlerEntry
from fobi.dynamic import assemble_form_class

from fobi.contrib.plugins.form_elements.content.content_text.fobi_form_elements \
    import ContentTextPlugin
from fobi.contrib.plugins.form_elements.content.content_image.fobi_form_elements \
    import ContentImagePlugin

from fobi.contrib.plugins.form_elements.fields.boolean.fobi_form_elements \
    import BooleanSelectPlugin
from fobi.contrib.plugins.form_elements.fields.email.fobi_form_elements \
    import EmailInputPlugin
from fobi.contrib.plugins.form_elements.fields.hidden.fobi_form_elements \
    import HiddenInputPlugin
from fobi.contrib.plugins.form_elements.fields.integer.fobi_form_elements \
    import IntegerInputPlugin
from fobi.contrib.plugins.form_elements.fields.text.fobi_form_elements \
    import TextInputPlugin
from fobi.contrib.plugins.form_elements.fields.textarea.fobi_form_elements \
    import TextareaPlugin

from fobi.contrib.plugins.form_handlers.db_store.fobi_form_handlers \
    import DBStoreHandlerPlugin
from fobi.contrib.plugins.form_handlers.mail.fobi_form_handlers \
    import MailHandlerPlugin

# ****************************************************************************
# **************** Safe User import for Django > 1.5, < 1.8 ******************
# ****************************************************************************
AUTH_USER_MODEL = settings.AUTH_USER_MODEL

# Note, that this may cause circular imports - thus the ``get_user_model``
# should be moved elsewhere (be used on the function/method level). For
# now leave commented and solve in future. Possible use the DjangoCMS solution
# https://github.com/divio/django-cms/blob/develop/cms/models/permissionmodels.py#L18

# Sanity checks.
#user = User()
#
#if not hasattr(user, 'username'):
#    from fobi.exceptions import ImproperlyConfigured
#    raise ImproperlyConfigured("Your custom user model ({0}.{1}) doesn't "
#                               "have ``username`` property, while "
#                               "``django-fobi`` relies on its' presence"
#                               ".".format(user._meta.app_label, user._meta.object_name))

# ****************************************************************************
# ****************************************************************************
# ****************************************************************************

PRINT_INFO = True
TRACK_TIME = False

def print_info(func):
    """
    Prints some useful info.
    """
    if not PRINT_INFO:
        return func

    def inner(self, *args, **kwargs):
        #if TRACK_TIME:
        #    import simple_timer
        #    timer = simple_timer.Timer() # Start timer

        result = func(self, *args, **kwargs)

        #if TRACK_TIME:
        #    timer.stop() # Stop timer

        print('\n{0}'.format(func.__name__))
        print('============================')
        if func.__doc__:
            print('""" {0} """'.format(func.__doc__.strip()))
        print('----------------------------')
        if result is not None:
            print(result)
        #if TRACK_TIME:
        #    print('done in {0} seconds'.format(timer.duration))
        print('\n')

        return result
    return inner

SKIP = False

def skip(func):
    """
    Simply skips the test.
    """
    def inner(self, *args, **kwargs):
        if SKIP:
            return
        return func(self, *args, **kwargs)
    return inner

class FobiSetup(object):
    """
    Basic setup class in order to avoid the fobi test data
    to be initialised multiple times.
    """
    def __init__(self):
        self.is_done = False

fobi_setup = FobiSetup()

def is_fobi_setup_completed():
    return fobi_setup.is_done == True

def mark_fobi_setup_as_completed():
    fobi_setup.is_done = True
