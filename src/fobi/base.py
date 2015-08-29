"""
All `uids` are supposed to be pythonic function names (see
PEP http://www.python.org/dev/peps/pep-0008/#function-names).
"""

__title__ = 'fobi.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'BaseDataStorage', 'FormElementPluginDataStorage',
    'FormHandlerPluginDataStorage', 'BasePluginForm', 'BasePlugin',
    'FormElementPlugin', 'FormHandlerPlugin', 'FormCallback', 'BaseRegistry',
    'FormElementPluginRegistry', 'FormHandlerPluginRegistry',
    'FormCallbackRegistry', 'ClassProperty', 'classproperty',
    'form_element_plugin_registry', 'form_handler_plugin_registry',
    'form_callback_registry', 'get_registered_plugins',
    'get_registered_plugin_uids', 'get_registered_form_element_plugins',
    'get_registered_form_element_plugin_uids',
    'validate_form_element_plugin_uid', 'get_registered_form_handler_plugins',
    'get_registered_form_handler_plugin_uids',
    'validate_form_handler_plugin_uid', 'get_registered_form_callbacks',
    'fire_form_callbacks', 'run_form_handlers', 'ensure_autodiscover',
    'collect_plugin_media', 'theme_registry', 'get_registered_themes',
    'get_registered_theme_uids', 'validate_theme_uid',
    'BaseFormFieldPluginForm', 'FormFieldPlugin',
    'form_element_plugin_widget_registry',
    'form_handler_plugin_widget_registry', 'FormElementPluginWidgetRegistry',
    'FormHandlerPluginWidgetRegistry', 'FormElementPluginWidget',
    'FormHandlerPluginWidget', 'get_ordered_form_handlers',
    'assemble_form_field_widget_class', 'get_plugin_widget',
    'get_form_element_plugin_widget', 'get_form_handler_plugin_widget'
    )

import traceback
import logging
import copy
import uuid
#import json
import re

import simplejson as json

try:
    from collections import OrderedDict
except ImportError as e:
    from ordereddict import OrderedDict

from six import with_metaclass, string_types

from django import forms
from django.forms import ModelForm
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.template import RequestContext, Template, Context

from nine.versions import DJANGO_GTE_1_8

if DJANGO_GTE_1_8:
    from django.forms.utils import ErrorList
else:
    from django.forms.util import ErrorList

from fobi.discover import autodiscover
from fobi.constants import CALLBACK_STAGES
from fobi.settings import (
    DEFAULT_THEME, FORM_HANDLER_PLUGINS_EXECUTION_ORDER,
    CUSTOM_THEME_DATA, THEME_FOOTER_TEXT, FAIL_ON_MISSING_FORM_ELEMENT_PLUGINS,
    FAIL_ON_MISSING_FORM_HANDLER_PLUGINS, DEBUG,
    #FAIL_ON_ERRORS_IN_FORM_ELEMENT_PLUGINS,
    FAIL_ON_ERRORS_IN_FORM_HANDLER_PLUGINS
)
from fobi.exceptions import (
    InvalidRegistryItemType, DoesNotExist, ThemeDoesNotExist,
    FormElementPluginDoesNotExist, FormHandlerPluginDoesNotExist
)
from fobi.helpers import (
    uniquify_sequence, map_field_name_to_label, clean_dict,
    map_field_name_to_label, get_ignorable_form_values, safe_text,
    StrippedRequest,
)
from fobi.data_structures import SortableDict

logger = logging.getLogger(__name__)

_ = lambda s: s

# *****************************************************************************
# *****************************************************************************
# ********************************** Theme ************************************
# *****************************************************************************
# *****************************************************************************

