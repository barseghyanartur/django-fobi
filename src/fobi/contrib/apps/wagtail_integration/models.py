from __future__ import absolute_import

from .abstract import AbstractFobiFormPage

__title__ = 'fobi.contrib.apps.wagtail_integration.models'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('FobiFormPage',)


class FobiFormPage(AbstractFobiFormPage):
    """Fobi form page."""
