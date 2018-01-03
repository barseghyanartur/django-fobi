from __future__ import absolute_import

from fobi.base import form_element_plugin_registry

from .base import ContentImagePlugin

__title__ = 'fobi.contrib.plugins.form_elements.content.content_image.' \
            'fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ContentImagePlugin',)


form_element_plugin_registry.register(ContentImagePlugin)
