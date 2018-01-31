from nine.versions import DJANGO_GTE_1_7

from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:
    INSTALLED_APPS.append('override_radio_plugin')
except Exception as err:
    pass

if DJANGO_GTE_1_7:
    try:
        INSTALLED_APPS.remove('south') if 'south' in INSTALLED_APPS else None
    except Exception as err:
        pass
