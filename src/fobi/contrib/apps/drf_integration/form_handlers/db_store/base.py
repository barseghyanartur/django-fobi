import logging
import os

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from ......base import IntegrationFormHandlerPlugin
from ......helpers import extract_file_path

from ... import UID as INTEGRATE_WITH_UID
from ...base import get_processed_serializer_data

from . import UID

__title__ = 'fobi.contrib.apps.drf_integration.' \
            'fobi_integration_form_handlers.db_store.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'DBStoreHandlerPlugin',
)

LOGGER = logging.getLogger(__name__)


class DBStoreHandlerPlugin(IntegrationFormHandlerPlugin):
    """DB store form handler plugin.

    Can be used only once per form.
    """

    uid = UID
    name = _("DB store")
    integrate_with = INTEGRATE_WITH_UID

    def run(self,
            form_handler_plugin,
            form_entry,
            request,
            form_element_entries=None,
            **kwargs):
        """Run."""
        serializer = kwargs['serializer']

        # Clean up the values, leave our content fields and empty values.
        field_name_to_label_map, cleaned_data = get_processed_serializer_data(
            serializer,
            form_element_entries
        )

        form_handler_plugin.save_form_data_entry(
            form_entry,
            request,
            field_name_to_label_map,
            cleaned_data
        )

    def _prepare_files(self, request, serializer):
        """Prepares the files for being attached to the mail message."""
        files = {}

        def process_path(file_path, imf):
            if file_path:
                file_path = file_path.replace(
                    settings.MEDIA_URL,
                    os.path.join(settings.MEDIA_ROOT, '')
                )
                files[field_name] = (imf.name, open(file_path, 'rb'))

        for field_name, imf in request.FILES.items():
            try:
                file_path = serializer.validate_data.get(field_name, '')
                process_path(file_path, imf)
            except Exception as err:
                file_path = extract_file_path(imf.name)
                process_path(file_path, imf)

        return files
