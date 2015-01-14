__title__ = 'fobi.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'do_slugify', 'lists_overlap', 'iterable_to_dict', 'map_field_name_to_label',
    'clean_dict', 'two_dicts_to_string', 'empty_string', 'ensure_unique_filename',
    'handle_uploaded_file', 'delete_file', 'clone_file', 'get_registered_models',
    'admin_change_url', 'uniquify_sequence', 'safe_text', 'combine_dicts',
    'update_plugin_data', 'get_select_field_choices',
)

import os
import glob
import logging
import uuid
import shutil

from six import text_type, PY3

from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.files.base import File
from django.contrib.contenttypes.models import ContentType
from django.db.utils import DatabaseError
from django.utils.encoding import force_text

from autoslug.settings import slugify

logger = logging.getLogger(__name__)

# *****************************************************************************
# *****************************************************************************
# ********************************** General **********************************
# *****************************************************************************
# *****************************************************************************

do_slugify = lambda s: slugify(s.lower()).lower()

def safe_text(text):
    """
    Safe text (encode).

    :return str:
    """
    if PY3:
        return force_text(text, encoding='utf-8')
    else:
        return force_text(text, encoding='utf-8').encode('utf-8')

def lists_overlap(sub, main):
    for i in sub:
        if i in main:
            return True
    return False

def iterable_to_dict(items, key_attr_name):
    """
    Converts iterable of certain objects to dict.

    :param iterable items:
    :param string key_attr_name: Attribute to use as a dictionary key.
    :return dict:
    """
    items_dict = {}
    for item in items:
        items_dict.update({getattr(item, key_attr_name): item})
    return items_dict

def map_field_name_to_label(form):
    """
    Takes a form and creates label to field name map.

    :param django.forms.Form form: Instance of ``django.forms.Form``.
    :param list keys_to_remove:
    :return dict:
    """
    return dict([(field_name, field.label) for (field_name, field) in form.base_fields.items()])

def clean_dict(source, keys=[], values=[]):
    """
    Removes given keys and values from dictionary.

    :param dict source:
    :param iterable keys:
    :param iterable values:
    :return dict:
    """
    d = {}
    for key, value in source.items():
        if (not key in keys) and (not value in values):
            d[key] = value
    return d

def combine_dicts(headers, data):
    """
    Takes two dictionaries, assuming one contains a mapping keys to titles
    and another keys to data. Joins as string and returns a result dict.
    """
    return [(value, data.get(key, '')) for key, value in list(headers.items())]

def two_dicts_to_string(headers, data, html_element='p'):
    """
    Takes two dictionaries, assuming one contains a mapping keys to titles 
    and another keys to data. Joins as string and returns wrapped into
    HTML "p" tag.
    """
    formatted_data = [
        (value, data.get(key, '')) for key, value in list(headers.items())
        ]
    return "".join(
        ["<{0}>{1}: {2}</{3}>".format(html_element, safe_text(key), safe_text(value), html_element) \
        for key, value in formatted_data]
        )

empty_string = text_type('')

def uniquify_sequence(sequence):
    """
    Makes sure items in the given sequence are unique, having the original order preserved.

    :param iterable sequence:
    :return list:
    """
    seen = set()
    seen_add = seen.add
    return [x for x in sequence if x not in seen and not seen_add(x)]

def get_ignorable_form_values():
    """
    Gets an iterable of form values to ignore.

    :return iterable:
    """
    return [None, empty_string,]

# *****************************************************************************
# *****************************************************************************
# ****************************** File helpers *********************************
# *****************************************************************************
# *****************************************************************************

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

def handle_uploaded_file(upload_dir, image_file):
    """
    :param django.core.files.uploadedfile.InMemoryUploadedFile image_file:
    :return string: Path to the image (relative).
    """
    upload_dir_absolute_path = os.path.join(settings.MEDIA_ROOT, upload_dir)

    if isinstance(image_file, File):
        destination_path = ensure_unique_filename(
            os.path.join(upload_dir_absolute_path, image_file.name)
            )
        image_filename = image_file.name
        with open(destination_path, 'wb+') as destination:
            image_filename = os.path.basename(destination.name)
            for chunk in image_file.chunks():
                destination.write(chunk)
        return os.path.join(upload_dir, image_filename)
    return image_file

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

def clone_file(upload_dir, source_filename, relative_path=True):
    """
    Clones the file.

    :param string source_filename: Source filename.
    :return string: Filename of the cloned file.
    """
    if source_filename.startswith(upload_dir):
        source_filename = os.path.join(settings.MEDIA_ROOT, source_filename)

    destination_filename = ensure_unique_filename(source_filename)
    try:
        shutil.copyfile(source_filename, destination_filename)
        if relative_path:
            destination_filename = destination_filename.replace(
                settings.MEDIA_ROOT, ''
                )
            if destination_filename.startswith('/'):
                destination_filename = destination_filename[1:]
        return destination_filename
    except Exception as e:
        logger.debug(str(e))

# *****************************************************************************
# *****************************************************************************
# ****************************** Model helpers ********************************
# *****************************************************************************
# *****************************************************************************

def get_registered_models(ignore=[]):
    """
    Gets registered models as list.

    :param iterable ignore: Ignore the following content types (should
        be in ``app_label.model`` format (example ``auth.User``).
    :return list:
    """
    registered_models = []
    try:
        content_types = ContentType._default_manager.all()

        for content_type in content_types:
            #model = content_type.model_class()
            content_type_id = "{0}.{1}".format(
                content_type.app_label, content_type.model
                )
            if not content_type_id in ignore:
                registered_models.append((content_type_id, content_type.name))
    except DatabaseError as e:
        logger.debug(str(e))

    return registered_models

# *****************************************************************************
# *****************************************************************************
# ****************************** Admin helpers ********************************
# *****************************************************************************
# *****************************************************************************

def admin_change_url(app_label, module_name, object_id, extra_path='', \
                     url_title=None):
    """
    Gets an admin change URL for the object given.

    :param str app_label:
    :param str module_name:
    :param int object_id:
    :param str extra_path:
    :param str url_title: If given, an HTML a tag is returned with `url_title`
        as the tag title. If left to None just the URL string is returned.
    :return str:
    """
    try:
        url = reverse('admin:%s_%s_change' %(app_label, module_name), args=[object_id]) + extra_path
        if url_title:
            return u'<a href="%s">%s</a>' %(url, url_title)
        else:
            return url
    except:
        return None

# *****************************************************************************
# *****************************************************************************
# ****************************** Fobi data helpers ****************************
# *****************************************************************************
# *****************************************************************************

def update_plugin_data(entry, request=None):
    """
    Update plugin data of a given entry.
    """
    if entry:
        plugin = entry.get_plugin(request=request)
        logger.debug(plugin)
        if plugin:
            return plugin._update_plugin_data(entry)

def get_select_field_choices(raw_choices_data):
    """
    Used in ``radio``, ``select`` and other choice based
    fields.

    :param str raw_choices_data:
    :return list:
    """
    choices = []
    keys = set([])
    for choice in raw_choices_data.split('\n'):
        choice = choice.strip()
        if ',' in choice:
            key, value = choice.split(',', 1)
            key = key.strip()
            value = value.strip()
            if not key in keys:
                choices.append((key, value))
                keys.add(key)
        else:
            choice = choice.strip()
            if not choice in keys:
                choices.append((choice, choice))
                keys.add(choice)
    return choices
