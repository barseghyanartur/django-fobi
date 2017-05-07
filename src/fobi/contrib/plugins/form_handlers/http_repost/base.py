import logging
import os

import requests

from django.conf import settings
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from six import PY3

from .....base import (
    form_handler_plugin_registry,
    form_wizard_handler_plugin_registry,
    FormHandlerPlugin,
    FormWizardHandlerPlugin,
)
from .....helpers import extract_file_path

from . import UID
from .forms import HTTPRepostForm

__title__ = 'fobi.contrib.plugins.form_handlers.http_repost.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'HTTPRepostHandlerPlugin',
    'HTTPRepostWizardHandlerPlugin',
)

logger = logging.getLogger(__name__)

# *****************************************************************************
# **************************** Form handler ***********************************
# *****************************************************************************


class HTTPRepostHandlerPlugin(FormHandlerPlugin):
    """HTTP repost handler plugin.

    Makes a HTTP repost to a given endpoint. Should be executed before
    ``db_store`` plugin.
    """

    uid = UID
    name = _("HTTP Repost")
    form = HTTPRepostForm

    def run(self, form_entry, request, form, form_element_entries=None):
        """Run.

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        :param iterable form_element_entries: Iterable of
            ``fobi.models.FormElementEntry`` objects.
        """
        files = self._prepare_files(request, form)

        return self.do_http_repost(request, files)

    def do_http_repost(self, request, files):
        """Re-post data via HTTP.

        Might be used in integration plugins.
        """
        try:
            response = requests.post(
                self.data.endpoint_url,
                data=request.POST.dict(),
                files=files,
                allow_redirects=True,
                timeout=5
            )
            return True, response
        except Exception as err:
            logger.debug(str(err))
            return False, err

    def _prepare_files(self, request, form):
        """Prepares the files for being attached to the mail message."""
        files = {}

        def process_path(file_path, imf):
            if file_path:
                # if file_path.startswith(settings.MEDIA_URL):
                #     file_path = file_path[1:]
                # file_path = settings.PROJECT_DIR('../{0}'.format(file_path))
                file_path = file_path.replace(
                    settings.MEDIA_URL,
                    os.path.join(settings.MEDIA_ROOT, '')
                )
                files[field_name] = (imf.name, open(file_path, 'rb'))

        for field_name, imf in request.FILES.items():
            try:
                file_path = form.cleaned_data.get(field_name, '')
                process_path(file_path, imf)
            except Exception as err:
                file_path = extract_file_path(imf.name)
                process_path(file_path, imf)

        return files

    def plugin_data_repr(self):
        """Human readable representation of plugin data.

        :return string:
        """
        context = {
            'endpoint_url': self.data.endpoint_url,
        }
        return render_to_string('http_repost/plugin_data_repr.html', context)


form_handler_plugin_registry.register(HTTPRepostHandlerPlugin)


# *****************************************************************************
# ************************ Form wizard handler ********************************
# *****************************************************************************


class HTTPRepostWizardHandlerPlugin(FormWizardHandlerPlugin):
    """HTTP repost wizard handler plugin.

    Makes a HTTP repost to a given endpoint. Should be executed before
    ``db_store`` plugin.
    """

    uid = UID
    name = _("HTTP Repost")
    form = HTTPRepostForm

    def run(self, form_wizard_entry, request, form_list, form_wizard,
            form_element_entries=None):
        """Run.

        :param fobi.models.FormWizardEntry form_wizard_entry: Instance
            of :class:`fobi.models.FormWizardEntry`.
        :param django.http.HttpRequest request:
        :param list form_list: List of :class:`django.forms.Form` instances.
        :param fobi.wizard.views.dynamic.DynamicWizardView form_wizard:
            Instance of :class:`fobi.wizard.views.dynamic.DynamicWizardView`.
        :param iterable form_element_entries: Iterable of
            ``fobi.models.FormElementEntry`` objects.
        """
        files = self._prepare_files(request, form_list)
        try:
            response = requests.post(
                self.data.endpoint_url,
                data=request.POST.dict(),
                files=files,
                allow_redirects=True,
                timeout=5
            )
            return (True, response)
        except Exception as err:
            logger.debug(str(err))
            return (False, err)

    def _prepare_files(self, request, form_list):
        """Prepares the files for being attached to the mail message."""
        files = {}

        def process_path(file_path, imf):
            if file_path:
                # if file_path.startswith(settings.MEDIA_URL):
                #     file_path = file_path[1:]
                # file_path = settings.PROJECT_DIR('../{0}'.format(file_path))
                file_path = file_path.replace(
                    settings.MEDIA_URL,
                    os.path.join(settings.MEDIA_ROOT, '')
                )
                files[field_name] = (imf.name, open(file_path, 'rb'))

        for form in form_list:
            for field_name, imf in request.FILES.items():
                try:
                    file_path = form.cleaned_data.get(field_name, '')
                    process_path(file_path, imf)
                except Exception as err:
                    file_path = extract_file_path(imf.name)
                    process_path(file_path, imf)

        return files

    def plugin_data_repr(self):
        """Human readable representation of plugin data.

        :return string:
        """
        context = {
            'endpoint_url': self.data.endpoint_url,
        }
        return render_to_string('http_repost/plugin_data_repr.html', context)


form_wizard_handler_plugin_registry.register(HTTPRepostWizardHandlerPlugin)