class BaseTheme(object):
    """
    Base theme.

    :property str view_embed_form_entry_ajax_template: A template to be used
        when integrating the form rendering from other products (for example,
        a CMS page, which has a widget which references the form object. If
        that property is left empty, the ``view_form_entry_ajax_template``
        is used.
    :property str embed_form_entry_submitted_ajax_template: A template to be
        used when integrating into other products (CMS page). Serves the
        thank you.
    """
    uid = None
    name = None
    description = None
    html_classes = []
    media_css = []
    media_js = []

    # General HTML specific
    project_name = _("Build your forms") # Project name
    footer_text = '' # '&copy; Company 2014'

    # *************************************************************************
    # ********************** Form HTML specific *******************************
    # *************************************************************************
    # Used in almost all ``fobi_form_elements`` modules and forms.
    form_element_html_class = '' #form-control

    # Radio element HTML class. Used in ``fobi_form_elements`` modules
    # and forms.
    form_radio_element_html_class = ''

    # Checkbox element HTML class. Used in ``fobi_form_elements`` modules
    # and forms.
    form_element_checkbox_html_class = '' # checkbox

    # Important, since used in ``edit_form_entry_edit_option_html``
    # method.
    form_edit_form_entry_option_class = '' #glyphicon glyphicon-edit

    # Important, since used in ``edit_form_entry_edit_option_html``
    # method.
    form_delete_form_entry_option_class = '' #glyphicon glyphicon-remove

    # Important, since used in ``edit_form_entry_help_text_extra``
    # method.
    form_list_container_class = '' #list-inline

    # *************************************************************************
    # ********************** Templates specific *******************************
    # *************************************************************************
    master_base_template = 'fobi/generic/_base.html'
    base_template = 'fobi/generic/base.html'
    base_view_template = None
    base_edit_template = None
    form_snippet_template_name = 'fobi/generic/snippets/form_snippet.html'
    form_view_snippet_template_name = None
    form_edit_snippet_template_name = None
    form_properties_snippet_template_name = \
        'fobi/generic/snippets/form_properties_snippet.html'
    messages_snippet_template_name = \
        'fobi/generic/snippets/messages_snippet.html'
    form_non_field_and_hidden_errors_snippet_template = \
        'fobi/generic/snippets/form_non_field_and_hidden_errors_snippet.html'

    form_ajax = 'fobi/generic/snippets/form_ajax.html'
    form_view_ajax = None
    form_edit_ajax = None
    add_form_element_entry_template = 'fobi/generic/add_form_element_entry.html'
    add_form_element_entry_ajax_template = \
        'fobi/generic/add_form_element_entry_ajax.html'
    add_form_handler_entry_template = 'fobi/generic/add_form_handler_entry.html'
    add_form_handler_entry_ajax_template = \
        'fobi/generic/add_form_handler_entry_ajax.html'
    create_form_entry_template = 'fobi/generic/create_form_entry.html'
    create_form_entry_ajax_template = 'fobi/generic/create_form_entry_ajax.html'
    dashboard_template = 'fobi/generic/dashboard.html'
    edit_form_element_entry_template = \
        'fobi/generic/edit_form_element_entry.html'
    edit_form_element_entry_ajax_template = \
        'fobi/generic/edit_form_element_entry_ajax.html'
    edit_form_entry_template = 'fobi/generic/edit_form_entry.html'
    edit_form_entry_ajax_template = 'fobi/generic/edit_form_entry_ajax.html'
    edit_form_handler_entry_template = \
        'fobi/generic/edit_form_handler_entry.html'
    edit_form_handler_entry_ajax_template = \
        'fobi/generic/edit_form_handler_entry_ajax.html'
    form_entry_submitted_template = 'fobi/generic/form_entry_submitted.html'
    form_entry_submitted_ajax_template = \
        'fobi/generic/form_entry_submitted_ajax.html'
    embed_form_entry_submitted_ajax_template = None
    view_form_entry_template = 'fobi/generic/view_form_entry.html'
    view_form_entry_ajax_template = 'fobi/generic/view_form_entry_ajax.html'
    view_embed_form_entry_ajax_template = None

    import_form_entry_template = 'fobi/generic/import_form_entry.html'
    import_form_entry_ajax_template = 'fobi/generic/import_form_entry_ajax.html'

    # *************************************************************************
    # ******************** Extras that make things easy ***********************
    # *************************************************************************
    custom_data = {}

    page_header_html_class = '' #page-header
    form_html_class = '' #form-horizontal
    form_button_outer_wrapper_html_class = '' #control-group
    form_button_wrapper_html_class = '' #controls
    form_button_html_class = '' #btn
    form_primary_button_html_class = '' #btn-primary

    def __init__(self, user=None):
        """
        :param django.contrib.auth.models.User user:
        """
        assert self.uid
        assert self.name
        #assert self.view_template_name
        #assert self.edit_template_name
        assert isinstance(self.media_js, (list, tuple))
        assert isinstance(self.media_css, (list, tuple))

        if isinstance(self.media_js, tuple):
            self.media_js = list(self.media_js)

        if isinstance(self.media_css, tuple):
            self.media_css = list(self.media_css)

        self.user = user

        self.plugin_media_js = []
        self.plugin_media_css = []

        if not self.form_radio_element_html_class:
            self.form_radio_element_html_class = self.form_element_html_class

        # If no specific base view template specified, fall back
        # to the base template.
        if not self.base_view_template:
            self.base_view_template = self.base_template

        # If no specific base edit template specified, fall back
        # to the base template.
        if not self.base_edit_template:
            self.base_edit_template = self.base_template

        # If no specific ``form_view_snippet_template_name`` specified, fall
        # back to the ``form_snippet_template_name``.
        if not self.form_view_snippet_template_name:
            self.form_view_snippet_template_name = \
                self.form_snippet_template_name

        # If no specific ``form_edit_snippet_template_name`` specified, fall
        # back to the ``form_snippet_template_name``.
        if not self.form_edit_snippet_template_name:
            self.form_edit_snippet_template_name = \
                self.form_snippet_template_name

        # If no specific ``form_view_ajax`` specified, fall
        # back to the ``form_ajax``.
        if not self.form_view_ajax:
            self.form_view_ajax = self.form_ajax

        # If no specific ``form_edit_ajax`` specified, fall
        # back to the ``form_ajax``.
        if not self.form_edit_ajax:
            self.form_edit_ajax = self.form_ajax

        # If no specific ``view_embed_form_entry_ajax_template`` specified, 
        # fall back to the ``view_form_entry_ajax_template``.
        if not self.view_embed_form_entry_ajax_template:
            self.view_embed_form_entry_ajax_template = \
                self.view_form_entry_ajax_template

        # Some sort of a embed thank you.
        if not self.embed_form_entry_submitted_ajax_template:
            self.embed_form_entry_submitted_ajax_template = \
                self.form_entry_submitted_ajax_template

        # Set theme specific data from settings for to be
        # refered like `fobi_theme.custom_data`.
        self.custom_data = self.get_custom_data()

        # Set the footer text from settings if not specified
        # in the theme.
        if not self.footer_text:
            self.footer_text = self.get_footer_text()

    def _get_custom_data(self):
        """
        Internal method for obtaining the custom data from settings.

        :return dict:
        """
        if self.uid in CUSTOM_THEME_DATA:
            return CUSTOM_THEME_DATA[self.uid]
        return {}

    def get_custom_data(self):
        """
        Fills the theme with custom data from settings.

        :return dict:
        """
        return self._get_custom_data()

    def _get_footer_text(self):
        """
        Internal method for returning the footer text from settings.

        :return str:
        """
        return _(THEME_FOOTER_TEXT)

    def get_footer_text(self):
        """
        Returns the footer text from settings.

        :return str:
        """
        return self._get_footer_text()

    @classmethod
    def edit_form_entry_edit_option_html(cls):
        """
        For adding the edit link to edit form entry view.

        :return str:
        """
        return """
            <li><a href="{edit_url}">
              <span class="{edit_option_class}"></span> {edit_text}</a>
            </li>
            """.format(
                edit_url = "{edit_url}",
                edit_option_class = cls.form_edit_form_entry_option_class,
                edit_text = "{edit_text}",
                )

    @classmethod
    def edit_form_entry_help_text_extra(cls):
        """
        For adding the edit link to edit form entry view.

        :return str:
        """
        return """
            <ul class="{container_class}">
              {edit_option_html}
              <li><a href="{delete_url}">
                <span class="{delete_option_class}"></span> {delete_text}</a>
              </li>
            </ul>
            <input type="hidden" value="{form_element_position}"
                   name="form-{counter}-position"
                   id="id_form-{counter}-position"
                   class="form-element-position">
            <input type="hidden" value="{form_element_pk}"
                   name="form-{counter}-id" id="id_form-{counter}-id">
            """.format(
                container_class = cls.form_list_container_class,
                edit_option_html = "{edit_option_html}",
                delete_url = "{delete_url}",
                delete_option_class = cls.form_delete_form_entry_option_class,
                delete_text = "{delete_text}",
                form_element_position = "{form_element_position}",
                counter = "{counter}",
                form_element_pk = "{form_element_pk}",
                )

    def get_view_template_name(self, request=None, origin=None):
        """
        Gets the view template name.

        :param django.http.HttpRequest request:
        :param string origin: Origin of the request. Hook to provide custom
            templates for apps. Example value: 'public_dashboard'. Take the
            `public_dashboard` app as example.
        """
        if not self.view_template_name_ajax:
            return self.view_template_name
        elif request and request.is_ajax():
            return self.view_template_name_ajax
        else:
            return self.view_template_name

    def get_edit_template_name(self, request=None):
        if not self.edit_template_name_ajax:
            return self.edit_template_name
        elif request and request.is_ajax():
            return self.edit_template_name_ajax
        else:
            return self.edit_template_name

    def collect_plugin_media(self, form_element_entries, request=None):
        """
        Collects the widget media files.

        :param iterable form_element_entries: Iterable of
            ``fobi.models.FormElementEntry`` instances.
        :param django.http.HttpRequest request:
        :return list:
        """
        plugin_media = collect_plugin_media(
            form_element_entries,
            request = request
            )

        if plugin_media:
            self.plugin_media_js = plugin_media['js']
            self.plugin_media_css = plugin_media['css']

    def get_media_css(self):
        """
        Gets all CSS media files (for the layout + plugins).

        :return list:
        """
        media_css = self.media_css[:]
        if self.plugin_media_css:
            media_css += self.plugin_media_css

        media_css = uniquify_sequence(media_css)

        return media_css

    def get_media_js(self):
        """
        Gets all JavaScript media files (for the layout + plugins).

        :return list:
        """
        media_js = self.media_js[:]
        if self.plugin_media_js:
            media_js += self.plugin_media_js

        media_js = uniquify_sequence(media_js)

        return media_js

    @property
    def primary_html_class(self):
        return 'theme-{0}'.format(self.uid)

    @property
    def html_class(self):
        """
        Class used in the HTML.

        :return string:
        """
        return '{0} {1}'.format(
            self.primary_html_class, ' '.join(self.html_classes)
            )

# *****************************************************************************
# *****************************************************************************
# ******************************** Plugins forms ******************************
# *****************************************************************************
# *****************************************************************************

class BasePluginForm(object):
    """
    Not a form actually. Defined for magic only.

    :property iterable plugin_data_fields: Fields to get when calling the
        ``get_plugin_data`` method. These field will be JSON serialized. All
        other fields, even if they are part of the form, won't be. Make sure
        all fields are serializable. If some of them aren't, override the
        ``save_plugin_data`` method and make them serializable there. See
        `fobi.contrib.plugins.form_elements.fields.select.forms` as a good
        example.

    :example:

        >>> plugin_data_fields = (
        >>>    ('name', ''),
        >>>    ('active': False)
        >>> )
    """
    plugin_data_fields = None

    def _get_plugin_data(self, fields, request=None, json_format=True):
        """
        Gets plugin data.

        :param iterable fields: List of tuples to iterate.
        :param django.http.HttpRequest request:
        :return string: JSON dumpled string.
        """
        data = {}

        for field, default_value in fields:
            data.update({field: self.cleaned_data.get(field)})

        if not json_format:
            return data

        return json.dumps(data)

    def get_plugin_data(self, request=None, json_format=True):
        """
        Data that would be saved in the ``plugin_data`` field of the
        ``fobi.models.FormElementEntry`` or ``fobi.models.FormHandlerEntry`.`
        subclassed model.

        :param django.http.HttpRequest request:
        """
        if self.plugin_data_fields:
            return self._get_plugin_data(self.plugin_data_fields,
                                         request=request,
                                         json_format=json_format)

    def save_plugin_data(self, request=None):
        """
        Dummy, but necessary.
        """

    def validate_plugin_data(self, form_element_entries, request=None):
        """
        :param iterable form_element_entries: Iterable of
            ``fobi.models.FormElementEntry``.
        :param django.http.HttpRequest request:
        :return bool:
        """
        return True


