from .conf import get_setting

__title__ = 'fobi.contrib.plugins.form_elements.content.content_text.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'ALLOWED_TAGS',
    'ALLOWED_ATTRIBUTES',
)

ALLOWED_TAGS = get_setting('ALLOWED_TAGS')
ALLOWED_ATTRIBUTES = get_setting('ALLOWED_ATTRIBUTES')
