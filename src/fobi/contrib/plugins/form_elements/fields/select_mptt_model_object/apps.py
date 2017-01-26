__title__ = 'fobi.contrib.plugins.form_elements.fields.' \
            'select_mptt_model_object.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)

try:
    from django.apps import AppConfig

    class Config(AppConfig):
        """Config."""

        name = 'fobi.contrib.plugins.form_elements.fields.' \
               'select_mptt_model_object'
        label = 'fobi_contrib_plugins_form_elements_fields_' \
                'select_mptt_model_object'

except ImportError:
    pass
