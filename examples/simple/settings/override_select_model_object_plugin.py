from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:
    INSTALLED_APPS.append('override_select_model_object_plugin')
except Exception as err:
    pass
