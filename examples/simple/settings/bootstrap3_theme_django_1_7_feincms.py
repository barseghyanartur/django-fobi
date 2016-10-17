from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:
    INSTALLED_APPS.remove('south') if 'south' in INSTALLED_APPS else None
    #INSTALLED_APPS.remove('tinymce') if 'tinymce' in INSTALLED_APPS else None
    INSTALLED_APPS.remove('admin_tools.dashboard') if 'admin_tools.dashboard' in INSTALLED_APPS else None

    INSTALLED_APPS += [
        'feincms', # FeinCMS

        'fobi.contrib.apps.feincms_integration', # Fobi FeinCMS app

        'page', # Example
    ]
except Exception as e:
    pass


FEINCMS_RICHTEXT_INIT_CONTEXT = {
    'TINYMCE_JS_URL': STATIC_URL + 'tiny_mce/tiny_mce.js',
}
