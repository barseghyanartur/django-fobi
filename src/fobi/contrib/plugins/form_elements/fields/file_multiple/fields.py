from os.path import splitext

from django.forms import forms
from django.forms.fields import FileField
from django.utils.translation import gettext_lazy as _

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2023 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = ("AllowedExtensionsMultipleFileField",)


class AllowedExtensionsMultipleFileField(FileField):
    """Same as FileField, but customizable.

    You can specify:
        * allowed_extension - list containing allowed extensions.
        Example: '.pdf, .jpeg'
    """

    def __init__(
        self,
        allowed_extensions=None,
        required=True,
        widget=None,
        label=None,
        initial=None,
        help_text="",
        *args,
        **kwargs,
    ):
        super(AllowedExtensionsMultipleFileField, self).__init__(
            required=required,
            widget=widget,
            label=label,
            initial=initial,
            help_text=help_text,
            *args,
            **kwargs,
        )
        if allowed_extensions:
            self.allowed_extensions = allowed_extensions.replace(" ", "").split(
                ","
            )
        else:
            self.allowed_extensions = allowed_extensions

    def validate(self, file):
        super(AllowedExtensionsMultipleFileField, self).validate(file)

        if file and self.allowed_extensions:
            extension = splitext(file.name)[1].lower()
            if extension not in self.allowed_extensions:
                raise forms.ValidationError(
                    _("File extension '{0}' is not allowed.".format(extension))
                )

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
