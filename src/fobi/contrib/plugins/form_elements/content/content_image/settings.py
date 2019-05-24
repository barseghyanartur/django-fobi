"""
- ``FIT_METHOD_CROP_SMART`` (string)
- ``FIT_METHOD_CROP_CENTER`` (string)
- ``FIT_METHOD_CROP_SCALE`` (string)
- ``FIT_METHOD_FIT_WIDTH`` (string)
- ``FIT_METHOD_FIT_HEIGHT`` (string)
- ``DEFAULT_FIT_METHOD`` (string)
- ``FIT_METHODS_CHOICES`` (tuple)
- ``FIT_METHODS_CHOICES_WITH_EMPTY_OPTION`` (list)
- ``IMAGES_UPLOAD_DIR`` (string)
"""

from .conf import get_setting

__title__ = 'fobi.contrib.plugins.form_elements.content.content_image.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'DEFAULT_FIT_METHOD',
    'DEFAULT_SIZE',
    'FIT_METHOD_CROP_CENTER',
    'FIT_METHOD_CROP_SCALE',
    'FIT_METHOD_CROP_SMART',
    'FIT_METHOD_FIT_HEIGHT',
    'FIT_METHOD_FIT_WIDTH',
    'FIT_METHODS_CHOICES',
    'FIT_METHODS_CHOICES_WITH_EMPTY_OPTION',
    'IMAGES_UPLOAD_DIR',
    'SIZE_100x100',
    'SIZE_200x200',
    'SIZE_300x300',
    'SIZE_400x400',
    'SIZE_500x500',
    'SIZE_600x600',
    'SIZES',
)


FIT_METHOD_CROP_SMART = get_setting('FIT_METHOD_CROP_SMART')
FIT_METHOD_CROP_CENTER = get_setting('FIT_METHOD_CROP_CENTER')
FIT_METHOD_CROP_SCALE = get_setting('FIT_METHOD_CROP_SCALE')
FIT_METHOD_FIT_WIDTH = get_setting('FIT_METHOD_FIT_WIDTH')
FIT_METHOD_FIT_HEIGHT = get_setting('FIT_METHOD_FIT_HEIGHT')
DEFAULT_FIT_METHOD = get_setting('DEFAULT_FIT_METHOD')
FIT_METHODS_CHOICES = get_setting('FIT_METHODS_CHOICES')
FIT_METHODS_CHOICES_WITH_EMPTY_OPTION = \
    get_setting('FIT_METHODS_CHOICES_WITH_EMPTY_OPTION')
SIZE_100x100 = get_setting('SIZE_100x100')
SIZE_200x200 = get_setting('SIZE_200x200')
SIZE_300x300 = get_setting('SIZE_300x300')
SIZE_400x400 = get_setting('SIZE_400x400')
SIZE_500x500 = get_setting('SIZE_500x500')
SIZE_600x600 = get_setting('SIZE_600x600')
DEFAULT_SIZE = get_setting('DEFAULT_SIZE')
SIZES = get_setting('SIZES')
IMAGES_UPLOAD_DIR = get_setting('IMAGES_UPLOAD_DIR')
