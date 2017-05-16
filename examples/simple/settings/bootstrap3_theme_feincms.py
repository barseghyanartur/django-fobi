from nine.versions import DJANGO_GTE_1_8
from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS += [
    'feincms',  # FeinCMS

    'fobi.contrib.apps.feincms_integration',  # Fobi FeinCMS app

    'page',  # Example

    'tinymce',  # TinyMCE
]

try:
    INSTALLED_APPS.remove('admin_tools.dashboard') \
        if 'admin_tools.dashboard' in INSTALLED_APPS else None
except Exception as err:
    pass

FEINCMS_RICHTEXT_INIT_CONTEXT = {
    'TINYMCE_JS_URL': STATIC_URL + 'tiny_mce/tiny_mce.js',
}

if DJANGO_GTE_1_8:

    MIGRATION_MODULES = {
        'fobi': 'fobi.migrations',
        'db_store': 'fobi.contrib.plugins.form_handlers.db_store.migrations',
    }
