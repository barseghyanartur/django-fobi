from django.apps import AppConfig

__title__ = 'fobi.contrib.plugins.form_elements.content.content_richtext.apps'
__author__ = 'Frantisek Holop <fholop@ripe.net>'
__copyright__ = 'RIPE NCC'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)


class Config(AppConfig):
    """Config."""

    name = 'fobi.contrib.plugins.form_elements.content.content_richtext'
    label = 'fobi_contrib_plugins_form_elements_content_content_richtext'
