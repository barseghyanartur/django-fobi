"""
- ``DEFAULT_SIZE`` (string)
- ``SIZE_100x100`` (string)
- ``SIZE_200x200`` (string)
- ``SIZE_300x300`` (string)
- ``SIZE_400x400`` (string)
- ``SIZE_500x500`` (string)
- ``SIZE_600x600`` (tuple)
- ``SIZES`` (list)
"""

from .conf import get_setting

__title__ = 'fobi.contrib.plugins.form_elements.content.content_image_url.' \
            'settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'DEFAULT_SIZE',
    'SIZE_100x100',
    'SIZE_200x200',
    'SIZE_300x300',
    'SIZE_400x400',
    'SIZE_500x500',
    'SIZE_600x600',
    'SIZES',
)


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
