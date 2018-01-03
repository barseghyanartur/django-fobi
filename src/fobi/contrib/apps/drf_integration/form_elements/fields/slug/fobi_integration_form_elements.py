from .......base import integration_form_element_plugin_registry
from .base import SlugInputPlugin

__title__ = 'fobi.contrib.apps.drf_integration.form_elements.fields.slug.' \
            'fobi_integration_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('SlugInputPlugin',)


integration_form_element_plugin_registry.register(SlugInputPlugin)
