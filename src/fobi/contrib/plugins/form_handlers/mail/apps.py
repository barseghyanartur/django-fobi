from __future__ import absolute_import
from django.apps import AppConfig

__title__ = 'fobi.contrib.plugins.form_handlers.mail.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)


class Config(AppConfig):
    """Config."""

    name = 'fobi.contrib.plugins.form_handlers.mail'
    label = 'fobi_contrib_plugins_form_handlers_mail'
