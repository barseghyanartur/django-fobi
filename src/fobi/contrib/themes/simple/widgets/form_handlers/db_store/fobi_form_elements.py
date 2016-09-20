from fobi.base import form_handler_plugin_widget_registry
from fobi.contrib.plugins.form_handlers.db_store.widgets import (
    BaseDbStorePluginWidget
)
from fobi.contrib.themes.simple import UID

__title__ = 'fobi.contrib.themes.simple.widgets.form_handlers.' \
            'db_store.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DbStorePluginWidget',)


class DbStorePluginWidget(BaseDbStorePluginWidget):
    """DbStore plugin widget for Simple theme."""

    theme_uid = UID
    view_entries_icon_class = ''
    export_entries_icon_class = ''


# Registering the widget
form_handler_plugin_widget_registry.register(DbStorePluginWidget)
