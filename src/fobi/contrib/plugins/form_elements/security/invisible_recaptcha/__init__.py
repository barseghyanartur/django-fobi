__title__ = "fobi.contrib.plugins.form_elements.security.invisible_recaptcha"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2019 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = (
    "default_app_config",
    "UID",
)
if django.VERSION < (3, 2): # pragma: no cover
    default_app_config = (
        "fobi.contrib.plugins.form_elements.security."
        "invisible_recaptcha.apps.Config"
    )

UID = "invisible_recaptcha"
