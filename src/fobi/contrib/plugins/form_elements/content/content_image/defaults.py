from django.utils.translation import ugettext_lazy as _

__title__ = 'fobi.contrib.plugins.form_elements.content.content_image.defaults'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
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

FIT_METHOD_CROP_SMART = 'smart'
FIT_METHOD_CROP_CENTER = 'center'
FIT_METHOD_CROP_SCALE = 'scale'
FIT_METHOD_FIT_WIDTH = 'fit_width'
FIT_METHOD_FIT_HEIGHT = 'fit_height'

DEFAULT_FIT_METHOD = FIT_METHOD_CROP_CENTER

FIT_METHODS_CHOICES = (
    (FIT_METHOD_CROP_SMART, _("Smart crop")),
    (FIT_METHOD_CROP_CENTER, _("Crop center")),
    (FIT_METHOD_CROP_SCALE, _("Crop scale")),
    (FIT_METHOD_FIT_WIDTH, _("Fit width")),
    (FIT_METHOD_FIT_HEIGHT, _("Fit height")),
)

FIT_METHODS_CHOICES_WITH_EMPTY_OPTION = [('', '---------')] + \
                                        list(FIT_METHODS_CHOICES)

SIZE_100x100 = '100x100'
SIZE_200x200 = '200x200'
SIZE_200x300 = '200x300'
SIZE_300x200 = '300x200'
SIZE_300x300 = '300x300'
SIZE_300x400 = '300x400'
SIZE_400x300 = '400x300'
SIZE_400x400 = '400x400'
SIZE_500x500 = '500x500'
SIZE_600x600 = '600x600'

DEFAULT_SIZE = SIZE_500x500

SIZES = (
    (SIZE_100x100, SIZE_100x100),
    (SIZE_200x200, SIZE_200x200),
    (SIZE_200x300, SIZE_200x300),
    (SIZE_300x200, SIZE_300x200),
    (SIZE_300x300, SIZE_300x300),
    (SIZE_300x400, SIZE_300x400),
    (SIZE_400x300, SIZE_400x300),
    (SIZE_400x400, SIZE_400x400),
    (SIZE_500x500, SIZE_500x500),
    (SIZE_600x600, SIZE_600x600),
)

IMAGES_UPLOAD_DIR = 'fobi_plugins/content_image'
