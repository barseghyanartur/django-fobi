from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)

if not 'captcha' in INSTALLED_APPS:
    INSTALLED_APPS.append('captcha')

if not 'fobi.contrib.plugins.form_elements.security.recaptcha' \
       in INSTALLED_APPS:
    INSTALLED_APPS.append(
        'fobi.contrib.plugins.form_elements.security.recaptcha'
    )

# Test keys are taken from official dedicated Google page
# https://developers.google.com/recaptcha/docs/faq#id-like-to-run-automated-tests-with-recaptcha.-what-should-i-do
RECAPTCHA_PUBLIC_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
RECAPTCHA_PRIVATE_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'
RECAPTCHA_USE_SSL = True
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
# FOBI_DEFAULT_THEME = 'simple'
