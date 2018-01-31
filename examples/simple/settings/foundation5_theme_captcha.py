from .base import *

FOBI_DEFAULT_THEME = 'foundation5'

INSTALLED_APPS = list(INSTALLED_APPS)

INSTALLED_APPS.append(
    'fobi.contrib.themes.foundation5.widgets.form_elements.date_foundation5_widget'  # NOQA
)
INSTALLED_APPS.append(
    'fobi.contrib.themes.foundation5.widgets.form_elements.datetime_foundation5_widget'  # NOQA
)

try:
    if 'captcha' not in INSTALLED_APPS:
        INSTALLED_APPS.append('captcha')

    if 'fobi.contrib.plugins.form_elements.security.captcha' \
            not in INSTALLED_APPS:
        INSTALLED_APPS.append(
            'fobi.contrib.plugins.form_elements.security.captcha'
        )

    CAPTCHA_TEXT_FIELD_TEMPLATE = 'foundation5/captcha/text_field.html'

    ENABLE_CAPTCHA = True

except Exception as e:
    pass
