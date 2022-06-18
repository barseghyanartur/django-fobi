import os

from django_nine.versions import *
from .bootstrap3_theme import *


def project_dir(base):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), base).replace('\\', '/')
    )


def gettext(s):
    return s


PROJECT_DIR = project_dir
DEBUG = True
DEBUG_TOOLBAR = False
# TEMPLATE_DEBUG = True
DEV = True

# DATABASES = {
#     'default': {
#         # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         # 'ENGINE': 'django.db.backends.sqlite3',
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         # Or path to database file if using sqlite3.
#         'NAME': PROJECT_DIR('../../db/example.db'),
#         # 'ENGINE': 'django.db.backends.mysql',
#         # 'NAME': 'fobi',
#         # 'TEST_NAME': 'fobi_test',
#         # The following settings are not used with sqlite3:
#         # 'USER': 'root',
#         'USER': 'postgres',
#         'PASSWORD': 'test',
#         # Empty for localhost through domain sockets or '127.0.0.1' for
#         # localhost through TCP.
#         'HOST': '',
#         # Set to empty string for default.
#         'PORT': '',
#     }
# }

# TEST_DATABASES = {
#     'default': {
#         # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'fobi',
#         'USER': 'postgres',
#         'PASSWORD': 'test',
#
#         # 'ENGINE': 'django.db.backends.sqlite3',
#         # 'NAME': PROJECT_DIR('../../db/example.db'),
#         # 'USER': '',
#         # 'PASSWORD': '',
#
#         # Empty for localhost through domain sockets or '127.0.0.1' for
#         # localhost through TCP.
#         'HOST': '',
#         # Set to empty string for default.
#         'PORT': '',
#     }
# }

POSTGRES_ENGINE = 'django.db.backends.postgresql'

DATABASES = {
    'default': {
        'ENGINE': POSTGRES_ENGINE,
        'HOST': 'postgresql',
        'NAME': 'fobi',
        'USER': 'postgres',
        'PASSWORD': 'test',
    }
}

TEST_DATABASES = {
    'default': {
        'ENGINE': POSTGRES_ENGINE,
        'HOST': 'postgresql',
        'NAME': 'fobi',
        'USER': 'postgres',
        'PASSWORD': 'test',
    }
}

INTERNAL_IPS = ('127.0.0.1',)
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = PROJECT_DIR('../../tmp')

DEFAULT_FROM_EMAIL = '<no-reply@dev.django-fobi.mail.example.com>'

FOBI_DEBUG = True
FOBI_RESTRICT_PLUGIN_ACCESS = False
FOBI_RESTRICT_FIELDS_ACCESS = False
FOBI_FORM_ELEMENT_SELECT_MODEL_OBJECT_IGNORED_MODELS = ['auth.User']
FOBI_FAIL_ON_MISSING_FORM_ELEMENT_PLUGINS = True
# FOBI_FAIL_ON_MISSING_FORM_HANDLER_PLUGINS = False
FOBI_FAIL_ON_ERRORS_IN_FORM_HANDLER_PLUGINS = True
# FOBI_DEFAULT_THEME = 'foundation5'


FOBI_FAIL_ON_MISSING_FORM_HANDLER_PLUGINS = True
FOBI_FAIL_ON_MISSING_FORM_WIZARD_HANDLER_PLUGINS = True
FOBI_FAIL_ON_ERRORS_IN_FORM_ELEMENT_PLUGINS = False
# FOBI_FAIL_ON_ERRORS_IN_FORM_HANDLER_PLUGINS = True
FOBI_FAIL_ON_ERRORS_IN_FORM_WIZARD_HANDLER_PLUGINS = True

# WAIT_BETWEEN_TEST_STEPS = 0
# FOBI_WAIT_AT_TEST_END = False
ENABLE_CAPTCHA = True

# LANGUAGE_CODE = 'nl'

# from fobi.constants import (
#    SUBMIT_VALUE_AS_VAL, SUBMIT_VALUE_AS_REPR, SUBMIT_VALUE_AS_MIX
#    )
# SUBMIT_VALUE_AS = SUBMIT_VALUE_AS_MIX
#
# FOBI_FORM_ELEMENT_RADIO_SUBMIT_VALUE_AS = SUBMIT_VALUE_AS  #'val'
# FOBI_FORM_ELEMENT_SELECT_SUBMIT_VALUE_AS = SUBMIT_VALUE_AS  #'val'
# FOBI_FORM_ELEMENT_SELECT_MULTIPLE_SUBMIT_VALUE_AS = SUBMIT_VALUE_AS  #'val'
# 'val'
# FOBI_FORM_ELEMENT_SELECT_MODEL_OBJECT_SUBMIT_VALUE_AS = SUBMIT_VALUE_AS
# FOBI_FORM_ELEMENT_SELECT_MULTIPLE_MODEL_OBJECTS_SUBMIT_VALUE_AS = \
#     SUBMIT_VALUE_AS

from selenium import webdriver
CHROME_DRIVER_OPTIONS = webdriver.ChromeOptions()
CHROME_DRIVER_OPTIONS.add_argument('-headless')
CHROME_DRIVER_OPTIONS.add_argument('-no-sandbox')
CHROME_DRIVER_OPTIONS.set_capability('chrome.binary', "/usr/bin/google-chrome")

# CHROME_DRIVER_OPTIONS.add_argument('-single-process')

from chromedriver_py import binary_path
CHROME_DRIVER_EXECUTABLE_PATH = binary_path  # '/usr/bin/chromedriver'
# CHROME_DRIVER_EXECUTABLE_PATH = None
FIREFOX_BIN_PATH = '/usr/lib/firefox/firefox'
FIREFOX_BIN_PATH = None
PHANTOM_JS_EXECUTABLE_PATH = ''
# PHANTOM_JS_EXECUTABLE_PATH = None

os.environ.setdefault(
    'FOBI_SOURCE_PATH',
    '/home/delusionalinsanity/bbrepos/django-fobi/src'
)

DEBUG_TEMPLATE = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'your-db-name',
#     }
# }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['all_log'],
    },
    'formatters': {
        'verbose': {
            'format': '\n%(levelname)s %(asctime)s [%(pathname)s:%(lineno)s] '
                      '%(message)s'
        },
        'simple': {
            'format': '\n%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'all_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR("../../logs/all.log"),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
        'django_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR("../../logs/django.log"),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
        'django_request_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR("../../logs/django_request.log"),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
        'fobi_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR("../../logs/fobi.log"),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['django_request_log'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['django_log'],
            'level': 'ERROR',
            'propagate': False,
        },
        'fobi': {
            'handlers': ['console', 'fobi_log'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
