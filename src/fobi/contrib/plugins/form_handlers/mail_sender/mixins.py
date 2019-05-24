from __future__ import absolute_import, unicode_literals

import datetime
from mimetypes import guess_type
import os

from six import string_types, PY3

from django.conf import settings

from .....helpers import extract_file_path, safe_text

from .helpers import send_mail
from .settings import MULTI_EMAIL_FIELD_VALUE_SPLITTER

__title__ = 'fobi.contrib.plugins.form_handlers.mail_sender.mixins'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'MailSenderHandlerMixin',
)

# *****************************************************************************
# **************************** Form handler ***********************************
# *****************************************************************************


class MailSenderHandlerMixin(object):
    """Mail handler mixin."""

    def get_base_url(self, request):
        """Get base URL.

        Might be used in integration packages.
        """
        base_url = 'http{secure}://{host}'.format(
            secure=('s' if request.is_secure() else ''),
            host=request.get_host()
        )
        return base_url

    def get_rendered_data(self,
                          cleaned_data,
                          field_name_to_label_map,
                          base_url):
        """Get rendered data.

        Might be used in integration packages.
        """
        rendered_data = []
        for key, value in cleaned_data.items():
            if value:
                if isinstance(value, string_types) \
                        and value.startswith(settings.MEDIA_URL):
                    cleaned_data[key] = '{base_url}{value}'.format(
                        base_url=base_url, value=value
                    )

                if isinstance(value, (datetime.datetime, datetime.date)):
                    cleaned_data[key] = value.isoformat() \
                        if hasattr(value, 'isoformat') \
                        else value

            label = field_name_to_label_map.get(key, key)
            rendered_data.append('{0}: {1}\n'.format(
                safe_text(label), safe_text(cleaned_data[key]))
            )
        return rendered_data

    def send_email(self, rendered_data, cleaned_data, files):
        """Send email.

        Might be used in integration packages.
        """
        to_email = cleaned_data.get(self.data.form_field_name_to_email)
        # Handling more than one email address
        if isinstance(to_email, (list, tuple)):
            pass  # Anything else needed here?
        else:
            # Assume that it's string
            to_email = to_email.split(
                MULTI_EMAIL_FIELD_VALUE_SPLITTER
            )

        send_mail(
            safe_text(self.data.subject),
            u"{0}\n\n{1}".format(
                safe_text(self.data.body),
                ''.join(rendered_data)
            ),
            self.data.from_email,
            to_email,
            fail_silently=False,
            attachments=files.values()
        )

    def _prepare_files(self, request, form):
        """Prepares the files for being attached to the mail message."""
        files = {}

        def process_path(file_path, imf):
            """Processes the file path and the file."""
            if file_path:
                # if file_path.startswith(settings.MEDIA_URL):
                #     file_path = file_path[1:]
                # file_path = settings.PROJECT_DIR('../{0}'.format(file_path))
                file_path = file_path.replace(
                    settings.MEDIA_URL,
                    os.path.join(settings.MEDIA_ROOT, '')
                )
                mime_type = guess_type(imf.name)
                if PY3:
                    imf_chunks = b''.join([c for c in imf.chunks()])
                else:
                    imf_chunks = str('').join([c for c in imf.chunks()])
                files[field_name] = (
                    imf.name,
                    imf_chunks,
                    mime_type[0] if mime_type else ''
                )

        for field_name, imf in request.FILES.items():
            try:
                file_path = form.cleaned_data.get(field_name, '')
                process_path(file_path, imf)
            except Exception as err:
                file_path = extract_file_path(imf.name)
                process_path(file_path, imf)

        return files
