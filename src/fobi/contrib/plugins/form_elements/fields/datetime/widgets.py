from __future__ import absolute_import

from fobi.base import FormElementPluginWidget

from . import UID

__title__ = 'fobi.contrib.plugins.form_elements.fields.datetime.widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BaseDateTimePluginWidget',)


class BaseDateTimePluginWidget(FormElementPluginWidget):
    """Base datetime form element plugin widget."""

    plugin_uid = UID
