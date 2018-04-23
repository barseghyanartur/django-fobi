"""
Helpers module. This module can be safely imported from any fobi (sub)module,
since it never imports from any of the fobi (sub)modules (except for the
`fobi.constants` and `fobi.exceptions` modules).
"""
from __future__ import unicode_literals
import glob
import logging
import os
import shutil
import uuid

from autoslug.settings import slugify

from django import forms
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
# from django.contrib.contenttypes.models import ContentType
from django.core.files.base import File
# from django.db.utils import DatabaseError
from django.http import HttpResponse
from django.templatetags.static import static
from django.test.client import RequestFactory
from django.utils.encoding import force_text, smart_text
from django.utils.html import format_html_join
from django.utils.translation import ugettext_lazy as _

from nine.user import User
from nine.versions import DJANGO_GTE_1_8, DJANGO_GTE_1_10

# import simplejson as json

from six import text_type, PY3

from .constants import (
    SUBMIT_VALUE_AS_MIX,
    SUBMIT_VALUE_AS_REPR,
    SUBMIT_VALUE_AS_VAL,
)
from .exceptions import ImproperlyConfigured

if DJANGO_GTE_1_8:
    import django.apps
else:
    from django.db import models

if DJANGO_GTE_1_10:
    from django.urls import reverse
else:
    from django.core.urlresolvers import reverse

__title__ = 'fobi.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'admin_change_url',
    'clean_dict',
    'clone_file',
    'combine_dicts',
    'delete_file',
    'do_slugify',
    'empty_string',
    'ensure_unique_filename',
    'flatatt_inverse_quotes',
    'get_app_label_and_model_name',
    'get_form_element_entries_for_form_wizard_entry',
    'get_ignorable_form_values',
    'get_model_name_for_object',
    'get_registered_models',
    'get_select_field_choices',
    'get_wizard_form_field_value_from_post',
    'get_wizard_form_field_value_from_request',
    'get_wizard_form_field_value_from_session',
    'handle_uploaded_file',
    'iterable_to_dict',
    'JSONDataExporter',
    'lists_overlap',
    'map_field_name_to_label',
    'safe_text',
    'StrippedRequest',
    'StrippedUser',
    'two_dicts_to_string',
    'uniquify_sequence',
    'update_plugin_data',
    'validate_initial_for_choices',
    'validate_initial_for_multiple_choices',
    'validate_submit_value_as',
)

logger = logging.getLogger(__name__)

# DEBUG = not True

# *****************************************************************************
# *****************************************************************************
# ********************************** General **********************************
# *****************************************************************************
# *****************************************************************************


def do_slugify(val):
    """Slugify."""
    return slugify(val.lower()).lower()


def safe_text(text):
    """Safe text (encode).

    :return str:
    """
    return smart_text(text)
    # if PY3:
    #     return force_text(text, encoding='utf-8')
    # else:
    #     return force_text(text, encoding='utf-8').encode('utf-8')


def lists_overlap(sub, main):
    """Check whether lists overlap."""
    for i in sub:
        if i in main:
            return True
    return False


def iterable_to_dict(items, key_attr_name):
    """Converts iterable of certain objects to dict.

    :param iterable items:
    :param string key_attr_name: Attribute to use as a dictionary key.
    :return dict:
    """
    items_dict = {}
    for item in items:
        items_dict.update({getattr(item, key_attr_name): item})
    return items_dict


def map_field_name_to_label(form):
    """Takes a form and creates label to field name map.

    :param django.forms.Form form: Instance of ``django.forms.Form``.
    :return dict:
    """
    return dict([(field_name, field.label)
                 for (field_name, field)
                 in form.base_fields.items()])


def clean_dict(source, keys=[], values=[]):
    """Removes given keys and values from dictionary.

    :param dict source:
    :param iterable keys:
    :param iterable values:
    :return dict:
    """
    dict_data = {}
    for key, value in source.items():
        if (key not in keys) and (value not in values):
            dict_data[key] = value
    return dict_data


def combine_dicts(headers, data):
    """Combine dicts.

    Takes two dictionaries, assuming one contains a mapping keys to titles
    and another keys to data. Joins as string and returns a result dict.
    """
    return [(value, data.get(key, '')) for key, value in list(headers.items())]


