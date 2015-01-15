__title__ = 'fobi.contrib.plugins.form_handlers.http_repost.fobi_form_handlers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('HTTPRepostHandlerPlugin',)

from os.path import join
import logging

import requests

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string

from fobi.base import FormHandlerPlugin, form_handler_plugin_registry
from fobi.contrib.plugins.form_handlers.http_repost import UID
from fobi.contrib.plugins.form_handlers.http_repost.forms import HTTPRepostForm
#from fobi.contrib.plugins.form_handlers.http_repost.helpers \
#    import extract_file_path

logger = logging.getLogger(__name__)

def extract_file_path(name):
    """
    Extracts the file path.

    :param string name:
    :return string:
    """
    return join(settings.MEDIA_ROOT, name)

class HTTPRepostHandlerPlugin(FormHandlerPlugin):
    """
    HTTP repost handler plugin. Makes a HTTP repost to a given endpoint.

    Should be executed before ``db_store`` plugin.
    """
    uid = UID
    name = _("HTTP Repost")
    form = HTTPRepostForm

    def run(self, form_entry, request, form, form_element_entries=None):
        """
        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        :param iterable form_element_entries: Iterable of
            ``fobi.models.FormElementEntry`` objects.
        """
        files = {}

        def process_path(file_path, imf):
            if file_path:
                if file_path.startswith(settings.MEDIA_URL):
                    file_path = file_path[1:]
                file_path = settings.PROJECT_DIR('../{0}'.format(file_path))
                files[field_name] = (imf.name, open(file_path, 'rb'))

        for field_name, imf in request.FILES.items():
            try:
                file_path = form.cleaned_data.get(field_name, '')
                process_path(file_path, imf)
            except Exception as e:
                file_path = extract_file_path(imf.name)
                process_path(file_path, imf)

        response = requests.post(self.data.endpoint_url, \
                                 data=request.POST, files=files)

    def plugin_data_repr(self):
        """
        Human readable representation of plugin data.

        :return string:
        """
        context = {
            'endpoint_url': self.data.endpoint_url,
        }
        return render_to_string('http_repost/plugin_data_repr.html', context)


form_handler_plugin_registry.register(HTTPRepostHandlerPlugin)
