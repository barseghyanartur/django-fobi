from django import forms


class MyForm(forms.Form):
    """Test form."""

    number = forms.IntegerField(max_value=200)
