__title__ = 'fobi.context_processors'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('theme', 'dynamic_values', 'form_importers',)

import datetime

from fobi.base import get_theme
from fobi.helpers import StrippedRequest
from fobi.form_importers import get_form_impoter_plugin_urls

def theme(request):
    """
    Gets active theme.

    :param django.http.HttpRequest request:
    :return fobi.base.BaseTheme: Instance of ``fobi.base.BaseTheme``.
    """
    return {'fobi_theme': get_theme(request, as_instance=True)}

def dynamic_values(request):
    """
    Dynamic values exposed to public forms.
    """
    return {
        'fobi_dynamic_values': {
            'request': StrippedRequest(request),
            'now': datetime.datetime.now(),
            'today': datetime.date.today(),
        }
    }

def form_importers(request):
    """
    Form importers.
    """
    return {
        'form_importers': get_form_impoter_plugin_urls(),
    }
