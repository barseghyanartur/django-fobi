from settings import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:
    INSTALLED_APPS.append('override_simple_theme')
except Exception as e:
    pass

FOBI_DEFAULT_THEME = 'simple'
