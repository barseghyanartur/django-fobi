from django.forms.widgets import CheckboxInput


class InvisibleRecaptchaWidget(CheckboxInput):
    """Invisible recaptcha widget."""

    def __init__(self, *args, **kwargs):
        attrs = kwargs.get('attrs', {})
        attrs.update({'data-customforms': 'disabled'})
        super(InvisibleRecaptchaWidget, self).__init__(*args, **kwargs)

