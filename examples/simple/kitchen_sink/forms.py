from django import forms


class KitchenSinkForm(forms.Form):
    choices = forms.MultipleChoiceField(
        choices=[
            ("a", "A"),
            ("b", "B"),
            ("c", "C"),
        ],
        widget=forms.CheckboxSelectMultiple,
    )
