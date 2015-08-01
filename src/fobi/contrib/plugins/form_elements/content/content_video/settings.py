__title__ = 'fobi.contrib.plugins.form_elements.content.content_video.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'SIZES', 'SIZE_400x300', 'SIZE_500x400', 'DEFAULT_SIZE',
)

from .conf import get_setting

SIZE_400x300 = get_setting('SIZE_400x300')
SIZE_500x400 = get_setting('SIZE_500x400')
DEFAULT_SIZE = get_setting('DEFAULT_SIZE')
SIZES = get_setting('SIZES')
