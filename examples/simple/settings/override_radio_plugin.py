from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:
    INSTALLED_APPS.append("override_radio_plugin")
except Exception as err:
    pass
