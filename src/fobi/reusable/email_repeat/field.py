from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .widget import EmailRepeatWidget

__title__ = "fobi.reusable.email_repeat.field"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2019 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = ("EmailRepeatField",)


class EmailRepeatField(forms.MultiValueField):
    """EmailRepeatField.

    Usage example:

        # *******************
        # **** forms.py *****
        # *******************
        from django import forms
        from fobi.reusable.email_repeat.fields import EmailRepeatField

        class MyForm(forms.Form):
            email = EmailRepeatField()

        # *******************
        # **** views.py *****
        # *******************
        from django.shortcuts import render
        from .forms import MyForm

        def my_view(request):
            if request.method == 'POST':
                form = MyForm(request.POST)
                if form.is_valid():
                    email = form.cleaned_data['email']
                    # Do something with email
            else:
                form = MyForm()

            return render(request, 'my_template.html', {'form': form})

        # ***************************
        # **** my_template.html *****
        # ***************************
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Submit">
        </form>
    """

    widget = EmailRepeatWidget

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        fields = (
            forms.EmailField(max_length=max_length, min_length=min_length),
            forms.EmailField(max_length=max_length, min_length=min_length),
        )
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return data_list[0]
        return None

    def clean(self, value):
        super().clean(value)
        if value[0] != value[1]:
            raise ValidationError(_("Emails must match."), code="invalid")
        return value[0]
