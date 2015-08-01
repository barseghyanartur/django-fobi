from __future__ import absolute_import

__title__ = 'fobi.contrib.plugins.form_elements.fields.datetime.widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BaseDateTimePluginWidget',)

from fobi.base import FormElementPluginWidget

from . import UID

class BaseDateTimePluginWidget(FormElementPluginWidget):
    """
    Base datetime form element plugin widget.
    """
    plugin_uid = UID
