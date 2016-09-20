from fobi.base import form_element_plugin_widget_registry
from fobi.contrib.plugins.form_elements.fields.date.widgets import (
    BaseDatePluginWidget
)
from fobi.contrib.themes.foundation5 import UID

__title__ = 'fobi.contrib.themes.foundation5.widgets.form_elements.' \
            'date_foundation5_widget.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DatePluginWidget',)


class DatePluginWidget(BaseDatePluginWidget):
    """Date plugin widget for Foundation 5."""

    theme_uid = UID
    media_js = [
        'js/moment-with-locales.js',
        'foundation5/js/foundation-datepicker.js',
        'foundation5/js/fobi.plugin.date-foundation5-widget.js',
    ]
    media_css = [
        'foundation5/css/foundation-datepicker.css',
        # 'datetime/css/fobi.plugin.date-foundation5-widget.css',
    ]


# Registering the widget
form_element_plugin_widget_registry.register(DatePluginWidget)
