from django.apps import AppConfig

__title__ = (
    "fobi.contrib.apps.drf_integration.form_elements.fields."
    "date_drop_down.apps"
)
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2019 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = ("Config",)


class Config(AppConfig):
    """Config."""

    name = (
        "fobi.contrib.apps.drf_integration.form_elements.fields."
        "date_drop_down"
    )
    label = (
        "fobi_contrib_apps_drf_integration_form_elements_fields_"
        "date_drop_down"
    )
