# Use in `tox`.
from nine import versions

from .base import *

TESTING = True

INSTALLED_APPS = list(INSTALLED_APPS)

if versions.DJANGO_1_8:

    try:
        INSTALLED_APPS.remove('tinymce') \
            if 'tinymce' in INSTALLED_APPS \
            else None
    except Exception as err:
        pass

    try:
        INSTALLED_APPS.remove('admin_tools') \
            if 'admin_tools' in INSTALLED_APPS else None
        INSTALLED_APPS.remove('admin_tools.menu') \
            if 'admin_tools.menu' in INSTALLED_APPS else None
        INSTALLED_APPS.remove('admin_tools.dashboard') \
            if 'admin_tools.dashboard' in INSTALLED_APPS else None
    except Exception as err:
        pass

elif versions.DJANGO_1_9:

    try:
        INSTALLED_APPS.remove('tinymce') \
            if 'tinymce' in INSTALLED_APPS \
            else None
    except Exception as err:
        pass

    try:
        INSTALLED_APPS.remove('admin_tools') \
            if 'admin_tools' in INSTALLED_APPS else None
        INSTALLED_APPS.remove('admin_tools.menu') \
            if 'admin_tools.menu' in INSTALLED_APPS else None
        INSTALLED_APPS.remove('admin_tools.dashboard') \
            if 'admin_tools.dashboard' in INSTALLED_APPS else None
    except Exception as err:
        pass

elif versions.DJANGO_1_10:

    try:
        INSTALLED_APPS.remove('tinymce') \
            if 'tinymce' in INSTALLED_APPS \
            else None
    except Exception as err:
        pass

    try:
        INSTALLED_APPS.remove('admin_tools') \
            if 'admin_tools' in INSTALLED_APPS else None
        INSTALLED_APPS.remove('admin_tools.menu') \
            if 'admin_tools.menu' in INSTALLED_APPS else None
        INSTALLED_APPS.remove('admin_tools.dashboard') \
            if 'admin_tools.dashboard' in INSTALLED_APPS else None
    except Exception as err:
        pass

LOGGING = {}

DEBUG_TOOLBAR = False

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': PROJECT_DIR('../../db/example.db'),
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        # Empty for localhost through domain sockets or '127.0.0.1' for
        # localhost through TCP.
        'HOST': '',
        # Set to empty string for default.
        'PORT': '',
    }
}


# FeinCMS addons

INSTALLED_APPS += [
    'feincms',  # FeinCMS

    'fobi.contrib.apps.feincms_integration',  # Fobi FeinCMS app

    'page',  # Example

    'tinymce',  # TinyMCE
]
