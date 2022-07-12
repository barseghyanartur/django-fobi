"""
Used in `tox` on GitHub CI.
"""
from chromedriver_py import binary_path

from .base import *

TESTING = True

INSTALLED_APPS = list(INSTALLED_APPS)

LOGGING = {}

DEBUG_TOOLBAR = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "fobi",
        "USER": "postgres",
        "PASSWORD": "test",
        # Empty for localhost through domain sockets or '127.0.0.1' for
        # localhost through TCP.
        "HOST": "localhost",
        "TEST": {
            "HOST": "localhost",
            "NAME": "fobi_tests",
            "USER": "postgres",
            "PASSWORD": "test",
        },
    }
}

# FeinCMS addons

INSTALLED_APPS += [
    "feincms",  # FeinCMS
    "fobi.contrib.apps.feincms_integration",  # Fobi FeinCMS app
    "page",  # Example
]

MIGRATION_MODULES = {
    "fobi": "fobi.migrations",
    "db_store": "fobi.contrib.plugins.form_handlers.db_store.migrations",
    "page": "page.migrations",
}

CHROME_DRIVER_EXECUTABLE_PATH = binary_path  # '/usr/bin/chromedriver'
CHROME_DRIVER_OPTIONS = webdriver.ChromeOptions()
CHROME_DRIVER_OPTIONS.add_argument("-headless")
CHROME_DRIVER_OPTIONS.add_argument("-no-sandbox")
CHROME_DRIVER_OPTIONS.set_capability("chrome.binary", "/usr/bin/google-chrome")

try:
    from .local_settings import TEST_DATABASES as DATABASES
except:
    pass
