from .....base import FormHandlerPluginWidget

from . import UID

__title__ = 'fobi.contrib.plugins.form_handlers.db_store.widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BaseDbStorePluginWidget',)


class BaseDbStorePluginWidget(FormHandlerPluginWidget):
    """Base dummy form element plugin widget."""

    plugin_uid = UID
    view_entries_icon_class = 'glyphicon glyphicon-list'
    export_entries_icon_class = 'glyphicon glyphicon-export'
    view_saved_form_data_entries_template_name = \
        'db_store/view_saved_form_data_entries.html'
