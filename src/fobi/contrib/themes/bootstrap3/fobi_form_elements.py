__title__ = 'fobi.contrib.themes.bootstrap3.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DummyPluginWidget',)

from fobi.base import form_element_plugin_widget_registry
from fobi.contrib.plugins.form_elements.content.dummy.widgets import BaseDummyPluginWidget

class DummyPluginWidget(BaseDummyPluginWidget):
    """
    Dummy plugin widget for Boootstrap 3.
    """
    theme_uid = 'bootstrap3'
    media_js = ['dummy/js/fobi.plugins.form_elements.dummy.js',]
    media_css = ['dummy/css/fobi.plugins.form_elements.dummy.css',]


# Registering the widget
form_element_plugin_widget_registry.register(DummyPluginWidget)