def two_dicts_to_string(headers, data, html_element='p'):
    """Two dicts to string.

    Takes two dictionaries, assuming one contains a mapping keys to titles
    and another keys to data. Joins as string and returns wrapped into
    HTML "p" tag.
    """
    formatted_data = [
        (value, data.get(key, '')) for key, value in list(headers.items())
    ]
    return "".join(
        ["<{0}>{1}: {2}</{3}>".format(html_element, safe_text(key),
                                      safe_text(value), html_element)
         for key, value in formatted_data]
    )


empty_string = text_type('')


def absolute_path(path):
    """
    Given a relative or absolute path to a static asset, return an absolute
    path. An absolute path will be returned unchanged while a relative path
    will be passed to django.templatetags.static.static().
    """
    if path.startswith(('http://', 'https://', '/')):
        return path
    return static(path)


def uniquify_sequence(sequence):
    """Uniqify sequence.

    Makes sure items in the given sequence are unique, having the original
    order preserved.

    :param iterable sequence:
    :return list:
    """
    seen = set()
    seen_add = seen.add
    return [absolute_path(x)
            for x in sequence if x not in seen and not seen_add(x)]


def get_ignorable_form_values():
    """Get ignorable for form values.

    Gets an iterable of form values to ignore.

    :return iterable:
    """
    return [None, empty_string]


def get_model_name_for_object(obj):
    """Get model name for object.

    Django version agnostic."""
    return obj._meta.model_name

# *****************************************************************************
# *****************************************************************************
# ****************************** File helpers *********************************
# *****************************************************************************
# *****************************************************************************


def ensure_unique_filename(destination):
    """Makes sure filenames are never overwritten.

    :param string destination:
    :return string:
    """
    if os.path.exists(destination):
        filename, extension = os.path.splitext(destination)
        return "{0}_{1}{2}".format(filename, uuid.uuid4(), extension)
    else:
        return destination


def handle_uploaded_file(upload_dir, image_file):
    """Handle uploaded files.

    :param django.core.files.uploadedfile.InMemoryUploadedFile image_file:
    :return string: Path to the image (relative).
    """
    upload_dir_absolute_path = os.path.join(settings.MEDIA_ROOT, upload_dir)

    # Create path if doesn't exist yet
    if not os.path.exists(upload_dir_absolute_path):
        os.makedirs(upload_dir_absolute_path)

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
    """Delete file from disc."""
    try:
        # Delete the main file.
        file_path = os.path.join(settings.MEDIA_ROOT, image_file)
        os.remove(file_path)

        # Delete the sized version of it.
        files = glob.glob("{0}*".format(file_path))
        for __f in files:
            try:
                os.remove(__f)
            except Exception as err:
                logger.debug(str(err))

        # If all goes well...
        return True
    except Exception as err:
        logger.debug(str(err))
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
    except Exception as err:
        logger.debug(str(err))


def extract_file_path(name):
    """Extracts the file path.

    :param string name:
    :return string:
    """
    return os.path.join(settings.MEDIA_ROOT, name)

# *****************************************************************************
# *****************************************************************************
# ****************************** Model helpers ********************************
# *****************************************************************************
# *****************************************************************************


def get_registered_models(ignore=[]):
    """Gets registered models as list.

    :param iterable ignore: Ignore the following content types (should
        be in ``app_label.model`` format (example ``auth.User``).
    :return list:
    """
    get_models = django.apps.apps.get_models
    # if DJANGO_GTE_1_7:
    #     get_models = django.apps.apps.get_models
    # else:
    #     def get_models():
    #         """Get models."""
    #         return models.get_models(include_auto_created=True)

    registered_models = [
        (
            "{0}.{1}".format(_m._meta.app_label, _m._meta.model_name),
            _m._meta.object_name
        )
        for _m
        in get_models()
    ]

    # registered_models = []
    # try:
    #     content_types = ContentType._default_manager.all()
    #
    #     for content_type in content_types:
    #         # model = content_type.model_class()
    #         content_type_id = "{0}.{1}".format(
    #             content_type.app_label, content_type.model
    #         )
    #         if content_type_id not in ignore:
    #             registered_models.append(
    #                 (content_type_id, content_type.name)
    #             )
    # except DatabaseError as err:
    #     logger.debug(str(err))

    return registered_models


