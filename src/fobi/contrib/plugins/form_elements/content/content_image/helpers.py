import logging
import os

from django.conf import settings

from .settings import (
    IMAGES_UPLOAD_DIR, FIT_METHOD_CROP_SMART, FIT_METHOD_CROP_CENTER,
    FIT_METHOD_CROP_SCALE
)

__title__ = 'fobi.contrib.plugins.form_elements.content.content_image.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('get_crop_filter',)

logger = logging.getLogger(__file__)

IMAGES_UPLOAD_DIR_ABSOLUTE_PATH = os.path.join(settings.MEDIA_ROOT,
                                               IMAGES_UPLOAD_DIR)


def get_crop_filter(fit_method):
    """Get crop filter."""
    if fit_method in (FIT_METHOD_CROP_SMART, FIT_METHOD_CROP_CENTER,
                      FIT_METHOD_CROP_SCALE):
        return fit_method
