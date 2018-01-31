from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:
    INSTALLED_APPS.append('mptt')
    INSTALLED_APPS.append('bar')
    INSTALLED_APPS.append(
        'fobi.contrib.plugins.form_elements.fields.select_mptt_model_object'
    )
    INSTALLED_APPS.append(
        'fobi.contrib.plugins.form_elements.fields.select_multiple_mptt_model_objects'  # NOQA
    )
except Exception as err:
    pass
