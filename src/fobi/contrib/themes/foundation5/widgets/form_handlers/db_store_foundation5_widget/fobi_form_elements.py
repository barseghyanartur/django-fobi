from fobi.base import form_handler_plugin_widget_registry
from fobi.contrib.plugins.form_handlers.db_store.widgets import (
    BaseDbStorePluginWidget
)
from fobi.contrib.themes.foundation5 import UID

__title__ = 'fobi.contrib.themes.foundation5.widgets.form_handlers.' \
            'db_store_foundation5_widget.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DbStorePluginWidget',)


class DbStorePluginWidget(BaseDbStorePluginWidget):
    """DbStore plugin widget for Foundation 5."""

    theme_uid = UID
    view_entries_icon_class = 'fi-list'
    export_entries_icon_class = 'fi-page-export'
    view_saved_form_data_entries_template_name = \
        'db_store_foundation5_widget/view_saved_form_data_entries.html'


# Registering the widget
form_handler_plugin_widget_registry.register(DbStorePluginWidget)
