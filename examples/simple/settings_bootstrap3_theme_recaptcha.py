from settings import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:
    INSTALLED_APPS.append('captcha')
    INSTALLED_APPS.append('fobi.contrib.plugins.form_elements.security.recaptcha')
except Exception as e:
    pass

RECAPTCHA_PUBLIC_KEY = '6LftLP8SAAAAANaQb7bW8DZAkL2yFGGIJeEYtr3b'
RECAPTCHA_PRIVATE_KEY = '6LftLP8SAAAAAFlc5NOLkLFCyDu79kwpKGsPLfJ8'
RECAPTCHA_USE_SSL = True
#FOBI_DEFAULT_THEME = 'simple'
