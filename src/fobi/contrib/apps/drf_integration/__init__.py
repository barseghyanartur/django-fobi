__title__ = "fobi.contrib.apps.drf_integration"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2016-2019 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = ("default_app_config",)


if django.VERSION < (3, 2): # pragma: no cover
    default_app_config = "fobi.contrib.apps.drf_integration.apps.Config"

UID = "drf_integration"
