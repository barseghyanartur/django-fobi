__title__ = 'fobi.contrib.themes.foundation5.widgets.form_elements.dummy_foundation5_widget.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)

try:
    from django.apps import AppConfig

    class Config(AppConfig):
        name = 'fobi.contrib.themes.foundation5.widgets.form_elements.dummy_foundation5_widget'
        label = 'fobi_contrib_themes_foundation5_widgets_form_elements_dummy_foundation5_widget'

except ImportError:
    pass
