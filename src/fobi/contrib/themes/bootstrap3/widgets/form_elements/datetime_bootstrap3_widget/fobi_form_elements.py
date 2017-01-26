from fobi.base import form_element_plugin_widget_registry
from fobi.contrib.plugins.form_elements.fields.datetime.widgets import (
    BaseDateTimePluginWidget
)
from fobi.contrib.themes.bootstrap3 import UID

__title__ = 'fobi.contrib.themes.bootstrap3.widgets.form_elements.' \
            'datetime_bootstrap3_widget.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DateTimePluginWidget',)


class DateTimePluginWidget(BaseDateTimePluginWidget):
    """DateTime plugin widget for Bootstrap 3."""

    theme_uid = UID
    media_js = [
        'js/moment-with-locales.js',
        'bootstrap3/js/bootstrap-datetimepicker.min.js',
        'bootstrap3/js/fobi.plugin.datetime-bootstrap3-widget.js',
    ]
    media_css = [
        'bootstrap3/css/bootstrap-datetimepicker.min.css',
        # 'datetime/css/fobi.plugin.datetime-bootstrap3-widget.css',
    ]


# Registering the widget
form_element_plugin_widget_registry.register(DateTimePluginWidget)
