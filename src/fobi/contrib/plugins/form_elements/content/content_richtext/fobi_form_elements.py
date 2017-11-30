from __future__ import absolute_import

from fobi.base import form_element_plugin_registry

from .base import ContentRichTextPlugin

__title__ = 'fobi.contrib.plugins.form_elements.content.content_richtext.' \
            'fobi_form_elements'
__author__ = 'Frantisek Holop <fholop@ripe.net>'
__copyright__ = 'RIPE NCC'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ContentRichTextPlugin',)


form_element_plugin_registry.register(ContentRichTextPlugin)
