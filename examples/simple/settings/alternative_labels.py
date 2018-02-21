import os
from .base import *

LOCALE_PATHS = [
    os.path.abspath(os.path.join(BASE_DIR, 'fobi_locale')),
    os.path.abspath(os.path.join(BASE_DIR, 'locale')),
]
FOBI_SORT_PLUGINS_BY_VALUE = True
