__title__ = "fobi.contrib.themes.djangocms_admin_style_theme"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2015-2019 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = (
    "default_app_config",
    "UID",
)

if django.VERSION < (3, 2): # pragma: no cover
    default_app_config = (
        "fobi.contrib.themes." "djangocms_admin_style_theme.apps.Config"
    )

UID = "djangocms_admin_style_theme"
