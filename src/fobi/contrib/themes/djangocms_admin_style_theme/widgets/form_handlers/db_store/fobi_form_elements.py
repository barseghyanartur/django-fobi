from fobi.base import form_handler_plugin_widget_registry
from fobi.contrib.plugins.form_handlers.db_store.widgets import (
    BaseDbStorePluginWidget
)
from fobi.contrib.themes.djangocms_admin_style_theme import UID

__title__ = 'fobi.contrib.themes.djangocms_admin_style_theme.widgets.' \
            'form_handlers.db_store.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2015-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DbStorePluginWidget',)


class DbStorePluginWidget(BaseDbStorePluginWidget):
    """DbStore plugin widget for djangocms_admin_style_theme theme."""

    theme_uid = UID
    view_entries_icon_class = ''
    export_entries_icon_class = ''


# Registering the widget
form_handler_plugin_widget_registry.register(DbStorePluginWidget)
