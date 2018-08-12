import os
import signal
import subprocess

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.management import call_command

from fobi.models import FormEntry, FormElementEntry, FormHandlerEntry
from fobi.contrib.plugins.form_elements.content \
         .content_text.fobi_form_elements import ContentTextPlugin
from fobi.contrib.plugins.form_elements.content \
         .content_image.fobi_form_elements import ContentImagePlugin

from fobi.contrib.plugins.form_elements.fields \
         .boolean.fobi_form_elements import BooleanSelectPlugin
from fobi.contrib.plugins.form_elements.fields \
         .email.fobi_form_elements import EmailInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .hidden.fobi_form_elements import HiddenInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .integer.fobi_form_elements import IntegerInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .text.fobi_form_elements import TextInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .textarea.fobi_form_elements import TextareaPlugin

from fobi.contrib.plugins.form_handlers \
         .db_store.fobi_form_handlers import DBStoreHandlerPlugin
from fobi.contrib.plugins.form_handlers \
         .mail.fobi_form_handlers import MailHandlerPlugin

from .core import (
    is_app_setup_completed,
    mark_app_setup_as_completed,
)
from .constants import (
    FOBI_TEST_USER_USERNAME,
    FOBI_TEST_USER_PASSWORD,
    TEST_FORM_NAME,
    TEST_FORM_SLUG,
)

__title__ = 'fobi.tests.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'create_form_with_entries',
    'db_clean_up',
    'get_or_create_admin_user',
    'get_or_create_admin_user',
    'phantom_js_clean_up',
    'setup_app',
)

# ****************************************************************************
# **************** Safe User import for Django > 1.5, < 1.8 ******************
# ****************************************************************************
AUTH_USER_MODEL = settings.AUTH_USER_MODEL

# ****************************************************************************
# ****************************************************************************
# ****************************************************************************


def get_or_create_admin_user():
    """Create a user for testing the fobi.

    TODO: At the moment an admin account is being tested. Automated tests
    with diverse accounts are to be implemented.
    """
    User = get_user_model()
    try:
        kwargs = {
            User.USERNAME_FIELD: FOBI_TEST_USER_USERNAME,
        }
        u = User._default_manager.get(**kwargs)
        return u
    except ObjectDoesNotExist as e:

        u = User()
        setattr(u, User.USERNAME_FIELD, FOBI_TEST_USER_USERNAME)
        u.email = 'admin@dev.django-fobi.example.com'
        u.is_superuser = True
        u.is_staff = True
        u.set_password(FOBI_TEST_USER_PASSWORD)

        try:
            u.save()
            return u
        except Exception as err:
            pass


def setup_app(collectstatic=False, fobi_sync_plugins=False):
    """Set up fobi."""
    if is_app_setup_completed():
        return False

    if collectstatic:
        call_command('collectstatic', verbosity=3, interactive=False)
    if fobi_sync_plugins:
        call_command('fobi_sync_plugins', verbosity=3, interactive=False)
    # call_command('loaddata', 'dash', verbosity=3, interactive=False)

    mark_app_setup_as_completed()


def create_form_with_entries(user=None,
                             create_entries_if_form_exist=True,
                             data={},
                             is_public=False,
                             name=TEST_FORM_NAME,
                             slug=TEST_FORM_SLUG):
    """Create test form with entries.

    Fills the form with pre-defined plugins.

    :param django.contrib.auth.models.User user:
    :param bool create_entries_if_form_exist: If set to True, entries
        are being created even if form already exists (a database
        record).
    :param dict data:
    :param bool is_public:
    :param str name:
    :param str slug:
    :return fobi.models.FormEntry: Instance of ``fobi.models.FormEntry``
        with a number of form elements and handlers filled in.
    """
    if not user:
        user = get_or_create_admin_user()

    try:
        form_entry = FormEntry._default_manager.get(slug=slug)
        if not create_entries_if_form_exist:
            return None
    except Exception as err:
        form_entry = FormEntry(
            name=name,
            slug=slug,
            user=user,
            is_public=is_public,
        )
        form_entry.save()

    # ************************************************************************
    # ******************************** Form elements *************************
    # ************************************************************************
    position = 1
    for key, entry_data in data.items():
        form_element_entry = FormElementEntry(
            form_entry=form_entry,
            plugin_uid=entry_data[0],
            plugin_data=entry_data[1],
            position=position
        )
        form_element_entry.save()
        position += 1

    # ************************************************************************
    # ******************************** Form handlers *************************
    # ************************************************************************

    # DB save
    form_handler_entry = FormHandlerEntry(
        form_entry=form_entry,
        plugin_uid=DBStoreHandlerPlugin.uid,
        plugin_data=''
    )
    form_handler_entry.save()

    # Mail
    form_handler_entry = FormHandlerEntry(
        form_entry=form_entry,
        plugin_uid=MailHandlerPlugin.uid,
        plugin_data='{'
                    '"from_name": "Fobi administration", '
                    '"from_email": "noreply@fobi.mail.example.com", '
                    '"to_name": "Artur Barseghyan", '
                    '"to_email": "artur.barseghyan@gmail.com", '
                    '"subject": "Test mail", "body": "Test body"'
                    '}'
    )
    form_handler_entry.save()

    return form_entry


def db_clean_up(clean_form=False, clean_elements=True, clean_handlers=True):
    """Clean up the database.

    Clean up the database by removing all form element and form handler
    entries.
    """
    if clean_form:
        FormEntry._default_manager.all().delete()
    if clean_elements:
        FormElementEntry._default_manager.all().delete()
    if clean_handlers:
        FormHandlerEntry._default_manager.all().delete()


def phantom_js_clean_up():
    """Clean up Phantom JS.

    Kills all phantomjs instances, disregard of their origin.
    """
    processes = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = processes.communicate()

    for line in out.splitlines():
        if 'phantomjs' in line:
            pid = int(line.split(None, 1)[0])
            os.kill(pid, signal.SIGKILL)
