from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:
    INSTALLED_APPS.append('foreign_key_to_saved_form_data_entry')
except Exception as e:
    pass
