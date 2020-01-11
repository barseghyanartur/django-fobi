from os.path import splitext

from django.forms import forms
from django.forms.fields import FileField
from django.utils.translation import gettext_lazy as _

__title__ = 'fobi.contrib.plugins.form_elements.fields.file.fields'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('AllowedExtensionsFileField',)


class AllowedExtensionsFileField(FileField):
    """Same as FileField, but customizable.

    You can specify:
        * allowed_extension - list containing allowed extensions.
        Example: '.pdf, .jpeg'
    """

    def __init__(self, allowed_extensions=None, required=True,
                 widget=None, label=None, initial=None, help_text='',
                 *args, **kwargs):
        super(AllowedExtensionsFileField, self).__init__(
            required=required, widget=widget, label=label,
            initial=initial, help_text=help_text, *args, **kwargs
        )
        if allowed_extensions:
            self.allowed_extensions = allowed_extensions.replace(' ', '') \
                                                        .split(',')
        else:
            self.allowed_extensions = allowed_extensions

    def validate(self, file):
        super(AllowedExtensionsFileField, self).validate(file)

        if file and self.allowed_extensions:
            extension = splitext(file.name)[1].lower()
            if extension not in self.allowed_extensions:
                raise forms.ValidationError(
                    _("File extension '{0}' is not allowed.".format(extension))
                )
