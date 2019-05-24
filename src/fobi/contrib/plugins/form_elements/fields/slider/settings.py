from .conf import get_setting

__title__ = 'fobi.contrib.plugins.form_elements.fields.slider.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'INITIAL',
    'INITIAL_MAX_VALUE',
    'INITIAL_MIN_VALUE',
    'MAX_VALUE',
    'MIN_VALUE',
    'STEP',
)

INITIAL = get_setting('INITIAL')

INITIAL_MAX_VALUE = get_setting('INITIAL_MAX_VALUE')

INITIAL_MIN_VALUE = get_setting('INITIAL_MIN_VALUE')

MAX_VALUE = get_setting('MAX_VALUE')

MIN_VALUE = get_setting('MIN_VALUE')

STEP = get_setting('STEP')
