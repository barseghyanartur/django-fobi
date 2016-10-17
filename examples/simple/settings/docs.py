from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)

if 'foo' in INSTALLED_APPS:
    INSTALLED_APPS.remove('foo')

LOGGING = {}
