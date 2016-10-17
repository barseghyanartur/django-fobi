from .base import *

# Using custom user model
AUTH_USER_MODEL = 'customauth.MyUser'

INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS.append('customauth')
