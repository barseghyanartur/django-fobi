from .conf import get_setting

__title__ = 'fobi.contrib.plugins.form_elements.fields.slider.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'INITIAL',
    'MAX_VALUE',
    'MIN_VALUE',
    'STEP',
)

INITIAL = get_setting('INITIAL')

MAX_VALUE = get_setting('MAX_VALUE')

MIN_VALUE = get_setting('MIN_VALUE')

STEP = get_setting('STEP')
