__title__ = 'fobi.contrib.themes.djangocms_admin_style_theme.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2015-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)

try:
    from django.apps import AppConfig

    class Config(AppConfig):
        """Config."""

        name = 'fobi.contrib.themes.djangocms_admin_style_theme'
        label = 'fobi_contrib_themes_djangocms_admin_style_theme'

except ImportError:
    pass
