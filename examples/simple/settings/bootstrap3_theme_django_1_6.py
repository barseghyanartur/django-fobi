from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:
    INSTALLED_APPS.append('south') if 'south' not in INSTALLED_APPS else None
    # INSTALLED_APPS.remove('tinymce') if 'tinymce' in INSTALLED_APPS else None
except Exception as e:
    pass
