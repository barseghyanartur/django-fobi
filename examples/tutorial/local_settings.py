import os
PROJECT_DIR = lambda base : os.path.abspath(os.path.join(os.path.dirname(__file__), base).replace('\\','/'))

DEBUG = True
DEBUG_TOOLBAR = not True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': PROJECT_DIR('../db/example.db'), # Or path to database file if using sqlite3.

        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}

INTERNAL_IPS = ('127.0.0.1',)

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = PROJECT_DIR('../tmp')

DEFAULT_FROM_EMAIL = '<no-reply@dev.django-fobi.mail.example.com>'

FOBI_DEBUG = True
FOBI_RESTRICT_PLUGIN_ACCESS = False
FOBI_RESTRICT_FIELDS_ACCESS = False
#FOBI_DEFAULT_THEME = 'foundation5'

WAIT_BETWEEN_TEST_STEPS = 0
FOBI_WAIT_AT_TEST_END = 0
