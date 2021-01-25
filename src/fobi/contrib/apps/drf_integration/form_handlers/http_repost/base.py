import logging
from mimetypes import guess_type
import os

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from six import PY3

from ......base import IntegrationFormHandlerPlugin
from ......helpers import extract_file_path

from ... import UID as INTEGRATE_WITH_UID
from ...base import get_processed_serializer_data

from . import UID

__title__ = 'fobi.contrib.apps.drf_integration.' \
            'fobi_integration_form_handlers.http_repost.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'HTTPRepostHandlerPlugin',
)

LOGGER = logging.getLogger(__name__)


class HTTPRepostHandlerPlugin(IntegrationFormHandlerPlugin):
    """HTTP re-post handler plugin."""

    uid = UID
    name = _("Mail")
    integrate_with = INTEGRATE_WITH_UID

    def run(self,
            form_handler_plugin,
            form_entry,
            request,
            form_element_entries=None,
            **kwargs):
        """Run."""
        serializer = kwargs['serializer']

        files = self._prepare_files(request, serializer)

        return form_handler_plugin.do_http_repost(request, files)

    def _prepare_files(self, request, serializer):
        """Prepares the files for being attached to the mail message."""
        files = {}

        def process_path(file_path, imf):
            """Processes the file path and the file."""
            if file_path:
                file_path = file_path.replace(
                    settings.MEDIA_URL,
                    os.path.join(settings.MEDIA_ROOT, '')
                )
                mime_type = guess_type(imf.name)

                if PY3:
                    imf_chunks = b''.join([c for c in imf.chunks()])
                else:
                    imf_chunks = ''.join([c for c in imf.chunks()])

                files[field_name] = (
                    imf.name,
                    imf_chunks,
                    mime_type[0] if mime_type else ''
                )

        for field_name, imf in request.FILES.items():
            try:
                file_path = serializer.validated_data.get(field_name, '')
                process_path(file_path, imf)
            except Exception as err:
                file_path = extract_file_path(imf.name)
                process_path(file_path, imf)

        return files
