from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:
    if 'captcha' not in INSTALLED_APPS:
        INSTALLED_APPS.append('captcha')

    if 'fobi.contrib.plugins.form_elements.security.captcha' \
            not in INSTALLED_APPS:
        INSTALLED_APPS.append(
            'fobi.contrib.plugins.form_elements.security.captcha'
        )

    CAPTCHA_TEXT_FIELD_TEMPLATE = 'bootstrap3/captcha/text_field.html'

    ENABLE_CAPTCHA = True

except Exception as e:
    pass

# FOBI_DEFAULT_THEME = 'simple'
