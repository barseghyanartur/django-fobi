from os.path import splitext
from django.forms.fields import FileField
from django.forms import forms
from django.utils.translation import ugettext_lazy as _


class AllowedExtensionsFileField(FileField):
    """
    Same as FileField, but you can specify:
        * allowed_extension - list containing allowed extensions.
        Example: '.pdf, .jpeg'
    """

    def __init__(self, allowed_extensions=None, required=True,
                 widget=None, label=None, initial=None, help_text='', *args,
                 **kwargs):
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

        if self.allowed_extensions:
            extension = splitext(file.name)[1].lower()
            if extension not in self.allowed_extensions:
                raise forms.ValidationError(
                    _("File extension '{0}' is not allowed.".format(
                        extension)))
