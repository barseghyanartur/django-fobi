from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:
    INSTALLED_APPS.append('captcha')
    INSTALLED_APPS.append(
        'fobi.contrib.plugins.form_elements.security.recaptcha'
    )
except Exception as err:
    pass

# RECAPTCHA_PUBLIC_KEY = ''
# RECAPTCHA_PRIVATE_KEY = ''
RECAPTCHA_USE_SSL = True
# FOBI_DEFAULT_THEME = 'simple'
