from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:
    INSTALLED_APPS.remove(
        "admin_tools"
    ) if "admin_tools" in INSTALLED_APPS else None
    INSTALLED_APPS.remove(
        "admin_tools.menu"
    ) if "admin_tools.menu" in INSTALLED_APPS else None
    INSTALLED_APPS.remove(
        "admin_tools.dashboard"
    ) if "admin_tools.dashboard" in INSTALLED_APPS else None
except Exception as err:
    pass

FOBI_DEFAULT_THEME = "bootstrap5"