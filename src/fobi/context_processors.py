__title__ = 'fobi.context_processors'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('theme',)

from fobi.base import get_theme

def theme(request):
    """
    Gets active theme.

    :param django.http.HttpRequest request:
    :return fobi.base.BaseTheme: Instance of ``fobi.base.BaseTheme``.
    """
    return {'fobi_theme': get_theme(request, as_instance=True)}