class BaseFormFieldPluginForm(BasePluginForm):
    """
    Base form for form field plugins.
    """
    plugin_data_fields = [
        ("name", ""),
        ("label", ""),
        ("help_text", ""),
        ("required", False)
    ]

    name = forms.CharField(
        label = _("Name"),
        required = True,
        #widget = forms.widgets.TextInput(attrs={})
        )
    label = forms.CharField(
        label = _("Label"),
        required = True,
        #widget = forms.widgets.TextInput(attrs={})
        )
    help_text = forms.CharField(
        label = _("Help text"),
        required = False,
        widget = forms.widgets.Textarea(attrs={})
        )
    required = forms.BooleanField(
        label = _("Required"),
        required = False,
        #widget = forms.widgets.CheckboxInput(attrs={})
        )

    def validate_plugin_data(self, form_element_entries, request=None):
        """
        :param iterable form_element_entries: Iterable of
            ``fobi.models.FormElementEntry``.
        :param django.http.HttpRequest request:
        :return bool:
        """
        if not getattr(self, 'cleaned_data', None):
            self.full_clean()

        data = self.get_plugin_data(request=request, json_format=False)

        for form_element_entry in form_element_entries:
            plugin = form_element_entry.get_plugin(request=request)

            # Make sure field name is unique
            if plugin.data.name == data['name']:
                self._errors.update({'name': [_("Duplicate field name!")]})
                return False

            # Make sure field label is unique
            if hasattr(plugin.data, 'label') and \
               plugin.data.label == data['label']:

                self._errors.update({'label': [_("Duplicate label name!")]})
                return False

        return True

# *****************************************************************************
# *****************************************************************************
# ******************************** Plugins ************************************
# *****************************************************************************
# *****************************************************************************

class BaseDataStorage(object):
    """
    Base storage data.
    """


class FormElementPluginDataStorage(BaseDataStorage):
    """
    Storage for `FormField` data.
    """


class FormHandlerPluginDataStorage(BaseDataStorage):
    """
    Storage for `FormField` data.
    """


class FormElementPluginWidgetDataStorage(BaseDataStorage):
    """
    Storage for `FormField` data.
    """


class FormHandlerPluginWidgetDataStorage(BaseDataStorage):
    """
    Storage for `FormField` data.
    """


