from django import forms

__title__ = "fobi.reusable.email_repeat.widget"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2019 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = ("EmailRepeatWidget",)


class EmailRepeatWidget(forms.MultiWidget):
    """EmailRepeatWidget."""

    def __init__(self, attrs=None):
        widgets = (
            forms.EmailInput(attrs=attrs),
            forms.EmailInput(attrs=attrs),
        )
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value, value]
        return ["", ""]

    def value_from_datadict(self, data, files, name):
        email1 = data.get(f"{name}_0")
        email2 = data.get(f"{name}_1")
        return email1, email2
