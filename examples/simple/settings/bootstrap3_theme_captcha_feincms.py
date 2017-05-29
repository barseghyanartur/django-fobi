from .bootstrap3_theme_feincms import *

try:

    INSTALLED_APPS += [
        'captcha',
        'fobi.contrib.plugins.form_elements.security.captcha',
    ]
except Exception as err:
    pass
