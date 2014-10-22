from settings import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:
    INSTALLED_APPS.append('captcha')
    INSTALLED_APPS.append('fobi.contrib.plugins.form_elements.fields.captcha')
except Exception as e:
    pass

#FOBI_DEFAULT_THEME = 'simple'
