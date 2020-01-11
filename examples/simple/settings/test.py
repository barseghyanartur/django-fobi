# Use in `tox`.
from django_nine import versions

from .base import *

TESTING = True

INSTALLED_APPS = list(INSTALLED_APPS)

LOGGING = {}

DEBUG_TOOLBAR = False

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fobi',
        'USER': 'postgres',
        'PASSWORD': 'test',

        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': PROJECT_DIR('../../db/example.db'),
        # 'USER': '',
        # 'PASSWORD': '',

        # Empty for localhost through domain sockets or '127.0.0.1' for
        # localhost through TCP.
        'HOST': '',
        # Set to empty string for default.
        'PORT': '',
        'TEST': {
            'NAME': 'fobi_tests',
            'USER': 'postgres',
            'PASSWORD': '',  # For travis
        }
    }
}

# Conditionally choosing the right postgres engine
if versions.DJANGO_GTE_1_11:
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql'
else:
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'

# FeinCMS addons

INSTALLED_APPS += [
    'feincms',  # FeinCMS

    'fobi.contrib.apps.feincms_integration',  # Fobi FeinCMS app

    'page',  # Example
]

MIGRATION_MODULES = {
    'fobi': 'fobi.migrations',
    'db_store': 'fobi.contrib.plugins.form_handlers.db_store.migrations',
    'page': 'page.migrations',
}

try:
    from .local_settings import TEST_DATABASES as DATABASES
except:
    pass
