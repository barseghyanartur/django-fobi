__title__ = 'fobi.contrib.plugins.form_elements.fields.file.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('FileInputPlugin',)

import os

from django.forms.fields import FileField
from django.forms.widgets import ClearableFileInput
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from fobi.base import FormFieldPlugin, form_element_plugin_registry
from fobi.helpers import handle_uploaded_file

from . import UID
from .forms import FileInputForm
from .settings import FILES_UPLOAD_DIR

class FileInputPlugin(FormFieldPlugin):
    """
    File field plugin.
    """
    uid = UID
    name = _("File")
    group = _("Fields")
    form = FileInputForm

    def get_form_field_instances(self):
        """
        Get form field instances.
        """
        kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'widget': ClearableFileInput(attrs={}),
        }
        if self.data.max_length:
            kwargs['max_length'] = self.data.max_length

        return [(self.data.name, FileField, kwargs)]

    def submit_plugin_form_data(self, form_entry, request, form):
        """
        Submit plugin form data/process file upload. Handling the posted data for file
        plugin when form is submitted. This method affects the original form and that's
        why it returns it.

        :param fobi.models.FormEntry form_entry: Instance of ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        """
        # Get the file path
        file_path = form.cleaned_data.get(self.data.name, None)
        if file_path:
            # Handle the upload
            saved_file = handle_uploaded_file(FILES_UPLOAD_DIR, file_path)
            # Overwrite ``cleaned_data`` of the ``form`` with path to moved file.
            file_relative_url = saved_file.replace(os.path.sep, '/')
            form.cleaned_data[self.data.name] = "{0}{1}".format(settings.MEDIA_URL, file_relative_url)

        # It's critically important to return the ``form`` with updated ``cleaned_data``
        return form


form_element_plugin_registry.register(FileInputPlugin)