class BasePlugin(object):
    """
    Base form field from which every form field should inherit.

    :Properties:

        - `uid` (string): Plugin uid (obligatory). Example value: 'dummy',
            'wysiwyg', 'news'.
        - `name` (string): Plugin name (obligatory). Example value:
            'Dummy plugin', 'WYSIWYG', 'Latest news'.
        - `description` (string): Plugin decription (optional). Example
            value: 'Dummy plugin used just for testing'.
        - `help_text` (string): Plugin help text (optional). This text would
            be shown in ``fobi.views.add_form_plugin_entry`` and
            ``fobi.views.edit_form_plugin_entry`` views.
        - `form`: Plugin form (optional). A subclass of ``django.forms.Form``.
            Should be given in case plugin is configurable.
        - `add_form_template` (str) (optional): Add form template (optional).
            If given, overrides the
          `fobi.views.add_form_handler_entry` default template.
        - `edit_form_template` (string): Edit form template (optional). If
            given, overrides the `fobi.views.edit_form_handler_entry` default
            template.
        - `html_classes` (list): List of extra HTML classes for the plugin.
        - `group` (string): Plugin are grouped under the specified group.
            Override in your plugin if necessary.
    """
    uid = None
    name = None
    description = None
    help_text = None
    form = None
    widget = None
    media_js = []
    media_css = []
    add_form_template = None
    edit_form_template = None
    html_classes = []
    group = _("General")
    storage = None

    def __init__(self, user=None):
        """
        :param django.contrib.auth.models.User user: Plugin owner.
        """
        # Making sure all necessary properties are defined.
        try:
            assert self.uid
            assert self.name
            assert self.storage and issubclass(self.storage, BaseDataStorage)
        except Exception as e:
            raise NotImplementedError(
                "You should define `uid`, `name` and `storage` properties in "
                "your `{0}.{1}` class. {2}".format(
                    self.__class__.__module__, self.__class__.__name__, str(e)
                    )
                )
        self.user = user

        # Some initial values
        self.request = None

        self.data = self.storage()

        self._html_id = 'p{0}'.format(uuid.uuid4())

    @property
    def html_id(self):
        return self._html_id

    @property # Comment the @property if something goes wrong.
    def html_class(self):
        """
        A massive work on positioning the plugin and having it to be displayed
        in a given width is done here. We should be getting the plugin widget
        for the plugin given and based on its' properties (static!) as well as
        on plugin position (which we have from model), we can show the plugin
        with the exact class.
        """
        try:
            html_class = ['plugin-{0} {1}'.format(
                self.uid, ' '.join(self.html_classes)
                )]
            return ' '.join(html_class)
        except Exception as e:
            logger.debug(
                "Error in class {0}. Details: "
                "{1}".format(self.__class__.__name__, str(e))
                )

    def process(self, plugin_data=None, fetch_related_data=False):
        """
        Init plugin with data.
        """
        try:
            # Calling pre-processor.
            self.pre_processor()

            if plugin_data:
                try:
                    # Trying to load the plugin data to JSON.
                    plugin_data = json.loads(plugin_data)

                    # If a valid JSON object, feed it to our plugin and process 
                    # the data. The ``process_data`` method should be defined
                    # in your subclassed plugin class.
                    if plugin_data:
                        self.load_plugin_data(plugin_data)

                        self.process_plugin_data(
                            fetch_related_data = fetch_related_data
                            )
                except Exception as e:
                    logger.debug(
                        "Error in class {0}. Details: "
                        "{1}".format(self.__class__.__name__, str(e))
                        )

            # Calling the post processor.
            self.post_processor()

            return self
        except Exception as e:
            logger.debug(
                "Error in class {0}. Details: "
                "{1}".format(self.__class__.__name__, str(e))
                )

    def load_plugin_data(self, plugin_data):
        """
        Loads the plugin data saved in ``fobi.models.FormElementEntry``
        or ``fobi.models.FormHandlerEntry``. Plugin data is saved in JSON
        string.

        :param string plugin_data: JSON string with plugin data.
        """
        self.plugin_data = plugin_data

    def _process_plugin_data(self, fields, fetch_related_data=False):
        """
        Process the plugin data. Override if need customisations.

        Beware, this is not always called.
        """
        for field, default_value in fields:
            try:
                setattr(
                    self.data,
                    field,
                    self.plugin_data.get(field, default_value)
                    )
            except Exception as e:
                setattr(self.data, field, default_value)

    def process_plugin_data(self, fetch_related_data=False):
        """
        Processes the plugin data.
        """
        form = self.get_form()

        return self._process_plugin_data(
            form.plugin_data_fields,
            fetch_related_data = fetch_related_data
            )

    def _get_plugin_form_data(self, fields):
        """
        Gets plugin data.

        :param iterable fields: List of tuples to iterate.
        :return dict:
        """
        form_data = {}
        for field, default_value in fields:
            try:
                form_data.update(
                    {field: self.plugin_data.get(field, default_value)}
                    )
            except Exception as e:
                logger.debug(
                    "Error in class {0}. Details: "
                    "{1}".format(self.__class__.__name__, str(e))
                    )
        return form_data

    def get_plugin_form_data(self):
        """
        Fed as ``initial`` argument to the plugin form when initialising the
        instance for adding or editing the plugin. Override in your plugin
        class if you need customisations.
        """
        form = self.get_form()

        return self._get_plugin_form_data(form.plugin_data_fields)

    def get_instance(self):
        return None

    def get_form(self):
        """
        Get the plugin form class. Override this method in your subclassed
        ``fobi.base.BasePlugin`` class when you need your plugin setup to vary
        depending on the placeholder, workspace, user or request given. By
        default returns the value of the ``form`` attribute defined in your
        plugin.

        :return django.forms.Form|django.forms.ModelForm: Subclass of
            ``django.forms.Form`` or ``django.forms.ModelForm``.
        """
        return self.form

    def get_initialised_create_form(self, data=None, files=None,
                                    initial_data=None):
        """
        Used ``fobi.views.add_form_element_entry`` and
        ``fobi.views.add_form_handler_entry`` view to gets initialised form
        for object to be created.
        """
        plugin_form = self.get_form()
        if plugin_form:
            try:
                plugin_form = self.get_form()
                if plugin_form:
                    kwargs = {
                        'data': data,
                        'files': files,
                    }
                    if initial_data:
                        kwargs.update({'initial': initial_data})
                    return plugin_form(**kwargs)
            except Exception as e:
                if DEBUG:
                    logger.debug(e)
                raise Http404(e)

    def get_initialised_create_form_or_404(self, data=None, files=None):
        """
        Same as ``get_initialised_create_form`` but raises
        ``django.http.Http404`` on errors.
        """
        plugin_form = self.get_form()
        if plugin_form:
            initial_data = {}
            try:
                initial_data = dict(plugin_form.plugin_data_fields)
            except Exception as err:
                pass
            try:
                return self.get_initialised_create_form(
                    data = data,
                    files = files,
                    initial_data = initial_data
                    )
            except Exception as e:
                if DEBUG:
                    logger.debug(e)
                raise Http404(e)

    def get_initialised_edit_form(self, data=None, files=None,
                                  auto_id='id_%s', prefix=None, initial=None,
                                  error_class=ErrorList, label_suffix=':',
                                  empty_permitted=False, instance=None):
        """
        Used in ``fobi.views.edit_form_element_entry`` and
        ``fobi.views.edit_form_handler_entry`` views.
        """
        plugin_form = self.get_form()
        if plugin_form:
            kwargs = {
                'data': data,
                'files': files,
                'auto_id': auto_id,
                'prefix': prefix,
                'initial': initial,
                'error_class': error_class,
                'label_suffix': label_suffix,
                'empty_permitted': empty_permitted
            }
            if issubclass(plugin_form, ModelForm):
                kwargs.update({'instance': instance})
            return plugin_form(**kwargs)

    def get_initialised_edit_form_or_404(self, data=None, files=None,
                                         auto_id='id_%s', prefix=None,
                                         error_class=ErrorList,
                                         label_suffix=':',
                                         empty_permitted=False):
        """
        Same as ``get_initialised_edit_form`` but raises
        ``django.http.Http404`` on errors.
        """
        plugin_form = self.get_form()
        if plugin_form:
            try:
                return self.get_initialised_edit_form(
                    data = data,
                    files = files,
                    auto_id = auto_id,
                    prefix = prefix,
                    initial = self.get_plugin_form_data(),
                    error_class = error_class,
                    label_suffix = label_suffix,
                    empty_permitted = empty_permitted,
                    instance = self.get_instance()
                    )
            except Exception as e:
                if DEBUG:
                    logger.debug(e)
                raise Http404(e)

    def get_widget(self, request=None, as_instance=False):
        """
        Gets the plugin widget.

        :param django.http.HttpRequest request:
        :param bool as_instance:
        :return mixed: Subclass of `fobi.base.BasePluginWidget` or instance
            of subclassed `fobi.base.BasePluginWidget` object.
        """
        raise NotImplemented

    def render(self, request=None):
        """
        Renders the plugin HTML.

        :param django.http.HttpRequest request:
        :return string:
        """
        widget_cls = self.get_widget()

        if widget_cls:
            widget = widget_cls(self)

            render = widget.render(request=request)
            return render or ''
        elif DEBUG:
            logger.debug("No widget defined for {0}.".format(self.uid))

    def _update_plugin_data(self, entry):
        """
        For private use. Do not override this method. Override
        `update_plugin_data` instead.
        """
        try:
            updated_plugin_data = self.update_plugin_data(entry)
            plugin_data = self.get_updated_plugin_data(
                update = updated_plugin_data
                )
            return self.save_plugin_data(entry, plugin_data=plugin_data)
        except Exception as e:
            logging.debug(str(e))

    def update_plugin_data(self, entry):
        """
        Used in ``fobi.management.commands.fobi_update_plugin_data``.

        Some plugins would contain data fetched from various sources (models,
        remote data). Since form entries are by definition loaded extremely
        much, you are advised to store as much data as possible in
        ``plugin_data`` field of ``fobi.models.FormElementEntry`` or
        ``fobi.models.FormHandlerEntry``. Some externally fetched data becomes
        invalid after some time and needs updating. For that purpose, in case
        if your plugin needs that, redefine this method in your plugin. If
        you need your data to be periodically updated, add a cron-job which
        would run ``fobi_update_plugin_data`` management command (see
        ``fobi.management.commands.fobi_update_plugin_data`` module).

        :param fobi.models.FormElementEntry or fobi.models.FormHandlerEntry:
            Instance of ``fobi.models.FormeHandlerEntry``.
        :return dict: Should return a dictionary containing data of fields to
            be updated.
        """

    def _delete_plugin_data(self):
        """
        For private use. Do not override this method. Override
        `delete_plugin_data` instead.
        """
        try:
            self.delete_plugin_data()
        except Exception as e:
            logging.debug(str(e))

    def delete_plugin_data(self):
        """
        Used in ``fobi.views.delete_form_entry`` and
        ``fobi.views.delete_form_handler_entry``. Fired automatically, when
        ``fobi.models.FormEntry`` object is about to be deleted. Make use of
        it if your plugin creates database records or files that are not
        monitored externally but by dash only.
        """

    def _clone_plugin_data(self, entry):
        """
        For private use. Do not override this method. Override
        `clone_plugin_data` instead.
        """
        try:
            return self.clone_plugin_data(entry)
        except Exception as e:
            logging.debug(str(e))

    def clone_plugin_data(self, entry):
        """
        Used when copying entries. If any objects or files are created by
        plugin, they should be cloned.

        :param fobi.models.AbstractPluginEntry: Instance of
            ``fobi.models.AbstractPluginEntry``.
        :return string: JSON dumped string of the cloned plugin data. The
            returned value would be inserted as is into the
            `fobi.models.AbstractPluginEntry.plugin_data` field.
        """

    def get_cloned_plugin_data(self, update={}):
        """
        Get the cloned plugin data and returns it in a JSON dumped format.

        :param dict update:
        :return string: JSON dumped string of the cloned plugin data.

        :example:

        In the ``get_cloned_plugin_data`` method of your plugin, do as
            follows:

        >>> def clone_plugin_data(self, dashboard_entry):
        >>>     cloned_image = clone_file(self.data.image, relative_path=True)
        >>>     return self.get_cloned_plugin_data(
        >>>         update={'image': cloned_image}
        >>>         )
        """
        form = self.get_form()

        cloned_data = copy.copy(self.data)
        data = {}

        for field, default_value in form.plugin_data_fields:
            data.update({field: getattr(cloned_data, field, '')})

        for prop, value in update.items():
            data.update({prop: value})

        return json.dumps(data)

    def get_updated_plugin_data(self, update={}):
        """
        Get the plugin data and returns it in a JSON dumped format.

        :param dict update:
        :return string: JSON dumped string of the cloned plugin data.
        """
        form = self.get_form()
        data = {}

        for field, default_value in form.plugin_data_fields:
            data.update({field: getattr(self.data, field, '')})

        for prop, value in update.items():
            data.update({prop: value})

        return json.dumps(data)

    def pre_processor(self):
        """
        Redefine in your subclassed plugin when necessary.

        Pre process plugin data (before rendering). This method is being 
        called before the data has been loaded into the plugin.
        
        Note, that request (django.http.HttpRequest) is available (
        self.request).
        """

    def post_processor(self):
        """
        Redefine in your subclassed plugin when necessary.

        Post process plugin data here (before rendering). This methid is
        being called after the data has been loaded into the plugin.
        
        Note, that request (django.http.HttpRequest) is available
        (self.request).
        """

    def plugin_data_repr(self):
        """
        Human readable representation of plugin data. A very basic
        way would be just:

        >>> return self.data.__dict__

        :return string:
        """


