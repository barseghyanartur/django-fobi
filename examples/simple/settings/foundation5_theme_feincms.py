from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS += [
    'feincms',  # FeinCMS

    'fobi.contrib.apps.feincms_integration',  # Fobi FeinCMS app

    'page',  # Example
]

FEINCMS_RICHTEXT_INIT_CONTEXT = {
    'TINYMCE_JS_URL': STATIC_URL + 'tiny_mce/tiny_mce.js',
}

FOBI_DEFAULT_THEME = 'foundation5'
