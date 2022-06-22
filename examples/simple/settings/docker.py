from chromedriver_py import binary_path
from selenium import webdriver
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
DEBUG_TEMPLATE = True
# TEMPLATE_DEBUG = True
DEV = True

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

INTERNAL_IPS = ('127.0.0.1',)
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = PROJECT_DIR('../../tmp')

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

CHROME_DRIVER_OPTIONS = webdriver.ChromeOptions()
CHROME_DRIVER_OPTIONS.add_argument('-headless')
CHROME_DRIVER_OPTIONS.add_argument('-no-sandbox')
CHROME_DRIVER_OPTIONS.set_capability('chrome.binary', "/usr/bin/google-chrome")

# CHROME_DRIVER_OPTIONS.add_argument('-single-process')

CHROME_DRIVER_EXECUTABLE_PATH = binary_path  # '/usr/bin/chromedriver'
FIREFOX_BIN_PATH = '/usr/lib/firefox/firefox'
PHANTOM_JS_EXECUTABLE_PATH = ''
