from fobi.base import form_element_plugin_widget_registry
from fobi.contrib.plugins.form_elements.test.dummy.widgets import (
    BaseDummyPluginWidget
)
from fobi.contrib.themes.bootstrap3 import UID

__title__ = 'fobi.contrib.themes.bootstrap3.widgets.form_elements.' \
            'dummy_bootstrap3_widget.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DummyPluginWidget',)


class DummyPluginWidget(BaseDummyPluginWidget):
    """Dummy plugin widget for Boootstrap 3."""
    theme_uid = UID
    media_js = [
        # 'bootstrap3/js/fobi.plugin.dummy-bootstrap3-widget.js',
    ]
    media_css = [
        # 'datetime/css/fobi.plugin.dummy-bootstrap3-widget.css',
    ]


# Registering the widget
form_element_plugin_widget_registry.register(DummyPluginWidget)
