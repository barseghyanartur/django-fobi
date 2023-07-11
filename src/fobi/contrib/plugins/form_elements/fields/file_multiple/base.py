from __future__ import absolute_import, unicode_literals

import json
import os

from django.conf import settings
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _

from . import UID
from .fields import AllowedExtensionsMultipleFileField as FileField
from .forms import FileMultipleInputForm
from .settings import FILES_MULTIPLE_UPLOAD_DIR

from fobi.base import FormFieldPlugin
from fobi.helpers import handle_uploaded_file

__title__ = "file_multiple.base"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2019 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = ("FileMultipleInputPlugin",)


class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True


class FileMultipleInputPlugin(FormFieldPlugin):
    """File field plugin."""

    uid = UID
    name = _("File multiple")
    group = _("Fields")
    form = FileMultipleInputForm

    def get_form_field_instances(
        self, request=None, form_entry=None, form_element_entries=None, **kwargs
    ):
        """Get form field instances."""
        attrs = {'multiple': True}
        if self.data.allowed_extensions:
            attrs["accept"] = self.data.allowed_extensions.replace(" ", "")

        field_kwargs = {
            "label": self.data.label,
            "help_text": self.data.help_text,
            "initial": self.data.initial,
            "required": self.data.required,
            "widget": MultipleFileInput(attrs=attrs),
        }
        if self.data.max_length is not None:
            field_kwargs["max_length"] = self.data.max_length

        if self.data.allowed_extensions:
            field_kwargs["allowed_extensions"] = self.data.allowed_extensions

        return [(self.data.name, FileField, field_kwargs)]

    def prepare_plugin_form_data(self, cleaned_data):
        """Prepare plugin form data.

        :param cleaned_data:
        :return:
        """
        # Get the file path
        file_path = cleaned_data.get(self.data.name, None)
        if file_path:
            if isinstance(file_path, (list, tuple)):
                fs = []
                for filep in file_path:
                    saved_file = handle_uploaded_file(FILES_MULTIPLE_UPLOAD_DIR, filep)
                    file_relative_url = saved_file.replace(os.path.sep, "/")
                    fs.append(f"{settings.MEDIA_URL}{file_relative_url}")

                cleaned_data[self.data.name] = json.dumps(fs)

            else:
                # Handle the upload
                saved_file = handle_uploaded_file(FILES_MULTIPLE_UPLOAD_DIR, file_path)
                # Overwrite ``cleaned_data`` of the ``form`` with path to moved
                # file.
                file_relative_url = saved_file.replace(os.path.sep, "/")
                cleaned_data[self.data.name] = "{0}{1}".format(
                    settings.MEDIA_URL, file_relative_url
                )

            # It's critically important to return the ``form`` with updated
            # ``cleaned_data``
            return cleaned_data

    def submit_plugin_form_data(
        self, form_entry, request, form, form_element_entries=None, **kwargs
    ):
        """Submit plugin form data/process file upload.

        Handling the posted data for file plugin when form is submitted.
        This method affects the original form and that's why it returns it.

        :param fobi.models.FormEntry form_entry: Instance
            of ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        :param form_element_entries:
        """
        print('submit_plugin_form_data', request.FILES.keys())
        for file in request.FILES:
            print('FF', file)
        # Get the file path
        cleaned_data = self.prepare_plugin_form_data(form.cleaned_data)

        if cleaned_data:
            form.cleaned_data = cleaned_data

        # # Get the file path
        # file_path = form.cleaned_data.get(self.data.name, None)
        # if file_path:
        #     # Handle the upload
        #     saved_file = handle_uploaded_file(FILES_UPLOAD_DIR, file_path)
        #     # Overwrite ``cleaned_data`` of the ``form`` with path to moved
        #     # file.
        #     file_relative_url = saved_file.replace(os.path.sep, '/')
        #     form.cleaned_data[self.data.name] = "{0}{1}".format(
        #         settings.MEDIA_URL,
        #         file_relative_url
        #     )

        # It's critically important to return the ``form`` with updated
        # ``cleaned_data``
        return form
