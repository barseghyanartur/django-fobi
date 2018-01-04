from django.apps import AppConfig

__title__ = 'fobi.contrib.themes.djangocms_admin_style_theme.widgets.' \
            'form_elements.' \
            'content_richtext_admin_style_widget.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)


class Config(AppConfig):
    """Config."""

    name = 'fobi.contrib.themes.djangocms_admin_style_theme.widgets.' \
           'form_elements.' \
           'content_richtext_admin_style_widget'
    label = 'fobi_contrib_themes_djangocms_admin_style_theme_widgets_' \
            'form_elements_content_richtext_admin_style_widget'