class FormElementPlugin(BasePlugin):
    """
    Base form element plugin.

    :property fobi.base.FormElementPluginDataStorage storage:
    :property bool has_value: If set to False, ignored (removed)
        from the POST when processing the form.
    """
    storage = FormElementPluginDataStorage
    has_value = False
    is_hidden = False

    def _get_form_field_instances(self, form_element_entry=None, origin=None,
                                  kwargs_update_func=None, return_func=None,
                                  extra={}, request=None):
        """
        Used internally. Do not override this method. Gets the instances of
        form fields, that plugin contains.

        :param fobi.models.FormElementEntry form_element_entry: Instance.
        :param string origin:
        :param callable kwargs_update_func:
        :param callable return_func:
        :return list: List of Django form field instances.
        """
        # For the moment, this piece of code has to be present here.
        return_func_results = self.get_origin_return_func_results(
            return_func, form_element_entry, origin
            )
        if return_func_results:
            return return_func_results

        # Get form field instances (as defined by ``get_form_field_instances``
        # methods in plugins). In DEBUG mode raise an exception if something
        # goes wrong. Otherwise - skip the element.
        try:
            form_field_instances = self.get_form_field_instances()
        except AttributeError as e:
            if DEBUG:
                raise e
            else:
                return []

        processed_field_instances = []
        for field_name, Field, field_kwargs in form_field_instances:
            Widget = None
            if isinstance(Field, (list, tuple)):
                Field, Widget = Field

            # Consider using context for resolving some variables.
            # For instance, if user is logged in, ``request.user.username``
            # as an initial value should put the current users' username
            # as initial value in the form.
            if 'initial' in field_kwargs and field_kwargs['initial']:
                try:

                    # For security reasons we're not using the original request
                    # here.
                    stripped_request = StrippedRequest(request)
                    context = RequestContext(stripped_request)

                    # In order to be sure, that no accidental sensitive data
                    # is exposed in the forms, we only vales from the
                    # fobi specific context processor. By automatically
                    # force-prefixing all dynamic value definitions with
                    # "fobi_dynamic_values." string. See the docs for
                    # more ("Dyamic initial values" section).
                    initial = field_kwargs['initial']

                    # For the moment, only string types are dynamic
                    if isinstance(initial, string_types):
                        # Strip down the whitespaces we don't need.
                        initial = re.sub("{{\s+", "{{", initial)
                        initial = re.sub("\s+}}", "}}", initial)

                        # Prefix all {{ variable }} occurrences with
                        # "fobi_dynamic_values." so that there's no risk of
                        # exposing sensitive data. Further security of
                        # template context processor variables within
                        # "fobi_dynamic_values." is a developer responsibility.
                        initial = re.sub("{{", "{{fobi_dynamic_values.",
                                         initial)
                        # Strip loading or executing any complicated template
                        # tags.
                        initial = re.sub("{%.*%}", "", initial)

                        field_kwargs['initial'] = \
                            Template(initial).render(context)

                except Exception as err:
                    logger.debug(err)

            # Data to update field instance kwargs with
            kwargs_update = self.get_origin_kwargs_update_func_results(
                kwargs_update_func,
                form_element_entry,
                origin,
                extra = extra,
                widget_cls = Widget
                )

            #if 'widget' in field_kwargs:
            #    field_kwargs['widget'] = assemble_form_field_widget_class(
            #        base_class = field_kwargs['widget'],
            #        plugin = self
            #        )
            if kwargs_update:
                field_kwargs.update(kwargs_update)

            processed_field_instances.append(
                (field_name, Field(**field_kwargs))
                )

        return processed_field_instances

    def get_form_field_instances(self):
        """
        Gets the instances of form fields, that plugin contains.

        :param fobi.models.FormElementEntry form_element_entry: Instance.
        :param string origin:
        :param callable kwargs_update_func:
        :param callable return_func:
        :return list: List of Django form field instances.

        :example:
        >>> from django.forms.fields import CharField, IntegerField, TextField
        >>> [CharField(max_length=100), IntegerField(), TextField()]
        """
        return []

    def get_origin_return_func_results(self, return_func, form_element_entry, \
                                       origin):
        """
        If ``return_func`` is given, is callable and returns results without
        failures, return the result. Otherwise - return None.
        """
        # Check hooks
        if return_func and callable(return_func):
            try:
                return return_func(
                    form_element_plugin = self,
                    form_element_entry = form_element_entry,
                    origin = origin
                    )
            except Exception as e:
                pass

    def get_origin_kwargs_update_func_results(self, kwargs_update_func, \
                                              form_element_entry, origin, \
                                              extra={}, widget_cls=None):
        """
        If ``kwargs_update_func`` is given, is callable and returns results
        without failures, return the result. Otherwise - return None.
        """
        # Check hooks
        if kwargs_update_func and callable(kwargs_update_func):
            try:
                kwargs_update = kwargs_update_func(
                    form_element_plugin = self,
                    form_element_entry = form_element_entry,
                    origin = origin,
                    extra = extra,
                    widget_cls = widget_cls
                    )
                if kwargs_update:
                    return kwargs_update
            except Exception as e:
                logger.debug(str(e))
        return {}

    def _submit_plugin_form_data(self, form_entry, request, form):
        """
        Do not override this meathod. Use ``submit_plugin_form_data``,
        instead.

        Submit plugin form data. Called on form submittion (when user actually
        posts the data to assembed form).

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        """
        try:
            return self.submit_plugin_form_data(
                form_entry=form_entry, request=request, form=form
                )
        except Exception as e:
            logger.debug(str(e))

    def submit_plugin_form_data(self, form_entry, request, form):
        """
        Submit plugin form data. Called on form submittion (when user actually
        posts the data to assembed form).

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        """


class FormFieldPlugin(FormElementPlugin):
    """
    Form field plugin.
    """
    has_value = True


class FormHandlerPlugin(BasePlugin):
    """
    Form handler plugin.

    :property fobi.base.FormHandlerPluginDataStorage storage:
    :property bool allow_multiple: If set to True, plugin can be used multiple
        times within (per form). Otherwise - just once.
    """
    storage = FormHandlerPluginDataStorage
    allow_multiple = True

    def _run(self, form_entry, request, form, form_element_entries=None):
        """
        Safely call the ``run`` method.

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        :param iterable form_element_entries: Iterable of
            ``fobi.models.FormElementEntry`` objects.
        :return tuple:
        """
        # For backwards compatibility.
        if not form_element_entries:
            form_element_entries = form_entry.formelemententry_set.all()[:]

        try:
            response = self.run(form_entry, request, form, form_element_entries)
            if response:
                return response
            else:
                return (True, None)
        except Exception as err:
            if FAIL_ON_ERRORS_IN_FORM_HANDLER_PLUGINS:
                raise err.__class__("Exception: {0}. {1}"
                                    "".format(str(err), traceback.format_exc()))
            logger.error(
                "Error in class {0}. Details: "
                "{1}. Full trace: {2}".format(self.__class__.__name__, str(err),
                                              traceback.format_exc())
                )
            return (False, err)

    def run(self, form_entry, request, form, form_element_entries=None):
        """
        Custom code should be implemented here.

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        :param iterable form_element_entries: Iterable of
            ``fobi.models.FormElementEntry`` objects.
        :return mixed: May be a tuple (bool, mixed) or None
        """
        raise NotImplemented(
            "You should implement ``callback`` method in your {1} "
            "subclass.".format(self.__class__.__name__)
            )

    def custom_actions(self, form_entry, request=None):
        """
        Override this method in your form handler if you want to specify
        custom actions. Note, that expected return value of this method
        is an iterable with a triple, where the first item is the URL of
        the action and the second item is the action title and the third
        item is the icon class of the action.

        :example:
        >>>  return (
        >>>      ('/add-to-favorites/',
        >>>       'Add to favourites',
        >>>       'glyphicon glyphicon-favourties'),
        >>>  )
        """

    def get_custom_actions(self, form_entry, request=None):
        """
        Internal method to for obtaining the ``get_custom_actions``.
        """
        return self.custom_actions(form_entry, request)


class FormCallback(object):
    """
    Base form callback.
    """
    stage = None

    def __init__(self):
        """
        """
        assert self.stage in CALLBACK_STAGES

    def _callback(self, form_entry, request, form):
        """
        Callign the ``callback`` method in a safe way.
        """
        try:
            return self.callback(form_entry, request, form)
        except Exception as e:
            logger.debug(
                "Error in class {0}. Details: "
                "{1}".format(self.__class__.__name__, str(e))
                )

    def callback(self, form_entry, request, form):
        """
        Custom callback code should be implemented here.

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        """
        raise NotImplemented(
            "You should implement ``callback`` method in your {1} "
            "subclass.".format(self.__class__.__name__)
            )


class ClassProperty(property):
    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()
classproperty = ClassProperty


