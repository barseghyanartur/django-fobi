from nine.versions import DJANGO_GTE_1_7

from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:
    INSTALLED_APPS.append('override_simple_theme')
    INSTALLED_APPS.append('crispy_forms')
except Exception as err:
    pass

if DJANGO_GTE_1_7:
    try:
        INSTALLED_APPS.remove('south') if 'south' in INSTALLED_APPS else None
    except Exception as err:
        pass

FOBI_DEFAULT_THEME = 'simple'

CRISPY_TEMPLATE_PACK = 'uni_form'

# Make crispy-forms fail loud
CRISPY_FAIL_SILENTLY = not DEBUG
