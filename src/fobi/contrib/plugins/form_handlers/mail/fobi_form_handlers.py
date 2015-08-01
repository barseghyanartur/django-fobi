from __future__ import absolute_import

__title__ = 'fobi.contrib.plugins.form_handlers.mail.fobi_form_handlers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('MailHandlerPlugin',)

from mimetypes import guess_type
import os

from six import string_types

from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string
from django.conf import settings

from fobi.base import (
    FormHandlerPlugin, form_handler_plugin_registry, get_processed_form_data
)
from fobi.helpers import safe_text, extract_file_path

from . import UID
from .forms import MailForm
from .helpers import send_mail
from .settings import MULTI_EMAIL_FIELD_VALUE_SPLITTER

class MailHandlerPlugin(FormHandlerPlugin):
    """
    Mail handler plugin. Sends emails to the person specified.

    Should be executed before ``db_store`` and ``http_repost`` plugins.
    """
    uid = UID
    name = _("Mail")
    form = MailForm

    def run(self, form_entry, request, form, form_element_entries=None):
        """
        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        :param iterable form_element_entries: Iterable of
            ``fobi.models.FormElementEntry`` objects.
        """
        base_url = 'http{secure}://{host}'.format(
            secure = ('s' if request.is_secure() else ''),
            host = request.get_host()
            )

        # Clean up the values, leave our content fields and empty values.
        field_name_to_label_map, cleaned_data = get_processed_form_data(
            form,
            form_element_entries
            )

        rendered_data = []
        for key, value in cleaned_data.items():
            if value and isinstance(value, string_types) \
                     and value.startswith(settings.MEDIA_URL):
                cleaned_data[key] = '{base_url}{value}'.format(
                    base_url=base_url, value=value
                    )
            label = field_name_to_label_map.get(key, key)
            rendered_data.append('{0}: {1}\n'.format(
                safe_text(label), safe_text(cleaned_data[key]))
                )

        files = self._prepare_files(request, form)

        # Handling more than one email address
        if isinstance(self.data.to_email, (list, tuple)):
            to_email = self.data.to_email
        else:
            # Assume that it's string
            to_email = self.data.to_email.split(MULTI_EMAIL_FIELD_VALUE_SPLITTER)

        send_mail(
            safe_text(self.data.subject),
            "{0}\n\n{1}".format(safe_text(self.data.body),
            ''.join(rendered_data)),
            self.data.from_email,
            to_email,
            fail_silently = False,
            attachments = files.values()
            )

    def _prepare_files(self, request, form):
        """
        Prepares the files for being attached to the mail message.
        """
        files = {}

        def process_path(file_path, imf):
            """
            Processes the file path and the file.
            """
            if file_path:
                #if file_path.startswith(settings.MEDIA_URL):
                #    file_path = file_path[1:]
                #file_path = settings.PROJECT_DIR('../{0}'.format(file_path))
                file_path = file_path.replace(
                    settings.MEDIA_URL,
                    os.path.join(settings.MEDIA_ROOT, '')
                    )
                mime_type = guess_type(imf.name)
                files[field_name] = (
                    imf.name,
                    ''.join([c for c in imf.chunks()]),
                    mime_type[0] if mime_type else ''
                )

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
        to_email = None
        # Handling more than one email address
        if isinstance(self.data.to_email, (list, tuple)):
            to_email = '{0} '.format(MULTI_EMAIL_FIELD_VALUE_SPLITTER).join(
                            self.data.to_email
                            )
        else:
            # Assume that it's string
            to_email = self.data.to_email

        context = {
            'to_name': safe_text(self.data.to_name),
            'to_email': to_email,
            'subject': safe_text(self.data.subject),
        }
        return render_to_string('mail/plugin_data_repr.html', context)


form_handler_plugin_registry.register(MailHandlerPlugin)
