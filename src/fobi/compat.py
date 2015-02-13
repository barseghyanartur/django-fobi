__title__ = 'fobi.compat'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('AUTH_USER_MODEL', 'User',)

from distutils.version import LooseVersion
import importlib

import django
from django.conf import settings

DJANGO_1_4 = LooseVersion('1.4') <= LooseVersion(django.get_version()) \
                                 < LooseVersion('1.5')
DJANGO_1_5 = LooseVersion('1.5') <= LooseVersion(django.get_version()) \
                                 < LooseVersion('1.6')
DJANGO_1_6 = LooseVersion('1.6') <= LooseVersion(django.get_version()) \
                                 < LooseVersion('1.7')
DJANGO_1_7 = LooseVersion('1.7') <= LooseVersion(django.get_version()) \
                                 < LooseVersion('1.8')
DJANGO_1_8 = LooseVersion('1.8') <= LooseVersion(django.get_version()) \
                                 < LooseVersion('1.9')
DJANGO_1_9 = LooseVersion('1.9') <= LooseVersion(django.get_version()) \
                                 < LooseVersion('2.0')
DJANGO_2_0 = LooseVersion('2.0') <= LooseVersion(django.get_version()) \
                                 < LooseVersion('2.1')

# Cannot use contrib.auth.get_user_model() at compile time.
user_app_name, user_model_name = settings.AUTH_USER_MODEL.rsplit('.', 1)
User = None
if DJANGO_1_6:
    for app in settings.INSTALLED_APPS:
        if app.endswith(user_app_name):
            user_app_models = importlib.import_module(app + ".models")
            User = getattr(user_app_models, user_model_name)
            break
elif DJANGO_1_7 or DJANGO_1_8 or DJANGO_1_9:
    from django.apps import apps
    try:
        User = apps.get_registered_model(user_app_name, user_model_name)
    except KeyError:
        pass

if User is None:
    raise ImproperlyConfigured(
        "You have defined a custom user model %s, but the app %s is not "
        "in settings.INSTALLED_APPS" % (settings.AUTH_USER_MODEL, user_app_name)
    )

# Sanity checks. Possibly rely on the dynamic username field in future.
user = User()

if not hasattr(user, 'username'):
    from dash.exceptions import ImproperlyConfigured
    raise ImproperlyConfigured("Your custom user model ({0}.{1}) doesn't "
                               "have ``username`` property, while "
                               "``django-fobi`` relies on its' presence."
                               "".format(user._meta.app_label, user._meta.object_name))

AUTH_USER_MODEL = settings.AUTH_USER_MODEL
