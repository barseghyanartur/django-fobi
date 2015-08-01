__title__ = 'fobi.contrib.plugins.form_elements.content.content_image.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'handle_uploaded_file', 'get_crop_filter', 'delete_file',
    'ensure_unique_filename', 'clone_file'
)

import os
import glob
import logging
import uuid
import shutil

from django.conf import settings
from django.core.files.base import File

from .settings import (
    IMAGES_UPLOAD_DIR, FIT_METHOD_CROP_SMART, FIT_METHOD_CROP_CENTER,
    FIT_METHOD_CROP_SCALE
    )

logger = logging.getLogger(__file__)

IMAGES_UPLOAD_DIR_ABSOLUTE_PATH = os.path.join(settings.MEDIA_ROOT, IMAGES_UPLOAD_DIR)

def ensure_unique_filename(destination):
    """
    Makes sure filenames are never overwritten.

    :param string destination:
    :return string:
    """
    if os.path.exists(destination):
        filename, extension = os.path.splitext(destination)
        return "{0}_{1}{2}".format(filename, uuid.uuid4(), extension)
    else:
        return destination

def handle_uploaded_file(image_file):
    """
    :param django.core.files.uploadedfile.InMemoryUploadedFile image_file:
    :return string: Path to the image (relative).
    """
    if isinstance(image_file, File):
        destination_path = ensure_unique_filename(os.path.join(IMAGES_UPLOAD_DIR_ABSOLUTE_PATH, image_file.name))
        image_filename = image_file.name
        with open(destination_path, 'wb+') as destination:
            image_filename = os.path.basename(destination.name)
            for chunk in image_file.chunks():
                destination.write(chunk)
        return os.path.join(IMAGES_UPLOAD_DIR, image_filename)
    return image_file

def get_crop_filter(fit_method):
    if fit_method in (FIT_METHOD_CROP_SMART, FIT_METHOD_CROP_CENTER, FIT_METHOD_CROP_SCALE):
        return fit_method

def delete_file(image_file):
    """
    Delete file from disc.
    """
    try:
        # Delete the main file.
        file_path = os.path.join(settings.MEDIA_ROOT, image_file)
        os.remove(file_path)

        # Delete the sized version of it.
        files = glob.glob("{0}*".format(file_path))
        for f in files:
            try:
                os.remove(f)
            except Exception as e:
                logger.debug(str(e))

        # If all goes well...
        return True
    except Exception as e:
        logger.debug(str(e))
        return False

def clone_file(source_filename, relative_path=True):
    """
    Clones the file.

    :param string source_filename: Source filename.
    :return string: Filename of the cloned file.
    """
    if source_filename.startswith(IMAGES_UPLOAD_DIR):
        source_filename = os.path.join(settings.MEDIA_ROOT, source_filename)

    destination_filename = ensure_unique_filename(source_filename)
    try:
        shutil.copyfile(source_filename, destination_filename)
        if relative_path:
            destination_filename = destination_filename.replace(settings.MEDIA_ROOT, '')
            if destination_filename.startswith('/'):
                destination_filename = destination_filename[1:]
        return destination_filename
    except Exception as e:
        logger.debug(str(e))
