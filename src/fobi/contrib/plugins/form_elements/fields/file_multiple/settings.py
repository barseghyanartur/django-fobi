"""
- ``FILE_MULTIPLE_UPLOAD_DIR`` (string)
"""
from .conf import get_setting

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2023 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = ("FILE_MULTIPLE_UPLOAD_DIR",)

FILE_MULTIPLE_UPLOAD_DIR = get_setting("FILE_MULTIPLE_UPLOAD_DIR")
