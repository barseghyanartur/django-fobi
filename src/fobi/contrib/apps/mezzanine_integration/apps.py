__title__ = 'fobi.contrib.apps.mezzanine_integration.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)

try:
    from django.apps import AppConfig

    class Config(AppConfig):
        name = 'fobi.contrib.apps.mezzanine_integration'
        label = 'fobi_contrib_apps_mezzanine_integration'

except ImportError:
    pass