class BasePluginWidget(object):
    """
    Base form element plugin widget.

    So, if we would want to register a plugin widget (renderer) for some
    theme, we would first define the plugin widget and then just write:

    >>> form_element_plugin_widget_registry.register(DummyPluginWidget)

    Plugin widget is always being registered for a theme. Since we register
    each widget for a tuple (theme, plugin) combination separately, it makes
    us quite flexible in what's related to use of CSS and JavaScript per
    theme.
    """
    theme_uid = None
    plugin_uid = None
    html_classes = []
    media_js = []
    media_css = []
    storage = None

    def __init__(self, plugin):
        assert self.theme_uid
        assert self.plugin_uid and \
               self.plugin_uid in get_registered_plugin_uids()
        assert isinstance(self.media_js, (list, tuple))
        assert isinstance(self.media_css, (list, tuple))
        assert self.storage

        if isinstance(self.media_js, tuple):
            self.media_js = list(self.media_js)

        if isinstance(self.media_css, tuple):
            self.media_css = list(self.media_css)

        self.plugin = plugin

        self.data = self.storage()

    @classproperty
    def html_class(cls):
        """
        HTML class of the ``fobi.base.BaseFormElementPluginWidget``.

        :return string:
        """
        return ' '.join(cls.html_classes)


class FormElementPluginWidget(BasePluginWidget):
    """
    Form element plugin widget.
    """
    storage = FormElementPluginWidgetDataStorage


class FormHandlerPluginWidget(BasePluginWidget):
    """
    Form handler plugin widget.
    """
    storage = FormHandlerPluginWidgetDataStorage


# *****************************************************************************
# *****************************************************************************
# ******************************* Registry ************************************
# *****************************************************************************
# *****************************************************************************

class BaseRegistry(object):
    """
    Registry of dash plugins. It's essential, that class registered has the
    ``uid`` property.
    
    If ``fail_on_missing_plugin`` is set to True, an appropriate exception
    (``plugin_not_found_exception_cls``) is raised in cases if plugin cound't
    be found in the registry.

    :property mixed type:
    :property bool fail_on_missing_plugin:
    :property fobi.exceptions.DoesNotExist plugin_not_found_exception_cls:
    :property str plugin_not_found_error_message:
    """
    type = None
    fail_on_missing_plugin = False
    plugin_not_found_exception_cls = DoesNotExist
    plugin_not_found_error_message = "Can't find plugin with uid `{0}` in " \
                                     "`{1}` registry."

    def __init__(self):
        assert self.type
        self._registry = {}
        self._forced = []

    def register(self, cls, force=False):
        """
        Registers the plugin in the registry.

        :param mixed.
        """
        if not issubclass(cls, self.type):
            raise InvalidRegistryItemType(
                "Invalid item type `{0}` for registry "
                "`{1}`".format(cls, self.__class__)
                )

        # If item has not been forced yet, add/replace its' value in the
        # registry.
        if force:

            if not cls.uid in self._forced:
                self._registry[cls.uid] = cls
                self._forced.append(cls.uid)
                return True
            else:
                return False

        else:

            if cls.uid in self._registry:
                return False
            else:
                self._registry[cls.uid] = cls
                return True

    def unregister(self, cls):
        if not issubclass(cls, self.type):
            raise InvalidRegistryItemType(
                "Invalid item type `{0}` for registry "
                "`{1}`".format(cls, self.__class__)
                )

        # Only non-forced items are allowed to be unregistered.
        if cls.uid in self._registry and not cls.uid in self._forced:
            self._registry.pop(cls.uid)
            return True
        else:
            return False

    def get(self, uid, default=None):
        """
        Gets the given entry from the registry.

        :param string uid:
        :return mixed.
        """
        item = self._registry.get(uid, default)

        if not item:
            err_msg = self.plugin_not_found_error_message.format(
                uid, self.__class__
                )
            if self.fail_on_missing_plugin:
                logger.error(err_msg)
                raise self.plugin_not_found_exception_cls(err_msg)
            else:
                logger.debug(err_msg)

        return item


class FormElementPluginRegistry(BaseRegistry):
    """
    Form element plugins registry.
    """
    type = (FormElementPlugin, FormFieldPlugin)
    fail_on_missing_plugin = FAIL_ON_MISSING_FORM_ELEMENT_PLUGINS
    plugin_not_found_exception_cls = FormElementPluginDoesNotExist


class FormHandlerPluginRegistry(BaseRegistry):
    """
    Form handler plugins registry.
    """
    type = FormHandlerPlugin
    fail_on_missing_plugin = FAIL_ON_MISSING_FORM_HANDLER_PLUGINS
    plugin_not_found_exception_cls = FormHandlerPluginDoesNotExist


class ThemeRegistry(BaseRegistry):
    """
    Themes registry.
    """
    type = BaseTheme


class FormCallbackRegistry(object):
    """
    Registry of callbacks. Holds callbacks for stages listed in the
    ``fobi.constants.CALLBACK_STAGES``.
    """
    def __init__(self):
        """
        """
        self._registry = {}

        for stage in CALLBACK_STAGES:
            self._registry[stage] = []

    def uidfy(self, cls):
        """
        Makes a UID string from the class given.

        :return string:
        """
        return "{0}.{1}".format(cls.__module__, cls.__name__)

    def register(self, cls):
        """
        Registers the plugin in the registry.

        :param mixed.
        """
        if not issubclass(cls, FormCallback):
            raise InvalidRegistryItemType(
                "Invalid item type `{0}` for registry "
                "`{1}`".format(cls, self.__class__)
                )

        #uid = self.uidfy(cls)
        # If item has not been forced yet, add/replace its' value in the
        # registry.

        if cls in self._registry[cls.stage]:
            return False
        else:
            self._registry[cls.stage].append(cls)
            return True

    def get_callbacks(self, stage=None):
        """
        Get callbacks for the stage given.

        :param string stage:
        :return list:
        """
        if stage:
            return self._registry.get(stage, [])
        else:
            callbacks = []
            for stage_callbacks in self._registry.values():
                callbacks += stage_callbacks
            return callbacks


class BasePluginWidgetRegistry(object):
    """
    Registry of fobi plugins widgets (renderers).
    """
    type = None

    def __init__(self):
        assert self.type
        self._registry = {}
        self._forced = []

    @staticmethod
    def namify(theme, plugin_uid):
        return '{0}.{1}'.format(theme, plugin_uid)

    def register(self, cls, force=False):
        """
        Registers the plugin renderer in the registry.

        :param fobi.base.BasePluginRenderer cls: Subclass of
            `fobi.base.BasePluginRenderer`.
        """
        if not issubclass(cls, self.type):
            raise InvalidRegistryItemType(
                "Invalid item type `{0}` for registry "
                "`{1}`".format(cls, self.__class__)
                )

        uid = BasePluginWidgetRegistry.namify(cls.theme_uid, cls.plugin_uid)

        # If item has not been forced yet, add/replace its' value in the
        # registry.
        if force:

            if not uid in self._forced:
                self._registry[uid] = cls
                self._forced.append(uid)
                return True
            else:
                return False

        else:

            if uid in self._registry:
                return False
            else:
                self._registry[uid] = cls
                return True

    def unregister(self, cls):
        if not issubclass(cls, self.type):
            raise InvalidRegistryItemType(
                "Invalid item type `{0}` for registry "
                "`{1}`".format(cls, self.__class__)
                )

        uid = BasePluginWidgetRegistry.namify(cls.theme_uid, cls.plugin_uid)

        # Only non-forced items are allowed to be unregistered.
        if uid in self._registry and not uid in self._forced:
            self._registry.pop(uid)
            return True
        else:
            return False

    def get(self, uid, default=None):
        """
        Gets the given entry from the registry.

        :param string uid:
        :return mixed.
        """
        item = self._registry.get(uid, default)
        if not item:
            logger.debug(
                "Can't find plugin widget with uid `{0}` in `{1}` "
                "registry".format(uid, self.__class__)
                )
        return item


class FormElementPluginWidgetRegistry(BasePluginWidgetRegistry):
    """
    Registry of form element plugins.
    """
    type = FormElementPluginWidget


class FormHandlerPluginWidgetRegistry(BasePluginWidgetRegistry):
    """
    Registry of form handler plugins.
    """
    type = FormHandlerPluginWidget


# Register form field plugins by calling form_field_plugin_registry.register()
form_element_plugin_registry = FormElementPluginRegistry()

# Register action plugins by calling form_action_plugin_registry.register()
form_handler_plugin_registry = FormHandlerPluginRegistry()

# Register themes by calling theme_registry.register()
theme_registry = ThemeRegistry()

