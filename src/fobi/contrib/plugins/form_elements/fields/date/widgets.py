from __future__ import absolute_import

from fobi.base import FormElementPluginWidget

from . import UID

__title__ = 'fobi.contrib.plugins.form_elements.fields.date.widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BaseDatePluginWidget',)


class BaseDatePluginWidget(FormElementPluginWidget):
    """Base date form element plugin widget."""

    plugin_uid = UID
