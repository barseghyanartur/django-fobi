from .bootstrap3_theme_feincms import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:

    if 'captcha' not in INSTALLED_APPS:
        INSTALLED_APPS.append('captcha')

    if 'fobi.contrib.plugins.form_elements.security.captcha' \
            not in INSTALLED_APPS:
        INSTALLED_APPS.append(
            'fobi.contrib.plugins.form_elements.security.captcha'
        )

except Exception as err:
    pass
