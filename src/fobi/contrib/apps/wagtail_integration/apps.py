from django.apps import AppConfig

__title__ = 'fobi.contrib.apps.wagtail_integration.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)


class Config(AppConfig):
    """Config."""

    name = 'fobi.contrib.apps.wagtail_integration'
    label = 'fobi_contrib_apps_wagtail_integration'
