from captcha.fields import CaptchaField

from django_registration.forms import RegistrationForm


class CaptchaRegistrationForm(RegistrationForm):
    """Captcha registration form."""

    captcha = CaptchaField()
