__title__ = 'fobi.contrib.apps.drf_integration.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

try:
    __all__ = ('Config',)

    from django.apps import AppConfig

    class Config(AppConfig):
        name = 'fobi.contrib.apps.drf_integration'
        label = 'fobi_contrib_apps_drf_integration'

except ImportError:
    pass
