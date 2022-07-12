from captcha.fields import CaptchaField
from django_nine.versions import DJANGO_GTE_3_0

if DJANGO_GTE_3_0:
    from django_registration.forms import RegistrationForm
else:
    from registration.forms import RegistrationForm


class CaptchaRegistrationForm(RegistrationForm):
    """Captcha registration form."""

    captcha = CaptchaField()
