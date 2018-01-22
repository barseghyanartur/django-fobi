from .base import *

FOBI_DEFAULT_THEME = 'foundation5'

INSTALLED_APPS = list(INSTALLED_APPS)

INSTALLED_APPS.append(
    'fobi.contrib.themes.foundation5.widgets.form_elements.date_foundation5_widget'  # NOQA
)
INSTALLED_APPS.append(
    'fobi.contrib.themes.foundation5.widgets.form_elements.datetime_foundation5_widget'  # NOQA
)
