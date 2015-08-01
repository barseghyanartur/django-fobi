__title__ = 'fobi.contrib.plugins.form_elements.test.dummy.widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BaseDummyPluginWidget',)

from fobi.base import FormElementPluginWidget

from . import UID

class BaseDummyPluginWidget(FormElementPluginWidget):
    """
    Base dummy form element plugin widget.
    """
    plugin_uid = UID