def get_app_label_and_model_name(path):
    """Gets app_label and model_name from the path given.

    :param str path: Dotted path to the model (without ".model", as stored
        in the Django `ContentType` model.
    :return tuple: app_label, model_name
    """
    parts = path.split('.')
    return (''.join(parts[:-1]), parts[-1])

# *****************************************************************************
# *****************************************************************************
# ****************************** Admin helpers ********************************
# *****************************************************************************
# *****************************************************************************


def admin_change_url(app_label, module_name, object_id, extra_path='',
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
        url = reverse('admin:{0}_{1}_change'.format(app_label, module_name),
                      args=[object_id]) + extra_path
        if url_title:
            return u'<a href="{0}">{1}</a>'.format(url, url_title)
        else:
            return url
    except Exception:
        return None

# *****************************************************************************
# *****************************************************************************
# ****************************** Fobi data helpers ****************************
# *****************************************************************************
# *****************************************************************************


def update_plugin_data(entry, request=None):
    """Update plugin data.

    Update plugin data of a given entry.
    """
    if entry:
        plugin = entry.get_plugin(request=request)
        logger.debug(plugin)
        if plugin:
            return plugin._update_plugin_data(entry)


def get_select_field_choices(raw_choices_data,
                             key_type=None,
                             value_type=None,
                             fail_silently=True):
    """Get select field choices.

    Used in ``radio``, ``select`` and other choice based
    fields.

    :param str raw_choices_data:
    :param type key_type:
    :param type value_type:
    :param bool fail_silently:
    :return list:
    """
    choices = []  # Holds return value
    keys = set([])  # For checking uniqueness of keys
    values = set([])  # For checking uniqueness of values

    # Looping through the raw data
    for choice in raw_choices_data.split('\n'):
        choice = choice.strip()

        # If comma separated key, value
        if ',' in choice:
            key, value = choice.split(',', 1)
            key = key.strip()

            # If type specified, cast to the type
            if key_type and key is not None:
                try:
                    key = key_type(key)
                except (ValueError, TypeError):
                    return [] if fail_silently else None

            value = value.strip()
            # If type specified, cast to the type
            if value_type and value is not None:
                try:
                    value = value_type(value)
                except (ValueError, TypeError):
                    return [] if fail_silently else None

            if key is not None \
                    and key not in keys \
                    and value not in values:
                choices.append((key, value))
                keys.add(key)
                values.add(value)

        # If key is also the value
        else:
            choice = choice.strip()
            if choice is not None \
                    and choice not in keys \
                    and choice not in values:
                choices.append((choice, choice))
                keys.add(choice)
                values.add(choice)

    return choices


def validate_initial_for_choices(plugin_form, field_name_choices='choices',
                                 field_name_initial='initial'):
    """Validate init for choices.
    Validates the initial value for the choices given.

    :param fobi.base.BaseFormFieldPluginForm plugin_form:
    :param str field_name_choices:
    :param str field_name_initial:
    :return str:
    """
    available_choices = dict(
        get_select_field_choices(plugin_form.cleaned_data[field_name_choices])
    ).keys()

    if plugin_form.cleaned_data[field_name_initial] \
       and not plugin_form.cleaned_data[field_name_initial] \
       in available_choices:
        raise forms.ValidationError(
            _("Invalid value for initial: {0}. Should be any of the following"
              ": {1}".format(plugin_form.cleaned_data[field_name_initial],
                             ','.join(available_choices)))
        )

    return plugin_form.cleaned_data[field_name_initial]


def validate_initial_for_multiple_choices(plugin_form,
                                          field_name_choices='choices',
                                          field_name_initial='initial'):
    """Validates the initial value for the multiple choices given.

    :param fobi.base.BaseFormFieldPluginForm plugin_form:
    :param str field_name_choices:
    :param str field_name_initial:
    :return str:
    """
    available_choices = dict(
        get_select_field_choices(
            plugin_form.cleaned_data[field_name_choices]
        )
    ).keys()

    if plugin_form.cleaned_data[field_name_initial]:
        for choice in plugin_form.cleaned_data[field_name_initial].split(','):
            choice = choice.strip()
            if choice not in available_choices:
                raise forms.ValidationError(
                    _("Invalid value for initial: {0}. Should be any "
                      "of the following: {1}"
                      "".format(choice, ','.join(available_choices)))
                )

    return plugin_form.cleaned_data[field_name_initial]


def validate_submit_value_as(value):
    """Validates the `SUBMIT_AS_VALUE`.

    :param str value:
    """
    if value not in (SUBMIT_VALUE_AS_VAL, SUBMIT_VALUE_AS_REPR,
                     SUBMIT_VALUE_AS_MIX):
        raise ImproperlyConfigured("The `SUBMIT_AS_VALUE` may have one of "
                                   "the following values: {0}, {1} or {2}"
                                   "".format(SUBMIT_VALUE_AS_VAL,
                                             SUBMIT_VALUE_AS_REPR,
                                             SUBMIT_VALUE_AS_MIX))


class StrippedUser(object):
    """Stripped user object."""

    def __init__(self, user):
        """Constructor.

        :param user:
        :return:
        """
        self._user = user
        if DJANGO_GTE_1_10:
            user_is_anonymous = self._user.is_anonymous
        else:
            user_is_anonymous = self._user.is_anonymous()
        if not user_is_anonymous:
            setattr(self._user, User.USERNAME_FIELD, self._user.get_username())
        else:
            setattr(self._user, User.USERNAME_FIELD, None)

    @property
    def email(self):
        """Email."""
        return self._user.email

    def get_username(self):
        """Get username."""
        if DJANGO_GTE_1_10:
            user_is_anonymous = self._user.is_anonymous
        else:
            user_is_anonymous = self._user.is_anonymous()
        if not user_is_anonymous:
            try:
                return self._user.get_username()
            except Exception as err:
                pass

    def get_full_name(self):
        """Get full name."""
        if DJANGO_GTE_1_10:
            user_is_anonymous = self._user.is_anonymous
        else:
            user_is_anonymous = self._user.is_anonymous()
        if not user_is_anonymous:
            try:
                return self._user.get_full_name()
            except Exception as err:
                pass

    def get_short_name(self):
        """Get short name."""
        if DJANGO_GTE_1_10:
            user_is_anonymous = self._user.is_anonymous
        else:
            user_is_anonymous = self._user.is_anonymous()
        if not user_is_anonymous():
            try:
                return self._user.get_full_name()
            except Exception as err:
                pass

    def is_anonymous(self):
        """Is anonymous."""
        if DJANGO_GTE_1_10:
            return self._user.is_anonymous
        else:
            return self._user.is_anonymous()


class StrippedRequest(object):
    """Stripped request object."""

    def __init__(self, request):
        """Constructor.

        :param django.http.HttpRequest request:
        :return:
        """
        # Just to make sure nothing breaks if we don't provide the request
        # object, we do fall back to a fake request object.
        if request:
            self._request = request
        else:
            request_factory = RequestFactory()
            self._request = request_factory.get('/')

        if hasattr(request, 'user') and request.user:
            self.user = StrippedUser(self._request.user)
        else:
            self.user = StrippedUser(AnonymousUser())

    @property
    def path(self):
        """Path.

        A string representing the full path to the requested page, not
        including the scheme or domain.
        """
        return self._request.path

    def get_full_path(self):
        """Returns the path, plus an appended query string, if applicable."""
        return self._request.get_full_path()

    def is_secure(self):
        """Is secure.

        Returns True if the request is secure; that is, if it was made with
        HTTPS.
        """
        return self._request.is_secure()

    def is_ajax(self):
        """Is ajax?

        Returns True if the request was made via an XMLHttpRequest, by
        checking the HTTP_X_REQUESTED_WITH header for the string
        'XMLHttpRequest'.
        """
        return self._request.is_ajax()

    @property
    def META(self):
        """Request meta stripped down.

        A standard Python dictionary containing all available HTTP
        headers. Available headers depend on the client and server, but here
        are some examples:

            - HTTP_ACCEPT_ENCODING: Acceptable encodings for the response.
            - HTTP_ACCEPT_LANGUAGE: Acceptable languages for the response.
            - HTTP_HOST: The HTTP Host header sent by the client.
            - HTTP_REFERER: The referring page, if any.
            - HTTP_USER_AGENT: The clients user-agent string.
            - QUERY_STRING: The query string, as a single (unparsed) string.
            - REMOTE_ADDR: The IP address of the client.
        """
        _meta = {
            'HTTP_ACCEPT_ENCODING': self._request.META.get(
                'HTTP_ACCEPT_ENCODING'
            ),
            'HTTP_ACCEPT_LANGUAGE': self._request.META.get(
                'HTTP_ACCEPT_LANGUAGE'
            ),
            'HTTP_HOST': self._request.META.get('HTTP_HOST'),
            'HTTP_REFERER': self._request.META.get('HTTP_REFERER'),
            'HTTP_USER_AGENT': self._request.META.get('HTTP_USER_AGENT'),
            'QUERY_STRING': self._request.META.get('QUERY_STRING'),
            'REMOTE_ADDR': self._request.META.get('REMOTE_ADDR'),
        }
        return _meta

# *****************************************************************************
# *****************************************************************************
# ******************************** Export related *****************************
# *****************************************************************************
# *****************************************************************************


class JSONDataExporter(object):
    """Exporting the data into JSON."""

    def __init__(self, data, filename):
        """Constructor.

        :param str data: Dumped JSON data (`json.dumps()`).
        :param str filename: File name prefix.
        """
        self.data = data
        self.filename = filename

    def _get_initial_response(self, mimetype="application/json"):
        """Get initial response.

        For compatibility with older versions (`mimetype` vs `content_type`).

        :param str mimetype:
        :return django.http.HttpResponse:
        """
        response_kwargs = {'content_type': mimetype}
        # response_kwargs = {}
        # if DJANGO_GTE_1_7:
        #     response_kwargs['content_type'] = mimetype
        # else:
        #     response_kwargs['mimetype'] = mimetype
        return HttpResponse(**response_kwargs)

    def export_to_json(self):
        """Export data to JSON."""
        response = self._get_initial_response(mimetype="text/json")
        response['Content-Disposition'] = \
            'attachment; filename={0}.json'.format(self.filename)

        response.write(self.data)
        return response

    def export(self):
        """Export."""
        return self.export_to_json()


def get_form_element_entries_for_form_wizard_entry(form_wizard_entry):
    """Get form element entries for the form wizard entry."""
    form_element_entries = []
    # TODO: Perhaps add select related here?
    for form_wizard_form_entry \
            in form_wizard_entry.formwizardformentry_set.all():
        form_element_entries += form_wizard_form_entry \
                                    .form_entry \
                                    .formelemententry_set.all()[:]
    return form_element_entries


def get_wizard_form_field_value_from_session(request,
                                             wizard_view_name,
                                             form_key,
                                             field_name,
                                             fail_silently=True):
    """Get wizard form field value from session.

    This is what we could have:

        >>> request.session['wizard_form_wizard_view']['step_data']
        >>> {
        >>>     'slider-form': {
        >>>         'csrfmiddlewaretoken': ['DhINThGTgQ50e2lDnGG4nYrG0a'],
        >>>         'slider-form-test_slider': ['14'],
        >>>         'form_wizard_view-current_step': ['slider-form'],
        >>>         'slider-form-test_email': ['user@example.com']
        >>>     }
        >>> }

    Note, that we know nothing about the types here, type conversion should
    be done manually. The values returned are strings always.

    :param django.http.HttpRequest request:
    :param str wizard_view_name:
    :param str form_key: Typically, this would be the step name (form slug).
    :param str field_name: Field name.
    :param bool fail_silently: If set to True, no errors raised.
    :return str: Since everything in session is stored as string.
    """
    # Field name in the session contains the form key
    session_field_name = "{0}-{1}".format(form_key, field_name)

    if not fail_silently:

        return request.session[wizard_view_name]['step_data'][form_key][
            session_field_name][0]

    else:

        try:
            return request.session[wizard_view_name]['step_data'][form_key][
                session_field_name][0]
        except (KeyError, IndexError) as err:
            logger.error(err)
            return None


def get_wizard_form_field_value_from_post(request,
                                          wizard_view_name,
                                          form_key,
                                          field_name,
                                          fail_silently=True):
    """Get wizard form field value from POST.

    This is what we could have:

    >>> request.POST
    >>> {
    >>>     'csrfmiddlewaretoken': ['kEprTL218a8HNcC02QefNNnF'],
    >>>     'slider-form-test_slider': ['14'],
    >>>     'form_wizard_view-current_step': ['slider-form'],
    >>>     'slider-form-test_email': ['user@example.com']
    >>> }

    Note, that we know nothing about the types here, type conversion should
    be done manually. The values returned are strings always.

    :param django.http.HttpRequest request:
    :param str wizard_view_name:
    :param str form_key: Typically, this would be the step name (form slug).
    :param str field_name: Field name.
    :param bool fail_silently: If set to True, no errors raised.
    :return str: Since everything in session is stored as string.
    """
    # Field name in the POST contains the form key
    form_field_name = "{0}-{1}".format(form_key, field_name)
    # current_step_name = "{0}-{1}".format(wizard_view_name, form_key)

    if not fail_silently:

        # if not (current_step_name in request.POST and
        #         request.POST[current_step_name] == form_key):
        #     return None
        return request.POST[form_field_name]

    else:

        try:
            # if not (current_step_name in request.POST and
            #         request.POST[current_step_name] == form_key):
            #     return None

            return request.POST[form_field_name]
        except (KeyError, IndexError) as err:
            logger.error(err)
            return None


def get_wizard_form_field_value_from_request(request,
                                             wizard_view_name,
                                             form_key,
                                             field_name,
                                             fail_silently=True,
                                             session_priority=False):
    """Get wizard form field value from request.

    Note, that we know nothing about the types here, type conversion should
    be done manually. The values returned are strings always.

    :param django.http.HttpRequest request:
    :param str wizard_view_name:
    :param str form_key: Typically, this would be the step name (form slug).
    :param str field_name: Field name.
    :param bool fail_silently: If set to True, no errors raised.
    :param bool session_priority: If set to True, first try to read from
        session.
    :return str: Since everything in session is stored as string.
    """
    if session_priority:
        # First try session
        value = get_wizard_form_field_value_from_session(
            request,
            wizard_view_name,
            form_key,
            field_name,
            fail_silently
        )

        if value is not None:
            return value

        # Then try POST
        if request.method == 'POST':
            value = get_wizard_form_field_value_from_post(
                request,
                wizard_view_name,
                form_key,
                field_name,
                fail_silently
            )

    else:
        # First try POST
        if request.method == 'POST':
            value = get_wizard_form_field_value_from_post(
                request,
                wizard_view_name,
                form_key,
                field_name,
                fail_silently
            )

            if value is not None:
                return value

        # Then try session
        value = get_wizard_form_field_value_from_session(
            request,
            wizard_view_name,
            form_key,
            field_name,
            fail_silently
        )

    return value

# *****************************************************************************
# *****************************************************************************
# ******************************** Export related *****************************
# *****************************************************************************
# *****************************************************************************


def flatatt_inverse_quotes(attrs):
    """Convert a dictionary of attributes to a single string.

    The returned string will contain a leading space followed by key="value",
    XML-style pairs. In the case of a boolean value, the key will appear
    without a value. It is assumed that the keys do not need to be
    XML-escaped. If the passed dictionary is empty, then return an empty
    string.

    The result is passed through 'mark_safe' (by way of 'format_html_join').
    """
    key_value_attrs = []
    boolean_attrs = []
    for attr, value in attrs.items():
        if isinstance(value, bool):
            if value:
                boolean_attrs.append((attr,))
        else:
            key_value_attrs.append((attr, value))

    return (
        format_html_join("", " {}='{}'", sorted(key_value_attrs)) +
        format_html_join("", " {}", sorted(boolean_attrs))
    )
