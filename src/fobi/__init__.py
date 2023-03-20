__title__ = "django-fobi"
__version__ = "0.19.8"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2022 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"

if django.VERSION < (3, 2): # pragma: no cover
    default_app_config = "fobi.apps.Config"
