from django.apps import AppConfig

__title__ = (
    "fobi.contrib.themes.simple.widgets.form_elements."
    "invisible_recaptcha_simple_widget.apps"
)
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2019 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = ("Config",)


class Config(AppConfig):
    """Config."""

    name = (
        "fobi.contrib.themes.simple.widgets.form_elements."
        "invisible_recaptcha_simple_widget"
    )
    label = (
        "fobi_contrib_themes_simple_widgets_form_elements_"
        "invisible_recaptcha_simple_widget"
    )
