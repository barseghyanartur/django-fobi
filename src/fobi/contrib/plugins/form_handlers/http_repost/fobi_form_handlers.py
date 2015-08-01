__title__ = 'fobi.contrib.plugins.form_handlers.http_repost.fobi_form_handlers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('HTTPRepostHandlerPlugin',)

import logging
import os

import requests

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string

from fobi.base import FormHandlerPlugin, form_handler_plugin_registry
from fobi.helpers import extract_file_path

from . import UID
from .forms import HTTPRepostForm

logger = logging.getLogger(__name__)

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
        files = self._prepare_files(request, form)
        try:
            response = requests.post(
                self.data.endpoint_url,
                data = request.POST.dict(),
                files = files,
                allow_redirects = True,
                timeout = 5
                )
            return (True, response)
        except Exception as err:
            logger.debug(str(err))
            return (False, err)

    def _prepare_files(self, request, form):
        """
        Prepares the files for being attached to the mail message.
        """
        files = {}

        def process_path(file_path, imf):
            if file_path:
                #if file_path.startswith(settings.MEDIA_URL):
                #    file_path = file_path[1:]
                #file_path = settings.PROJECT_DIR('../{0}'.format(file_path))
                file_path = file_path.replace(
                    settings.MEDIA_URL,
                    os.path.join(settings.MEDIA_ROOT, '')
                    )
                files[field_name] = (imf.name, open(file_path, 'rb'))

        for field_name, imf in request.FILES.items():
            try:
                file_path = form.cleaned_data.get(field_name, '')
                process_path(file_path, imf)
            except Exception as e:
                file_path = extract_file_path(imf.name)
                process_path(file_path, imf)

        return files

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
