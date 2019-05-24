from __future__ import absolute_import

from fobi.base import form_element_plugin_registry

from .base import FileInputPlugin

__title__ = 'fobi.contrib.plugins.form_elements.fields.file.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('FileInputPlugin',)


form_element_plugin_registry.register(FileInputPlugin)
