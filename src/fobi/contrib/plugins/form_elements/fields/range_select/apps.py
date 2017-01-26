__title__ = 'fobi.contrib.plugins.form_elements.fields.range_select.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)

try:
    from django.apps import AppConfig

    class Config(AppConfig):
        """Config."""

        name = 'fobi.contrib.plugins.form_elements.fields.range_select'
        label = 'fobi_contrib_plugins_form_elements_fields_range_select'

except ImportError:
    pass