# Register action plugins by calling form_action_plugin_registry.register()
form_callback_registry = FormCallbackRegistry()

# Register plugin widgets by calling
# form_element_plugin_widget_registry.register()
form_element_plugin_widget_registry = FormElementPluginWidgetRegistry()

# Register plugin widgets by calling
# form_handler_plugin_widget_registry.register()
form_handler_plugin_widget_registry = FormHandlerPluginWidgetRegistry()

# *****************************************************************************
# *****************************************************************************
# ******************************** Helpers ************************************
# *****************************************************************************
# *****************************************************************************

def ensure_autodiscover():
    """
    Ensures that plugins are autodiscovered.
    """
    if not (form_element_plugin_registry._registry
            and form_handler_plugin_registry._registry
            and theme_registry._registry):
        autodiscover()


def assemble_form_field_widget_class(base_class, plugin):
    """
    Finish this or remove.

    #TODO
    """
    class DeclarativeMetaclass(type):
        """
        Wrapped class.
        """
        def __new__(cls, name, bases, attrs):
            new_class = super(DeclarativeMetaclass, cls).__new__(
                cls, name, bases, attrs
                )
            return new_class

        def render(self, name, value, attrs=None):
            """
            Smart render.
            """
            widget = plugin.get_widget()
            if widget.hasattr('render') and callable(widget.render):
                return widget.render(name, value, attrs=attrs)
            else:
                super(DeclarativeMetaclass, self).render(
                    name, value, attrs=attrs
                    )

    class WrappedWidget(with_metaclass(DeclarativeMetaclass, base_class)):
        """
        Dynamically created form element plugin class.
        """

    return WrappedWidget

# *****************************************************************************
# *********************************** Generic *********************************
# *****************************************************************************

def get_registered_plugins(registry, as_instances=False):
    """
    Gets a list of registered plugins in a form if tuple (plugin name, plugin
    description). If not yet autodiscovered, autodiscovers them.

    :return list:
    """
    ensure_autodiscover()

    if as_instances:
        return registry._registry

    registered_plugins = []

    for uid, plugin in registry._registry.items():
        plugin_name = safe_text(plugin.name)
        registered_plugins.append((uid, plugin_name))

    return registered_plugins

def get_registered_plugins_grouped(registry, sort_items=True):
    """
    Gets a list of registered plugins in a form if tuple (plugin name, plugin
    description). If not yet autodiscovered, autodiscovers them.

    :return dict:
    """
    ensure_autodiscover()

    registered_plugins = {}

    for uid, plugin in registry._registry.items():
        plugin_name = safe_text(plugin.name)
        plugin_group = safe_text(plugin.group)

        if not plugin_group in registered_plugins:
            registered_plugins[plugin_group] = []
        registered_plugins[plugin_group].append((uid, plugin_name))

    if sort_items:
        for key, prop in registered_plugins.items():
            prop.sort()

    return registered_plugins

def get_registered_plugin_uids(registry, flattern=True):
    """
    Gets a list of registered plugin uids as a list . If not yet
    autodiscovered, autodiscovers them.

    :return list:
    """
    ensure_autodiscover()

    registered_plugin_uids = registry._registry.keys()

    if flattern:
        registered_plugin_uids = list(registered_plugin_uids)

    return registered_plugin_uids

def validate_plugin_uid(registry, plugin_uid):
    """
    Validates the plugin uid.

    :param string plugin_uid:
    :return bool:
    """
    return plugin_uid in get_registered_plugin_uids(registry, flattern=True)

# *****************************************************************************
# ***************************** Form element specific *************************
# *****************************************************************************

def get_registered_form_element_plugins():
    """
    Gets a list of registered plugins in a form if tuple (plugin name, plugin
    description). If not yet autodiscovered, autodiscovers them.

    :return list:
    """
    return get_registered_plugins(form_element_plugin_registry)

def get_registered_form_element_plugins_grouped():
    """
    Gets a list of registered plugins in a form if tuple (plugin name, plugin
    description). If not yet autodiscovered, autodiscovers them.

    :return dict:
    """
    return get_registered_plugins_grouped(form_element_plugin_registry)

def get_registered_form_element_plugin_uids(flattern=True):
    """
    Gets a list of registered plugins in a form if tuple (plugin name, plugin
    description). If not yet autodiscovered, autodiscovers them.

    :return list:
    """
    return get_registered_plugin_uids(
        form_element_plugin_registry, flattern=flattern
        )

def validate_form_element_plugin_uid(plugin_uid):
    """
    Validates the plugin uid.

    :param string plugin_uid:
    :return bool:
    """
    return validate_plugin_uid(form_element_plugin_registry, plugin_uid)

def submit_plugin_form_data(form_entry, request, form):
    """
    Submit plugin form data for all plugins.

    :param fobi.models.FormEntry form_entry: Instance of
        ``fobi.models.FormEntry``.
    :param django.http.HttpRequest request:
    :param django.forms.Form form:
    """
    for form_element_entry in form_entry.formelemententry_set.all():
        # Get the plugin.
        form_element_plugin = form_element_entry.get_plugin(request=request)
        updated_form = form_element_plugin._submit_plugin_form_data(
            form_entry=form_entry, request=request, form=form
            )
        if updated_form:
            form = updated_form

    return form

def get_ignorable_form_fields(form_element_entries):
    """
    Get ignorable form fields by getting those without values.

    :param iterable form_element_entries: Iterable of
        ``fobi.models.FormElementEntry`` objects.
    :return iterable: Iterable of ignorable form element entries.
    """
    # Get ignorable plugins
    ignorable_plugins = []
    for key, value in form_element_plugin_registry._registry.items():
        if not value.has_value:
            ignorable_plugins.append(key)

    # Get ignorable form fields
    ignorable_form_fields = []
    for form_element_entry in form_element_entries:
        if form_element_entry.plugin_uid in ignorable_plugins:
            form_element_plugin = form_element_entry.get_plugin()
            try:
                ignorable_form_fields.append(form_element_plugin.data.name)
            except AttributeError as e:
                pass

    return ignorable_form_fields

# *****************************************************************************
# **************************** Form handler specific **************************
# *****************************************************************************

def get_cleaned_data(form, keys_to_remove=[], values_to_remove=[]):
    """
    Gets cleaned data, having the trash (fields without values) filtered
    out.

    :param form:
    :param iterable values_to_remove:
    :return dict:
    """
    if not values_to_remove:
        values_to_remove = get_ignorable_form_values()

    cleaned_data = copy.copy(form.cleaned_data)
    cleaned_data = clean_dict(
        cleaned_data,
        keys = list(set(cleaned_data.keys()) - set(keys_to_remove)),
        values = values_to_remove
        )

    return cleaned_data

def get_field_name_to_label_map(form, keys_to_remove=[], values_to_remove=[]):
    """
    Get field name to label map.

    :param form:
    :param iterable keys_to_remove:
    :param iterable values_to_remove:
    :return dict:
    """
    if not keys_to_remove:
        keys_to_remove = get_ignorable_form_fields([])

    if not values_to_remove:
        values_to_remove = get_ignorable_form_values()

    field_name_to_label_map = clean_dict(
        map_field_name_to_label(form),
        keys_to_remove,
        values_to_remove
        )

    return field_name_to_label_map

def get_processed_form_data(form, form_element_entries):
    """
    Gets processed form handler data. Simply fires both 
    ``fobi.base.get_cleaned_data`` and ``fobi.base.get_field_name_to_label_map``
    functions and returns the result.

    :param django.forms.Form form:
    :param iterable: Iterable of form element entries.
    :return tuple:
    """
    keys_to_remove = get_ignorable_form_fields(form_element_entries)
    values_to_remove = get_ignorable_form_values()

    field_name_to_label_map = \
        get_field_name_to_label_map(form, keys_to_remove, values_to_remove)

    keys_to_remove = list(field_name_to_label_map.keys())

    return (
        field_name_to_label_map,
        get_cleaned_data(form, keys_to_remove, values_to_remove)
        )

def get_registered_form_handler_plugins(as_instances=False):
    """
    Gets a list of registered plugins in a form of tuple (plugin name, plugin
    description). If not yet autodiscovered, autodiscovers them.

    :return list:
    """
    return get_registered_plugins(form_handler_plugin_registry,
                                  as_instances=as_instances)

