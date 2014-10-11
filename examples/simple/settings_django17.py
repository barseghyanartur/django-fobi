from settings import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:
    INSTALLED_APPS.remove('tinymce')
except Exception as e:
    pass
