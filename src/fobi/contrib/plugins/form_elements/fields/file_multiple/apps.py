from django.apps import AppConfig

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2023 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = ("Config",)


class Config(AppConfig):
    """Config."""

    name = "fobi.contrib.plugins.form_elements.fields.file_multiple"
    label = "fobi_contrib_plugins_form_elements_fields_file_multiple"