def get_registered_form_handler_plugin_uids(flattern=True):
    """
    Gets a list of UIDs of registered form handler plugins. If not yet
    autodiscovered, autodiscovers them.

    :return list:
    """
    return get_registered_plugin_uids(
        form_handler_plugin_registry, flattern=flattern
        )

def validate_form_handler_plugin_uid(plugin_uid):
    """
    Validates the plugin uid.

    :param string plugin_uid:
    :return bool:
    """
    return validate_plugin_uid(form_handler_plugin_registry, plugin_uid)

def get_ordered_form_handler_plugins():
    """
    Gets form handler plugins in the execution order as a sortable
    dictionary, which can be later on used to add real plugins to
    be executed.

    :return fobi.data_structures.SortableDict:
    """
    form_handler_plugins = SortableDict()

    # Prio goes to the ones specified as first in the settings
    for uid in FORM_HANDLER_PLUGINS_EXECUTION_ORDER:
        form_handler_plugins[uid] = []

    # Adding all the rest
    for uid in form_handler_plugin_registry._registry.keys():
        if not uid in form_handler_plugins:
            form_handler_plugins[uid] = []

    return form_handler_plugins

def run_form_handlers(form_entry, request, form, form_element_entries=None):
    """
    Runs form handlers.

    :param fobi.models.FormEntry form_entry:
    :param django.http.HttpRequest request:
    :param django.forms.Form form:
    :param iterable form_element_entries:
    :return tuple: List of success responses, list of error responses
    """
    # Errors list
    errors = []

    # Responses of successfully procesessed handlers
    responses = []

    # Getting form handler plugins in their execution order.
    ordered_form_handlers = get_ordered_form_handler_plugins()

    # Getting the form handlers to be executed.
    form_handlers = form_entry.formhandlerentry_set.order_by('plugin_uid')[:]

    # Assembling a new dictionary of the form handlers to iterate later.
    for form_handler in form_handlers:
        ordered_form_handlers[form_handler.plugin_uid].append(form_handler)

    # Iterating through the form handlers in the order
    # specified in the settings.
    for uid, form_handlers in ordered_form_handlers.items():
        #logger.debug("UID: {0}".format(uid))
        for form_handler in form_handlers:
            # Get the form handler plugin
            form_handler_plugin = form_handler.get_plugin(request=request)

            # Run the form handler
            success, response = form_handler_plugin._run(
                form_entry,
                request,
                form,
                form_element_entries
                )

            if success:
                responses.append((form_handler_plugin, response))
            else:
                errors.append((form_handler_plugin, response))

    return (responses, errors)

# *****************************************************************************
# ******************************* Theme specific ******************************
# *****************************************************************************

def get_registered_themes():
    """
    Gets a list of registered themes in form of tuple (plugin name, plugin
    description). If not yet autodiscovered, autodiscovers them.

    :return list:
    """
    return get_registered_plugins(theme_registry)

def get_registered_theme_uids(flattern=True):
    """
    Gets a list of registered themes in a form of tuple (plugin name, plugin
    description). If not yet autodiscovered, autodiscovers them.

    :return list:
    """
    return get_registered_plugin_uids(theme_registry, flattern=flattern)

def validate_theme_uid(plugin_uid):
    """
    Validates the theme uid.

    :param string plugin_uid:
    :return bool:
    """
    return validate_plugin_uid(theme_registry, plugin_uid)

def get_theme(request=None, theme_uid=None, as_instance=False):
    """
    Gets the theme by ``theme_uid`` given. If left empty, takes the default
    one chosen in ``settings`` module.

    Raises a ``fobi.exceptions.ThemeDoesNotExist`` when no default layout
    could be found.

    :param django.http.HttpRequest request:
    :param int theme_uid:
    :param bool as_instance:
    :return fobi.base.BaseTheme: Sublcass of `fobi.base.BaseTheme`.
    """
    ensure_autodiscover()

    if not theme_uid:
        theme_uid = DEFAULT_THEME

    Theme = theme_registry.get(theme_uid, None)
    if not Theme:
        raise ThemeDoesNotExist(
            _("Theme `{0}` does not exist!").format(theme_uid)
            )

    if as_instance:
        return Theme()

    return Theme

get_default_theme = lambda: get_theme(as_instance=True)

get_theme_by_uid = lambda theme_uid: get_theme(
    theme_uid = theme_uid,
    as_instance = True
    )

# *****************************************************************************
# **************************** Form callbacks specific ************************
# *****************************************************************************

def get_registered_form_callbacks(stage=None):
    """
    Gets registered form callbacks for the stage given.
    """
    return form_callback_registry.get_callbacks(stage=stage)

def fire_form_callbacks(form_entry, request, form, stage=None):
    """
    Fires callbacks.

    :param fobi.models.FormEntry form_entry:
    :param django.http.HttpRequest request:
    :param django.forms.Form form:
    :param string stage:
    :return django.forms.Form form:
    """
    callbacks = form_callback_registry.get_callbacks(stage=stage)
    for CallbackClass in callbacks:
        callback = CallbackClass()
        updated_form = callback.callback(form_entry, request, form)
        if updated_form:
            form = updated_form
    return form

# *****************************************************************************
# ******************************* Widget specific *****************************
# *****************************************************************************
def get_plugin_widget(registry, plugin_uid, request=None, as_instance=False,
                      theme=None):
    """
    Gets the plugin widget for the ``plugin_uid`` given. Looks up in the
    ``registry`` provided.

    :param fobi.base.BasePluginWidgetRegistry registry: Subclass of.
    :param str plugin_uid: UID of the plugin to get the widget for.
    :param django.http.HttpRequest request:
    :param bool as_instance:
    :param fobi.base.BaseTheme theme: Subclass of.
    :return BasePluginWidget: Subclass of.
    """
    if not theme:
        theme = get_theme(request=request, as_instance=True)

    return registry.get(
        BasePluginWidgetRegistry.namify(theme.uid, plugin_uid)
        )

def get_form_element_plugin_widget(plugin_uid, request=None, as_instance=False,
                                   theme=None):
    """
    Gets the form element plugin widget for the ``plugin_uid`` given.

    :param fobi.base.BasePluginWidgetRegistry registry: Subclass of.
    :param str plugin_uid: UID of the plugin to get the widget for.
    :param django.http.HttpRequest request:
    :param bool as_instance:
    :param fobi.base.BaseTheme theme: Subclass of.
    :return BasePluginWidget: Subclass of.
    """
    return get_plugin_widget(
        registry = form_element_plugin_widget_registry,
        plugin_uid = plugin_uid,
        request = request,
        as_instance = as_instance,
        theme = theme
        )

def get_form_handler_plugin_widget(plugin_uid, request=None, as_instance=False,
                                   theme=None):
    """
    Gets the form handler plugin widget for the ``plugin_uid`` given.

    :param fobi.base.BasePluginWidgetRegistry registry: Subclass of.
    :param str plugin_uid: UID of the plugin to get the widget for.
    :param django.http.HttpRequest request:
    :param bool as_instance:
    :param fobi.base.BaseTheme theme: Subclass of.
    :return BasePluginWidget: Subclass of.
    """
    return get_plugin_widget(
        registry = form_handler_plugin_widget_registry,
        plugin_uid = plugin_uid,
        request = request,
        as_instance = as_instance,
        theme = theme
        )

# *****************************************************************************
# ******************************** Media specific *****************************
# *****************************************************************************

def collect_plugin_media(form_element_entries, request=None):
    """
    Collects the plugin media for form element entries given.

    :param iterable form_element_entries: Iterable of
        ``fobi.models.FormElementEntry`` instances.
    :param django.http.HttpRequest request:
    :return dict: Returns a dict containing the 'js' and 'css' keys.
        Correspondent values of those keys are lists containing paths to the
        CSS and JS media files.
    """
    media_js = []
    media_css = []
    theme = get_theme(request=request, as_instance=True)
    for form_element_entry in form_element_entries:
        widget_cls = form_element_plugin_widget_registry.get(
            BasePluginWidgetRegistry.namify(
                theme.uid, form_element_entry.plugin_uid
                )
            )
        if widget_cls:
            media_js += getattr(widget_cls, 'media_js', [])
            media_css += getattr(widget_cls, 'media_css', [])
        else:
            logger.debug(
                "No widget for form element entry "
                "{0}".format(form_element_entry.__dict__)
                )
    return {'js': media_js, 'css': media_css}
