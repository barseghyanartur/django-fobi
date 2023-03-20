from __future__ import absolute_import

__title__ = "fobi.contrib.plugins.form_handlers.mail_sender"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2019 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = (
    "default_app_config",
    "UID",
)

if django.VERSION < (3, 2): # pragma: no cover
    default_app_config = (
        "fobi.contrib.plugins.form_handlers.mail_sender.apps." "Config"
    )

UID = "mail_sender"
