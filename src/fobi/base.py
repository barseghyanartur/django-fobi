"""
Base module. All `uids` are supposed to be pythonic function names (see
PEP http://www.python.org/dev/peps/pep-0008/#function-names).
"""
import copy
import logging
import re
import traceback
import uuid

from collections import defaultdict, OrderedDict

import simplejson as json

from django import forms
from django.forms import ModelForm
from django.forms.utils import ErrorList
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext, Template

from nine.versions import DJANGO_GTE_1_8

from six import with_metaclass, string_types

from .constants import CALLBACK_STAGES
from .data_structures import SortableDict
from .discover import autodiscover
from .exceptions import (
    DoesNotExist,
    FormElementPluginDoesNotExist,
    FormHandlerPluginDoesNotExist,
    FormWizardHandlerPluginDoesNotExist,
    IntegrationFormElementPluginDoesNotExist,
    IntegrationFormHandlerPluginDoesNotExist,
    InvalidRegistryItemType,
    ThemeDoesNotExist,
)
from .helpers import (
    clean_dict,
    get_form_element_entries_for_form_wizard_entry,
    get_ignorable_form_values,
    map_field_name_to_label,
    safe_text,
    StrippedRequest,
    uniquify_sequence,
)
from .settings import (
    CUSTOM_THEME_DATA,
    DEBUG,
    DEFAULT_THEME,
    FAIL_ON_ERRORS_IN_FORM_ELEMENT_PLUGINS,
    FAIL_ON_ERRORS_IN_FORM_HANDLER_PLUGINS,
    FAIL_ON_ERRORS_IN_FORM_WIZARD_HANDLER_PLUGINS,
    FAIL_ON_MISSING_FORM_ELEMENT_PLUGINS,
    FAIL_ON_MISSING_FORM_HANDLER_PLUGINS,
    FAIL_ON_MISSING_FORM_WIZARD_HANDLER_PLUGINS,
    FAIL_ON_MISSING_INTEGRATION_FORM_ELEMENT_PLUGINS,
    FAIL_ON_MISSING_INTEGRATION_FORM_HANDLER_PLUGINS,
    FORM_HANDLER_PLUGINS_EXECUTION_ORDER,
    FORM_WIZARD_HANDLER_PLUGINS_EXECUTION_ORDER,
    SORT_PLUGINS_BY_VALUE,
    THEME_FOOTER_TEXT,
    # FAIL_ON_ERRORS_IN_FORM_ELEMENT_PLUGINS,
)

__title__ = 'fobi.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'assemble_form_field_widget_class',
    'BaseDataStorage',
    'BaseFormFieldPluginForm',
    'BasePlugin',
    'BasePluginForm',
    'BaseRegistry',
    'ClassProperty',
    'classproperty',
    'collect_plugin_media',
    'ensure_autodiscover',
    'fire_form_callbacks',
    'form_callback_registry',
    'form_element_plugin_registry',
    'form_element_plugin_widget_registry',
    'form_handler_plugin_registry',
    'form_handler_plugin_widget_registry',
    'form_wizard_handler_plugin_registry',
    'form_wizard_handler_plugin_widget_registry',
    'FormCallback',
    'FormCallbackRegistry',
    'FormElementPlugin',
    'FormElementPluginDataStorage',
    'FormElementPluginRegistry',
    'FormElementPluginWidget',
    'FormElementPluginWidgetRegistry',
    'FormFieldPlugin',
    'FormHandlerPlugin',
    'FormHandlerPluginDataStorage',
    'FormHandlerPluginRegistry',
    'FormHandlerPluginWidget',
    'FormHandlerPluginWidgetRegistry',
    'FormWizardHandlerPlugin',
    'FormWizardHandlerPluginDataStorage',
    'FormWizardHandlerPluginRegistry',
    'FormWizardHandlerPluginWidget',
    'FormWizardHandlerPluginWidgetRegistry',
    'get_form_element_plugin_widget',
    'get_form_handler_plugin_widget',
    'get_form_wizard_handler_plugin_widget',
    'get_ordered_form_handlers',
    'get_ordered_form_wizard_handlers',
    'get_plugin_widget',
    'get_processed_form_data',
    'get_processed_form_wizard_data',
    'get_registered_form_callbacks',
    'get_registered_form_element_plugin_uids',
    'get_registered_form_element_plugins',
    'get_registered_form_element_plugins_grouped',
    'get_registered_form_handler_plugin_uids',
    'get_registered_form_handler_plugins',
    'get_registered_form_wizard_handler_plugin_uids',
    'get_registered_form_wizard_handler_plugins',
    'get_registered_integration_form_element_plugin_uids',
    'get_registered_integration_form_element_plugins',
    'get_registered_integration_form_element_plugins_grouped',
    'get_registered_integration_form_handler_plugin_uids',
    'get_registered_integration_form_handler_plugins',
    'get_registered_integration_form_handler_plugins_grouped',
    'get_registered_plugin_uids',
    'get_registered_plugins',
    'get_registered_theme_uids',
    'get_registered_themes',
    'get_theme',
    'integration_form_callback_registry',
    'integration_form_element_plugin_registry',
    'integration_form_handler_plugin_registry',
    'IntegrationFormCallback',
    'IntegrationFormCallbackRegistry',
    'IntegrationFormElementPlugin',
    'IntegrationFormElementPluginDataStorage',
    'IntegrationFormElementPluginProcessor',
    'IntegrationFormElementPluginRegistry',
    'IntegrationFormFieldPlugin',
    'IntegrationFormHandlerPlugin',
    'IntegrationFormHandlerPluginDataStorage',
    'IntegrationFormHandlerPluginRegistry',
    'run_form_handlers',
    'run_form_wizard_handlers',
    'submit_plugin_form_data',
    'theme_registry',
    'validate_form_element_plugin_uid',
    'validate_form_handler_plugin_uid',
    'validate_form_wizard_handler_plugin_uid',
    'validate_integration_form_element_plugin_uid',
    'validate_integration_form_handler_plugin_uid',
    'validate_theme_uid',
)

logger = logging.getLogger(__name__)

# _ = lambda s: s

# *****************************************************************************
# *****************************************************************************
# ********************************** Theme ************************************
# *****************************************************************************
# *****************************************************************************


class BaseTheme(object):
    """Base theme.

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
    project_name = _("Build your forms")  # Project name
    footer_text = ''  # '&copy; Company 2014'

    

    # ***********************************************************************
    # ***********************************************************************
    # ********************** Theme specific urls*****************************
    # ***********************************************************************
    # ***********************************************************************

    # form element entry

    add_form_element_entry = 'fobi.add_form_element_entry'

    add_form_handler_entry = 'fobi.add_form_handler_entry'
    edit_form_handler_entry = 'fobi.edit_form_handler_entry'
    delete_form_handler_entry = 'fobi.delete_form_handler_entry'

    # form wizard entry

    create_form_wizard_entry = 'fobi.create_form_wizard_entry'
    import_form_wizard_entry = 'fobi.import_form_wizard_entry'
    view_form_wizard_entry = 'fobi.view_form_wizard_entry'
    edit_form_wizard_entry = 'fobi.edit_form_wizard_entry'
    delete_form_wizard_entry = 'fobi.delete_form_wizard_entry'
    export_form_wizard_entry = 'fobi.export_form_wizard_entry'

    add_form_wizard_form_entry = 'fobi.add_form_wizard_form_entry'
    delete_form_wizard_form_entry = 'fobi.delete_form_wizard_form_entry'

    add_form_wizard_handler_entry = 'fobi.add_form_wizard_handler_entry'
    edit_form_wizard_handler_entry = 'fobi.edit_form_wizard_handler_entry'
    delete_form_wizard_handler_entry = 'fobi.delete_form_wizard_handler_entry'

    # form entry

    create_form_entry = 'fobi.create_form_entry'
    import_form_entry = 'fobi.import_form_entry'
    export_form_entry = 'fobi.export_form_entry'
    delete_form_entry = 'fobi.delete_form_entry'
    edit_form_entry = 'fobi.edit_form_entry'
    view_form_entry = 'fobi.view_form_entry'


    # dashboards

    dashboard = 'fobi.dashboard'
    form_wizards_dashboard = 'fobi.form_wizards_dashboard'
    


    # ***********************************************************************
    # ***********************************************************************
    # ********************** Form HTML specific *****************************
    # ***********************************************************************
    # ***********************************************************************
    # Used in almost all ``fobi_form_elements`` modules and forms.
    form_element_html_class = ''  # form-control

    # Radio element HTML class. Used in ``fobi_form_elements`` modules
    # and forms.
    form_radio_element_html_class = ''

    # Checkbox element HTML class. Used in ``fobi_form_elements`` modules
    # and forms.
    form_element_checkbox_html_class = ''  # checkbox

    # Important, since used in ``edit_form_entry_edit_option_html``
    # method.
    form_view_form_entry_option_class = ''  # glyphicon glyphicon-list

    # Important, since used in ``edit_form_entry_edit_option_html``
    # method.
    form_edit_form_entry_option_class = ''  # glyphicon glyphicon-edit

    # Important, since used in ``edit_form_entry_edit_option_html``
    # method.
    form_delete_form_entry_option_class = ''  # glyphicon glyphicon-remove

    # Important, since used in ``edit_form_entry_help_text_extra``
    # method.
    form_list_container_class = ''  # list-inline

    # ***********************************************************************
    # ***********************************************************************
    # ****************************** Templates ******************************
    # ***********************************************************************
    # ***********************************************************************

    # ***********************************************************************
    # *************************** Base templates ****************************
    # ***********************************************************************
    master_base_template = 'fobi/generic/_base.html'
    base_template = 'fobi/generic/base.html'
    base_view_template = None
    base_edit_template = None

    # ***********************************************************************
    # ***************************** Snippets ********************************
    # ***********************************************************************
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

    # TODO
    form_wizard_ajax = 'fobi/generic/snippets/form_wizard_ajax.html'
    form_wizard_view_ajax = None
    form_wizard_edit_ajax = None
    # END TODO

    form_wizard_snippet_template_name = \
        'fobi/generic/snippets/form_wizard_snippet.html'
    form_wizard_view_snippet_template_name = None
    form_wizard_edit_snippet_template_name = None

    form_wizard_properties_snippet_template_name = \
        'fobi/generic/snippets/form_wizard_properties_snippet.html'

    # ***********************************************************************
    # *********************** Form entry CUD and add-ons ********************
    # ***********************************************************************
    create_form_entry_template = 'fobi/generic/create_form_entry.html'
    create_form_entry_ajax_template = \
        'fobi/generic/create_form_entry_ajax.html'

    edit_form_entry_template = 'fobi/generic/edit_form_entry.html'
    edit_form_entry_ajax_template = 'fobi/generic/edit_form_entry_ajax.html'

    form_entry_submitted_template = 'fobi/generic/form_entry_submitted.html'
    form_entry_submitted_ajax_template = \
        'fobi/generic/form_entry_submitted_ajax.html'

    embed_form_entry_submitted_ajax_template = None

    view_form_entry_template = 'fobi/generic/view_form_entry.html'
    view_form_entry_ajax_template = 'fobi/generic/view_form_entry_ajax.html'

    view_embed_form_entry_ajax_template = None

    form_entry_inactive_template = 'fobi/generic/form_entry_inactive.html'
    form_entry_inactive_ajax_template = \
        'fobi/generic/form_entry_inactive_ajax.html'

    # ***********************************************************************
    # *********************** Form element entry CUD ************************
    # ***********************************************************************
    add_form_element_entry_template = \
        'fobi/generic/add_form_element_entry.html'
    add_form_element_entry_ajax_template = \
        'fobi/generic/add_form_element_entry_ajax.html'

    edit_form_element_entry_template = \
        'fobi/generic/edit_form_element_entry.html'
    edit_form_element_entry_ajax_template = \
        'fobi/generic/edit_form_element_entry_ajax.html'

    # ***********************************************************************
    # *********************** Form handler entry CUD ************************
    # ***********************************************************************
    add_form_handler_entry_template = \
        'fobi/generic/add_form_handler_entry.html'
    add_form_handler_entry_ajax_template = \
        'fobi/generic/add_form_handler_entry_ajax.html'

    edit_form_handler_entry_template = \
        'fobi/generic/edit_form_handler_entry.html'
    edit_form_handler_entry_ajax_template = \
        'fobi/generic/edit_form_handler_entry_ajax.html'

    # ***********************************************************************
    # ******************* Form wizard handler entry CUD *********************
    # ***********************************************************************
    add_form_wizard_handler_entry_template = \
        'fobi/generic/add_form_wizard_handler_entry.html'
    add_form_wizard_handler_entry_ajax_template = \
        'fobi/generic/add_form_wizard_handler_entry_ajax.html'

    edit_form_wizard_handler_entry_template = \
        'fobi/generic/edit_form_wizard_handler_entry.html'
    edit_form_wizard_handler_entry_ajax_template = \
        'fobi/generic/edit_form_wizard_handler_entry_ajax.html'

    # ***********************************************************************
    # ***************************** Dashboard *******************************
    # ***********************************************************************
    dashboard_template = 'fobi/generic/dashboard.html'

    form_wizards_dashboard_template = \
        'fobi/generic/form_wizards_dashboard.html'

    forms_list_template = 'fobi/generic/forms_list.html'

    # ***********************************************************************
    # ************************ Form wizard entry CUD ************************
    # ***********************************************************************
    # Not even sure if this one is used - TODO: find out
    form_wizard_template = 'fobi/generic/snippets/form_wizard.html'

    create_form_wizard_entry_template = \
        'fobi/generic/create_form_wizard_entry.html'
    create_form_wizard_entry_ajax_template = \
        'fobi/generic/create_form_wizard_entry_ajax.html'

    edit_form_wizard_entry_template = \
        'fobi/generic/edit_form_wizard_entry.html'
    edit_form_wizard_entry_ajax_template = \
        'fobi/generic/edit_form_wizard_entry_ajax.html'

    # TODO
    form_wizard_entry_submitted_template = \
        'fobi/generic/form_wizard_entry_submitted.html'
    form_wizard_entry_submitted_ajax_template = \
        'fobi/generic/form_wizard_entry_submitted_ajax.html'

    embed_form_wizard_entry_submitted_ajax_template = None

    view_form_wizard_entry_template = \
        'fobi/generic/view_form_wizard_entry.html'
    view_form_wizard_entry_ajax_template = \
        'fobi/generic/view_form_wizard_entry_ajax.html'

    view_embed_form_wizard_entry_ajax_template = None
    # END TODO

    # ***********************************************************************
    # *************************** Service templates *************************
    # ***********************************************************************
    import_form_entry_template = 'fobi/generic/import_form_entry.html'
    import_form_entry_ajax_template = \
        'fobi/generic/import_form_entry_ajax.html'

    # ***********************************************************************
    # ************************* Form importer templates *********************
    # ***********************************************************************
    form_importer_template = 'fobi/generic/form_importer.html'
    form_importer_ajax_template = 'fobi/generic/form_importer_ajax.html'

    # *************************************************************************
    # ******************** Extras that make things easy ***********************
    # *************************************************************************
    custom_data = {}

    page_header_html_class = ''  # page-header
    form_html_class = ''  # form-horizontal
    form_button_outer_wrapper_html_class = ''  # control-group
    form_button_wrapper_html_class = ''  # controls
    form_button_html_class = ''  # btn
    form_primary_button_html_class = ''  # btn-primary

    def __init__(self, user=None):
        """Constructor.

        :param django.contrib.auth.models.User user:
        """
        assert self.uid
        assert self.name
        # assert self.view_template_name
        # assert self.edit_template_name
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

        # If no specific ``form_wizard_view_snippet_template_name`` specified,
        # fall back to the ``form_wizard_snippet_template_name``.
        if not self.form_wizard_view_snippet_template_name:
            self.form_wizard_view_snippet_template_name = \
                self.form_wizard_snippet_template_name

        # If no specific ``form_wizard_edit_snippet_template_name`` specified,
        # fall back to the ``form_wizard_snippet_template_name``.
        if not self.form_wizard_edit_snippet_template_name:
            self.form_wizard_edit_snippet_template_name = \
                self.form_wizard_snippet_template_name

        # If no specific ``form_view_ajax`` specified, fall
        # back to the ``form_ajax``.
        if not self.form_view_ajax:
            self.form_view_ajax = self.form_ajax

        # If no specific ``form_edit_ajax`` specified, fall
        # back to the ``form_ajax``.
        if not self.form_edit_ajax:
            self.form_edit_ajax = self.form_ajax

        # If no specific ``form_wizard_view_ajax`` specified, fall
        # back to the ``form_wizard_ajax``.
        if not self.form_wizard_view_ajax:
            self.form_wizard_view_ajax = self.form_wizard_ajax

        # If no specific ``form_wizard_edit_ajax`` specified, fall
        # back to the ``form_wizard_ajax``.
        if not self.form_wizard_edit_ajax:
            self.form_wizard_edit_ajax = self.form_wizard_ajax

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
        # referred like `fobi_theme.custom_data`.
        self.custom_data = self.get_custom_data()

        # Set the footer text from settings if not specified
        # in the theme.
        if not self.footer_text:
            self.footer_text = self.get_footer_text()

    def _get_custom_data(self):
        """Get custom data (used internally).

        Internal method for obtaining the custom data from settings.

        :return dict:
        """
        if self.uid in CUSTOM_THEME_DATA:
            return CUSTOM_THEME_DATA[self.uid]
        return {}

    def get_custom_data(self):
        """Get custom data.

        Fills the theme with custom data from settings.

        :return dict:
        """
        return self._get_custom_data()

    def _get_footer_text(self):
        """Get footer text (used internally).

        Internal method for returning the footer text from settings.

        :return str:
        """
        return _(THEME_FOOTER_TEXT)

    def get_footer_text(self):
        """Get footer text.

        Returns the footer text from settings.

        :return str:
        """
        return self._get_footer_text()

    @classmethod
    def edit_form_entry_edit_option_html(cls):
        """Edit FormEntry edit option HTML.

        For adding the edit link to edit form entry view.

        :return str:
        """
        return """
        <li><a href="{edit_url}">
          <span class="{edit_option_class}"></span> {edit_text}</a>
        </li>
        """.format(
            edit_url="{edit_url}",
            edit_option_class=cls.form_edit_form_entry_option_class,
            edit_text="{edit_text}",
        )

    @classmethod
    def edit_form_entry_help_text_extra(cls):
        """Edit FormEntry help_text extra.

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
            container_class=cls.form_list_container_class,
            edit_option_html="{edit_option_html}",
            delete_url="{delete_url}",
            delete_option_class=cls.form_delete_form_entry_option_class,
            delete_text="{delete_text}",
            form_element_position="{form_element_position}",
            counter="{counter}",
            form_element_pk="{form_element_pk}",
        )

    def get_view_template_name(self, request=None, origin=None):
        """Get view template name.

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
        """Get edit template name."""
        if not self.edit_template_name_ajax:
            return self.edit_template_name
        elif request and request.is_ajax():
            return self.edit_template_name_ajax
        else:
            return self.edit_template_name

    def collect_plugin_media(self, form_element_entries, request=None):
        """Collect the widget media files.

        :param iterable form_element_entries: Iterable of
            ``fobi.models.FormElementEntry`` instances.
        :param django.http.HttpRequest request:
        :return list:
        """
        plugin_media = collect_plugin_media(
            form_element_entries,
            request=request
        )

        if plugin_media:
            self.plugin_media_js = plugin_media['js']
            self.plugin_media_css = plugin_media['css']

    def get_media_css(self):
        """Get all CSS media files (for the layout + plugins).

        :return list:
        """
        media_css = uniquify_sequence(self.media_css + self.plugin_media_css)

        return media_css

    def get_media_js(self):
        """Get all JavaScript media files (for the layout + plugins).

        :return list:
        """
        media_js = uniquify_sequence(self.media_js + self.plugin_media_js)

        return media_js

    @property
    def primary_html_class(self):
        """Primary HTML class."""
        return 'theme-{0}'.format(self.uid)

    @property
    def html_class(self):
        """HTML classes.

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
    """Not a form actually; defined for magic only.

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
        """Get plugin data.

        :param iterable fields: List of tuples to iterate.
        :param django.http.HttpRequest request:
        :return string: JSON dumped string.
        """
        data = {}

        for field, default_value in fields:
            data.update({field: self.cleaned_data.get(field)})

        if not json_format:
            return data

        return json.dumps(data)

    def get_plugin_data(self, request=None, json_format=True):
        """Get plugin data.

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
        """Save plugin data.

        Dummy, but necessary.
        """

    def validate_plugin_data(self, form_element_entries, request=None):
        """Validate plugin data.

        :param iterable form_element_entries: Iterable of
            ``fobi.models.FormElementEntry``.
        :param django.http.HttpRequest request:
        :return bool:
        """
        return True


class BaseFormFieldPluginForm(BasePluginForm):
    """Base form for form field plugins."""

    plugin_data_fields = [
        ("name", ""),
        ("label", ""),
        ("help_text", ""),
        ("required", False)
    ]

    name = forms.CharField(
        label=_("Name"),
        required=True,
        # widget=forms.widgets.TextInput(attrs={})
    )
    label = forms.CharField(
        label=_("Label"),
        required=True,
        # widget = forms.widgets.TextInput(attrs={})
    )
    help_text = forms.CharField(
        label=_("Help text"),
        required=False,
        widget=forms.widgets.Textarea(attrs={})
    )
    required = forms.BooleanField(
        label=_("Required"),
        required=False,
        # widget = forms.widgets.CheckboxInput(attrs={})
    )

    def validate_plugin_data(self, form_element_entries, request=None):
        """Validate plugin data.

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

    if not DJANGO_GTE_1_8:
        def add_error(self, field, error):
            """Backwards compatibility hack."""
            raise forms.ValidationError(error, 'invalid')

# *****************************************************************************
# *****************************************************************************
# ******************************** Plugins ************************************
# *****************************************************************************
# *****************************************************************************


class BaseDataStorage(object):
    """Base storage data."""


class FormElementPluginDataStorage(BaseDataStorage):
    """Storage for `FormElementPlugin` data."""


class FormHandlerPluginDataStorage(BaseDataStorage):
    """Storage for `FormHandlerPlugin` data."""


class FormWizardHandlerPluginDataStorage(BaseDataStorage):
    """Storage for `FormWizardHandlerPlugin` handler data."""


class FormElementPluginWidgetDataStorage(BaseDataStorage):
    """Storage for `FormElementPluginWidget` data."""


class FormHandlerPluginWidgetDataStorage(BaseDataStorage):
    """Storage for `FormHandlerPluginWidget` data."""


class IntegrationFormElementPluginDataStorage(BaseDataStorage):
    """Storage for `IntegrationFormElementPlugin`."""


class IntegrationFormHandlerPluginDataStorage(BaseDataStorage):
        """Storage for `IntegrationFormHandlerPlugin`."""


class FormWizardHandlerPluginWidgetDataStorage(BaseDataStorage):
    """Storage for `FormWizardHandlerPluginWidget` data."""


class BasePlugin(object):
    """Base plugin.

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
        """Constructor.

        :param django.contrib.auth.models.User user: Plugin owner.
        """
        # Making sure all necessary properties are defined.
        try:
            assert self.uid
            assert self.name
            assert self.storage and issubclass(self.storage, BaseDataStorage)
        except Exception as err:
            raise NotImplementedError(
                "You should define `uid`, `name` and `storage` properties in "
                "your `{0}.{1}` class. {2}".format(
                    self.__class__.__module__,
                    self.__class__.__name__,
                    str(err)
                )
            )
        self.user = user

        # Some initial values
        self.request = None

        self.data = self.storage()

        self._html_id = 'p{0}'.format(uuid.uuid4())

    @property
    def html_id(self):
        """HTML id."""
        return self._html_id

    @property  # Comment the @property if something goes wrong.
    def html_class(self):
        """HTML class.

        A massive work on positioning the plugin and having it to be displayed
        in a given width is done here. We should be getting the plugin widget
        for the plugin given and based on its' properties (static!) as well as
        on plugin position (which we have from model), we can show the plugin
        with the exact class.
        """
        try:
            html_class = [
                'plugin-{0} {1}'.format(
                    self.uid, ' '.join(self.html_classes)
                )
            ]
            return ' '.join(html_class)
        except Exception as err:
            logger.debug(
                "Error in class %s. Details: %s",
                self.__class__.__name__,
                str(err)
            )

    def process(self, plugin_data=None, fetch_related_data=False):
        """Process.

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
                            fetch_related_data=fetch_related_data
                        )
                except Exception as err:
                    logger.debug(
                        "Error in class %s. Details: %s",
                        self.__class__.__name__,
                        str(err)
                    )

            # Calling the post processor.
            self.post_processor()

            return self
        except Exception as err:
            logger.debug(
                "Error in class %s. Details: %s",
                self.__class__.__name__,
                str(err)
            )

    def load_plugin_data(self, plugin_data):
        """Load plugin data.

        Load the plugin data saved in ``fobi.models.FormElementEntry``
        or ``fobi.models.FormHandlerEntry``. Plugin data is saved in JSON
        string.

        :param string plugin_data: JSON string with plugin data.
        """
        self.plugin_data = plugin_data

    def _process_plugin_data(self, fields, fetch_related_data=False):
        """Process plugin data (internal method).

        Override if need customisations.

        Beware, this is not always called.
        """
        for field, default_value in fields:
            try:
                setattr(
                    self.data,
                    field,
                    self.plugin_data.get(field, default_value)
                )
            except Exception:
                setattr(self.data, field, default_value)

    def process_plugin_data(self, fetch_related_data=False):
        """Processes plugin data."""
        form = self.get_form()

        return self._process_plugin_data(
            form.plugin_data_fields,
            fetch_related_data=fetch_related_data
        )

    def _get_plugin_form_data(self, fields):
        """Get plugin form data (used internally).

        :param iterable fields: List of tuples to iterate.
        :return dict:
        """
        form_data = {}
        for field, default_value in fields:
            try:
                form_data.update(
                    {field: self.plugin_data.get(field, default_value)}
                )
            except Exception as err:
                logger.debug(
                    "Error in class %s. Details: %s",
                    self.__class__.__name__,
                    str(err)
                )
        return form_data

    def get_plugin_form_data(self):
        """Get plugin form data.

        Fed as ``initial`` argument to the plugin form when initialising the
        instance for adding or editing the plugin. Override in your plugin
        class if you need customisations.
        """
        form = self.get_form()

        return self._get_plugin_form_data(form.plugin_data_fields)

    def get_instance(self):
        """Get instance."""
        return None

    def get_form(self):
        """Get the plugin form class.

        Override this method in your subclassed ``fobi.base.BasePlugin`` class
        when you need your plugin setup to vary depending on the placeholder,
        workspace, user or request given. By default returns the value of the
        ``form`` attribute defined in your plugin.

        :return django.forms.Form|django.forms.ModelForm: Subclass of
            ``django.forms.Form`` or ``django.forms.ModelForm``.
        """
        return self.form

    def get_initialised_create_form(self, data=None, files=None,
                                    initial_data=None):
        """Get initialized create form.

        Used ``fobi.views.add_form_element_entry`` and
        ``fobi.views.add_form_handler_entry`` view to gets initialised form
        for object to be created.
        """
        plugin_form = self.get_form()
        if plugin_form:
            try:
                kwargs = {
                    'data': data,
                    'files': files,
                }
                if initial_data:
                    kwargs.update({'initial': initial_data})
                return plugin_form(**kwargs)
            except Exception as err:
                if DEBUG:
                    logger.debug(err)
                raise Http404(err)

    def get_initialised_create_form_or_404(self, data=None, files=None):
        """Get initialized create form or page 404.

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
                    data=data,
                    files=files,
                    initial_data=initial_data
                )
            except Exception as err:
                if DEBUG:
                    logger.debug(err)
                raise Http404(err)

    def get_initialised_edit_form(self, data=None, files=None,
                                  auto_id='id_%s', prefix=None, initial=None,
                                  error_class=ErrorList, label_suffix=':',
                                  empty_permitted=False, instance=None):
        """Get initialized edit form.

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
        """Get initialized edit form or page 404.

        Same as ``get_initialised_edit_form`` but raises
        ``django.http.Http404`` on errors.
        """
        plugin_form = self.get_form()
        if plugin_form:
            try:
                return self.get_initialised_edit_form(
                    data=data,
                    files=files,
                    auto_id=auto_id,
                    prefix=prefix,
                    initial=self.get_plugin_form_data(),
                    error_class=error_class,
                    label_suffix=label_suffix,
                    empty_permitted=empty_permitted,
                    instance=self.get_instance()
                )
            except Exception as err:
                if DEBUG:
                    logger.debug(err)
                raise Http404(err)

    def get_widget(self, request=None, as_instance=False):
        """Get the plugin widget.

        :param django.http.HttpRequest request:
        :param bool as_instance:
        :return mixed: Subclass of `fobi.base.BasePluginWidget` or instance
            of subclassed `fobi.base.BasePluginWidget` object.
        """
        raise NotImplementedError

    def render(self, request=None):
        """Renders the plugin HTML.

        :param django.http.HttpRequest request:
        :return string:
        """
        widget_cls = self.get_widget()

        if widget_cls:
            widget = widget_cls(self)

            render = widget.render(request=request)
            return render or ''
        elif DEBUG:
            logger.debug("No widget defined for %s.", self.uid)

    def _update_plugin_data(self, entry):
        """Update plugin data (internal method).

        For private use. Do not override this method. Override
        `update_plugin_data` instead.
        """
        try:
            updated_plugin_data = self.update_plugin_data(entry)
            plugin_data = self.get_updated_plugin_data(
                update=updated_plugin_data
            )
            return self.save_plugin_data(entry, plugin_data=plugin_data)
        except Exception as err:
            logging.debug(str(err))

    def update_plugin_data(self, entry):
        """Update plugin data.

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
        """Delete plugin data (internal method).

        For private use. Do not override this method. Override
        `delete_plugin_data` instead.
        """
        try:
            self.delete_plugin_data()
        except Exception as err:
            logging.debug(str(err))

    def delete_plugin_data(self):
        """Delete plugin data (internal method).

        Used in ``fobi.views.delete_form_entry`` and
        ``fobi.views.delete_form_handler_entry``. Fired automatically, when
        ``fobi.models.FormEntry`` object is about to be deleted. Make use of
        it if your plugin creates database records or files that are not
        monitored externally but by fobi only.
        """

    def _clone_plugin_data(self, entry):
        """Clone plugin data (internal method).

        For private use. Do not override this method. Override
        `clone_plugin_data` instead.
        """
        try:
            return self.clone_plugin_data(entry)
        except Exception as err:
            logging.debug(str(err))

    def clone_plugin_data(self, entry):
        """Clone plugin data.

        Used when copying entries. If any objects or files are created by
        plugin, they should be cloned.

        :param fobi.models.AbstractPluginEntry: Instance of
            ``fobi.models.AbstractPluginEntry``.
        :return string: JSON dumped string of the cloned plugin data. The
            returned value would be inserted as is into the
            `fobi.models.AbstractPluginEntry.plugin_data` field.
        """

    def get_cloned_plugin_data(self, update={}):
        """Get cloned plugin data.

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
        >>>     )
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
        """Get updated plugin data.

        Returns it in a JSON dumped format.

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
        """Pre-processor (callback).

        Redefine in your subclassed plugin when necessary.

        Pre process plugin data (before rendering). This method is being
        called before the data has been loaded into the plugin.

        Note, that request (django.http.HttpRequest) is available (
        self.request).
        """

    def post_processor(self):
        """Post-processor (self).

        Redefine in your subclassed plugin when necessary.

        Post process plugin data here (before rendering). This method is
        being called after the data has been loaded into the plugin.

        Note, that request (django.http.HttpRequest) is available
        (self.request).
        """

    def plugin_data_repr(self):
        """Plugin data repr.

        Human readable representation of plugin data. A very basic
        way would be just:

        >>> return self.data.__dict__

        :return string:
        """


class FormElementPlugin(BasePlugin):
    """Base form element plugin.

    :property fobi.base.FormElementPluginDataStorage storage:
    :property bool has_value: If set to False, ignored (removed)
        from the POST when processing the form.
    """

    storage = FormElementPluginDataStorage
    has_value = False
    is_hidden = False

    def _get_form_field_instances(self, form_element_entry=None, origin=None,
                                  kwargs_update_func=None, return_func=None,
                                  extra={}, request=None, form_entry=None,
                                  form_element_entries=None, **kwargs):
        """Get form field instances (internal method).

        Used internally. Do not override this method. Gets the instances of
        form fields, that plugin contains.

        :param fobi.models.FormElementEntry form_element_entry: Instance.
        :param string origin:
        :param callable kwargs_update_func:
        :param callable return_func:
        :param dict extra:
        :param django.http.HttpRequest request:
        :param fobi.models.FormEntry form_entry:
        :param django.db.models.QuerySet form_element_entries: Queryset of
            :class:`fobi.models.FormElementEntry` instances.
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
        if DEBUG:
            form_field_instances = self.get_form_field_instances(
                request=request,
                form_entry=form_entry,
                form_element_entries=form_element_entries,
                **kwargs
            )
        else:
            try:
                form_field_instances = self.get_form_field_instances(
                    request=request,
                    form_entry=form_entry,
                    form_element_entries=form_element_entries,
                    **kwargs
                )
            except AttributeError as err:
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
                    # more ("Dynamic initial values" section).
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
                extra=extra,
                widget_cls=Widget
            )

            # if 'widget' in field_kwargs:
            #    field_kwargs['widget'] = assemble_form_field_widget_class(
            #        base_class=field_kwargs['widget'],
            #        plugin=self
            #    )
            if kwargs_update:
                field_kwargs.update(kwargs_update)

            processed_field_instances.append(
                (field_name, Field(**field_kwargs))
            )

        return processed_field_instances

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get the instances of form fields, that plugin contains.

        :param django.http.HttpRequest request:
        :param fobi.models.FormEntry form_entry:
        :param django.db.models.QuerySet form_element_entries: Queryset of
            :class:`fobi.models.FormElementEntry` instances.
        :return list: List of Django form field instances.

        :example:
        >>> from django.forms.fields import CharField, IntegerField, TextField
        >>> [CharField(max_length=100), IntegerField(), TextField()]
        """
        return []

    def get_custom_field_instances(self,
                                   integrate_with,
                                   request=None,
                                   form_entry=None,
                                   form_element_entries=None,
                                   has_value=None,
                                   **kwargs):
        """Get custom field instances.

        :param str integrate_with:
        :param django.http.HttpRequest request:
        :param form_entry:
        :param form_element_entries:
        :param bool has_value: If not None, used for filtering out.
        :return list:
        """
        cls = integration_form_element_plugin_registry.get(
            integrate_with, self.uid
        )

        if cls:

            if has_value is not None:
                if cls.has_value != has_value:
                    return []

            plugin = cls()
            return plugin.get_custom_field_instances(
                form_element_plugin=self,
                request=request,
                form_entry=form_entry,
                form_element_entries=form_element_entries,
                **kwargs
            )
        return []

    def _get_custom_field_instances(self,
                                    integrate_with,
                                    form_element_entry=None,
                                    origin=None,
                                    kwargs_update_func=None,
                                    return_func=None,
                                    extra={},
                                    request=None,
                                    form_entry=None,
                                    form_element_entries=None,
                                    has_value=None,
                                    **kwargs):

        """Gets the instances of form fields, that plugin contains.

        Used internally. Do not override this method.

        :param str integrate_with:s
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
        if DEBUG:
            custom_field_instances = self.get_custom_field_instances(
                integrate_with=integrate_with,
                request=request,
                form_entry=form_entry,
                form_element_entries=form_element_entries,
                has_value=has_value,
                **kwargs
            )
        else:
            try:
                custom_field_instances = self.get_custom_field_instances(
                    integrate_with=integrate_with,
                    request=request,
                    form_entry=form_entry,
                    form_element_entries=form_element_entries,
                    has_value=has_value,
                    **kwargs
                )
            except AttributeError:
                return []

        # This is the flexible part. We delegate implementation to the
        # plugin.
        processed_custom_field_instances = []
        # Actually, ``custom_field_instance`` isn't a good name, since
        # here we actually deal with sub-classed
        # ``CustomFormFieldInstanceProcessor`` instances.
        for custom_field_instance in custom_field_instances:
            processed_custom_field_instances.append(
                custom_field_instance.process_custom_form_field_instance(
                    form_element_entry=form_element_entry,
                    form_entry=form_entry,
                    request=request,
                    form_element_plugin=self
                )
            )

        return processed_custom_field_instances

    def get_origin_return_func_results(self, return_func, form_element_entry,
                                       origin):
        """Get origin return func results.

        If ``return_func`` is given, is callable and returns results without
        failures, return the result. Otherwise - return None.
        """
        # Check hooks
        if return_func and callable(return_func):
            try:
                return return_func(
                    form_element_plugin=self,
                    form_element_entry=form_element_entry,
                    origin=origin
                )
            except Exception:
                pass

    def get_origin_kwargs_update_func_results(self, kwargs_update_func,
                                              form_element_entry, origin,
                                              extra={}, widget_cls=None):
        """Get origin kwargs update func results.

        If ``kwargs_update_func`` is given, is callable and returns results
        without failures, return the result. Otherwise - return None.
        """
        # Check hooks
        if kwargs_update_func and callable(kwargs_update_func):
            try:
                kwargs_update = kwargs_update_func(
                    form_element_plugin=self,
                    form_element_entry=form_element_entry,
                    origin=origin,
                    extra=extra,
                    widget_cls=widget_cls
                )
                if kwargs_update:
                    return kwargs_update
            except Exception as err:
                if FAIL_ON_ERRORS_IN_FORM_ELEMENT_PLUGINS:
                    raise err
                else:
                    logger.error(str(err))
        return {}

    def _submit_plugin_form_data(self, form_entry, request, form,
                                 form_element_entries=None, **kwargs):
        """Submit plugin form data (internal method).

        Do not override this method. Use ``submit_plugin_form_data``,
        instead.

        Submit plugin form data. Called on form submission (when user actually
        posts the data to assembled form).

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        :param iterable form_element_entries:
        """
        if DEBUG:
            return self.submit_plugin_form_data(
                form_entry=form_entry,
                request=request,
                form=form,
                form_element_entries=form_element_entries,
                **kwargs
            )
        else:
            try:
                return self.submit_plugin_form_data(
                    form_entry=form_entry,
                    request=request,
                    form=form,
                    form_element_entries=form_element_entries,
                    **kwargs
                )
            except Exception as err:
                logger.debug(str(err))

    def submit_plugin_form_data(self, form_entry, request, form,
                                form_element_entries=None, **kwargs):
        """Submit plugin form data.

        Called on form submission (when user actually
        posts the data to assembled form).

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        :param iterable form_element_entries:
        """


class FormFieldPlugin(FormElementPlugin):
    """Form field plugin."""

    has_value = True


class FormHandlerPlugin(BasePlugin):
    """Form handler plugin.

    :property fobi.base.FormHandlerPluginDataStorage storage:
    :property bool allow_multiple: If set to True, plugin can be used multiple
        times within (per form). Otherwise - just once.
    """

    storage = FormHandlerPluginDataStorage
    allow_multiple = True

    def _run(self, form_entry, request, form, form_element_entries=None):
        """Run (internal method).

        Safely call the ``run`` method.

        Note, that we DO need `form_element_entries` in any case to
        determine the form elements that do have value (or form elements
        that matter). We do need this in both, form handlers and form wizard
        handlers.

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

        if FAIL_ON_ERRORS_IN_FORM_HANDLER_PLUGINS:
            response = self.run(form_entry, request, form,
                                form_element_entries)
            if response:
                return response
            else:
                return (True, None)
        else:
            try:
                response = self.run(form_entry, request, form,
                                    form_element_entries)
                if response:
                    return response
                else:
                    return (True, None)
            except Exception as err:
                logger.error(
                    "Error in class %s. Details: %s. Full trace: %s",
                    self.__class__.__name__,
                    str(err),
                    traceback.format_exc()
                )
                return (False, err)

    def run(self, form_entry, request, form, form_element_entries=None):
        """Run.

        Custom code should be implemented here.

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        :param iterable form_element_entries: Iterable of
            ``fobi.models.FormElementEntry`` objects.
        :return mixed: May be a tuple (bool, mixed) or None
        """
        raise NotImplementedError(
            "You should implement ``run`` method in your {0} "
            "subclass.".format(self.__class__.__name__)
        )

    def run_integration_handler(self,
                                integrate_with,
                                form_entry,
                                request,
                                form_element_entries=None,
                                **kwargs):
        """Run integration handler."""
        cls = integration_form_handler_plugin_registry.get(
            integrate_with,
            self.uid
        )
        if cls:
            plugin = cls()
            response = plugin.run(
                form_handler_plugin=self,
                form_entry=form_entry,
                request=request,
                form_element_entries=form_element_entries,
                **kwargs
            )
            if response:
                return response
            else:
                return True, None
        return (
            False,
            _("No integration handler for plugin {} found.").format(self.uid)
        )

    def _run_integration_handler(self,
                                 integrate_with,
                                 form_entry,
                                 request,
                                 form_element_entries=None,
                                 **kwargs):
        """Run integration handlers."""
        if DEBUG:
            return self.run_integration_handler(
                integrate_with=integrate_with,
                form_entry=form_entry,
                request=request,
                form_element_entries=form_element_entries,
                **kwargs
            )
        else:
            try:
                return self.run_integration_handler(
                    integrate_with=integrate_with,
                    form_entry=form_entry,
                    request=request,
                    form_element_entries=form_element_entries,
                    **kwargs
                )
            except Exception as err:
                return False, err

    def custom_actions(self, form_entry, request=None):
        """Custom actions.

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
        """Internal method to for obtaining the ``get_custom_actions``."""
        return self.custom_actions(form_entry, request)


class FormWizardHandlerPlugin(BasePlugin):
    """Form wizard handler plugin.

    :property fobi.base.FormWizardHandlerPluginDataStorage storage:
    :property bool allow_multiple: If set to True, plugin can be used multiple
        times within (per form). Otherwise - just once.

    DONE
    """

    storage = FormWizardHandlerPluginDataStorage
    allow_multiple = True

    def _run(self, form_wizard_entry, request, form_list, form_wizard,
             form_element_entries=None):
        """Run (internal method).

        Safely call the ``run`` method.

        :param fobi.models.FormEntry form_wizard_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        :param iterable form_element_entries: Iterable of
            ``fobi.models.FormElementEntry`` objects.
        :return tuple:
        """
        # For backwards compatibility.
        if not form_element_entries:
            form_element_entries = \
                get_form_element_entries_for_form_wizard_entry(
                    form_wizard_entry
                )

        try:
            response = self.run(form_wizard_entry,
                                request,
                                form_list,
                                form_wizard,
                                form_element_entries)
            if response:
                return response
            else:
                return (True, None)
        except Exception as err:
            if FAIL_ON_ERRORS_IN_FORM_WIZARD_HANDLER_PLUGINS:
                raise err.__class__(
                    "Exception: %s. %s",
                    str(err),
                    traceback.format_exc()
                )
            logger.error(
                "Error in class %s. Details: %s. Full trace: %s",
                self.__class__.__name__,
                str(err),
                traceback.format_exc()
            )
            return (False, err)

    def run(self, form_wizard_entry, request, form_list, form_wizard,
            form_element_entries=None):
        """Run.

        Custom code should be implemented here.

        :param fobi.models.FormEntry form_wizard_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        :param iterable form_element_entries: Iterable of
            ``fobi.models.FormElementEntry`` objects.
        :return mixed: May be a tuple (bool, mixed) or None
        """
        raise NotImplementedError(
            "You should implement ``run`` method in your %s subclass.",
            self.__class__.__name__
        )

    def custom_actions(self, form_wizard_entry, request=None):
        """Custom actions.

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

    def get_custom_actions(self, form_wizard_entry, request=None):
        """Internal method to for obtaining the ``get_custom_actions``."""
        return self.custom_actions(form_wizard_entry, request)


class IntegrationFormElementPluginProcessor(object):
    """Custom form field instance processor.

    Supposed to have implemented a single method called
    ``process_custom_form_field_instance``.
    """

    def __init__(self, *args, **kwargs):
        """Constructor."""
        self.args = args
        self.kwargs = kwargs

    def process_custom_form_field_instance(self,
                                           form_element_entry,
                                           form_entry,
                                           request,
                                           form_element_plugin):
        """You should implement this method in your implementation."""
        raise NotImplementedError("You should implement this method!")


class BaseIntegrationFormElementPlugin(BasePlugin):
    """Base custom field instance plugin."""

    storage = IntegrationFormElementPluginDataStorage
    integrate_with = None
    has_value = False
    is_hidden = False

    def __init__(self, user=None):
        """Constructor."""
        super(BaseIntegrationFormElementPlugin, self).__init__(user=user)
        assert self.integrate_with


class IntegrationFormElementPlugin(BasePlugin):
    """Base custom field instance plugin for integration."""

    storage = IntegrationFormElementPluginDataStorage
    has_value = False
    is_hidden = False


class IntegrationFormFieldPlugin(IntegrationFormElementPlugin):
    """Integration form field plugin for custom field instances."""

    has_value = True


class BaseIntegrationFormHandlerPlugin(BasePlugin):
    """Base integration form handler plugin."""

    storage = IntegrationFormHandlerPluginDataStorage
    integrate_with = None
    has_value = False
    is_hidden = False

    def __init__(self, user=None):
        """Constructor."""
        super(BaseIntegrationFormHandlerPlugin, self).__init__(user=user)
        assert self.integrate_with


class IntegrationFormHandlerPlugin(BasePlugin):
    """Base integration form handler plugin for integration."""

    storage = IntegrationFormHandlerPluginDataStorage
    has_value = True
    is_hidden = False


class BaseFormCallback(object):
    """Base form callback."""

    stage = None

    def __init__(self):
        """Constructor."""
        assert self.stage in CALLBACK_STAGES


class FormCallback(BaseFormCallback):
    """Form callback."""

    def _callback(self, form_entry, request, form):
        """Callback (internal method).

        Calling the ``callback`` method in a safe way.
        """
        try:
            return self.callback(form_entry, request, form)
        except Exception as err:
            logger.debug(
                "Error in class %s. Details: %s",
                self.__class__.__name__,
                str(err)
            )

    def callback(self, form_entry, request, form):
        """Callback.

        Custom callback code should be implemented here.

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        """
        raise NotImplementedError(
            "You should implement ``callback`` method in your {0} "
            "subclass.".format(self.__class__.__name__)
        )


class IntegrationFormCallback(object):
    """Integration form callback."""

    integrate_with = None

    def __init__(self):
        """Constructor."""
        assert self.stage in CALLBACK_STAGES
        assert self.integrate_with is not None

    def _callback(self, form_entry, request, **kwargs):
        """Callback (internal method).

        Calling the ``callback`` method in a safe way.
        """
        try:
            return self.callback(form_entry, request, **kwargs)
        except Exception as err:
            logger.debug(
                "Error in class %s. Details: %s",
                self.__class__.__name__,
                str(err)
            )

    def callback(self, form_entry, request, **kwargs):
        """Callback.

        Custom callback code should be implemented here.

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        """
        raise NotImplementedError(
            "You should implement ``callback`` method in your {0} "
            "subclass.".format(self.__class__.__name__)
        )


class ClassProperty(property):
    """ClassProperty."""

    def __get__(self, cls, owner):
        """Get."""
        return classmethod(self.fget).__get__(None, owner)()


classproperty = ClassProperty


class BasePluginWidget(object):
    """Base form element plugin widget.

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
        """Constructor."""
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
        """HTML class of the ``fobi.base.BaseFormElementPluginWidget``.

        :return string:
        """
        return ' '.join(cls.html_classes)


class FormElementPluginWidget(BasePluginWidget):
    """Form element plugin widget."""

    storage = FormElementPluginWidgetDataStorage


class FormHandlerPluginWidget(BasePluginWidget):
    """Form handler plugin widget."""

    storage = FormHandlerPluginWidgetDataStorage


class FormWizardHandlerPluginWidget(BasePluginWidget):
    """Form wizard handler plugin widget."""

    storage = FormWizardHandlerPluginWidgetDataStorage


# *****************************************************************************
# *****************************************************************************
# ******************************* Registry ************************************
# *****************************************************************************
# *****************************************************************************

class BaseRegistry(object):
    """Base registry.

    Registry of plugins. It's essential, that class registered has the
    ``uid`` property.

    If ``fail_on_missing_plugin`` is set to True, an appropriate exception
    (``plugin_not_found_exception_cls``) is raised in cases if plugin could't
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
        """Constructor."""
        assert self.type
        self._registry = {}
        self._forced = []

    @property
    def registry(self):
        """Shortcut to self._registry."""
        return self._registry

    def items(self):
        """Shortcut to self._registry.items()."""
        return self._registry.items()

    def register(self, cls, force=False):
        """Registers the plugin in the registry.

        :param mixed cls:
        :param bool force:
        """
        if not issubclass(cls, self.type):
            raise InvalidRegistryItemType(
                "Invalid item type `{0}` for registry "
                "`{1}`".format(cls, self.__class__)
            )

        # If item has not been forced yet, add/replace its' value in the
        # registry.
        if force:

            if cls.uid not in self._forced:
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
        """Un-register."""
        if not issubclass(cls, self.type):
            raise InvalidRegistryItemType(
                "Invalid item type `{0}` for registry "
                "`{1}`".format(cls, self.__class__)
            )

        # Only non-forced items are allowed to be unregistered.
        if cls.uid in self._registry and cls.uid not in self._forced:
            self._registry.pop(cls.uid)
            return True
        else:
            return False

    def get(self, uid, default=None):
        """Get the given entry from the registry.

        :param string uid:
        :param mixed default:
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
    """Form element plugins registry."""

    type = (FormElementPlugin, FormFieldPlugin)
    fail_on_missing_plugin = FAIL_ON_MISSING_FORM_ELEMENT_PLUGINS
    plugin_not_found_exception_cls = FormElementPluginDoesNotExist


class FormHandlerPluginRegistry(BaseRegistry):
    """Form handler plugins registry."""

    type = FormHandlerPlugin
    fail_on_missing_plugin = FAIL_ON_MISSING_FORM_HANDLER_PLUGINS
    plugin_not_found_exception_cls = FormHandlerPluginDoesNotExist


class BaseIntegrationPluginRegistry(object):
    """Base integration plugin registry."""

    plugin_not_found_error_message = "Can't find plugin with uid `{0}` in " \
                                     "`{1}` registry."

    def __init__(self):
        super(BaseIntegrationPluginRegistry, self).__init__()
        self._registry = defaultdict(dict)
        self._forced = defaultdict(dict)

    @property
    def registry(self):
        """Shortcut to self._registry."""
        return self._registry

    def items(self):
        """Shortcut to self._registry.items()."""
        return self._registry.items()

    def register(self, cls, force=False):
        """Registers the plugin in the registry.

        :param mixed cls:
        :param bool force:
        """
        if not issubclass(cls, self.type):
            raise InvalidRegistryItemType(
                "Invalid item type `{0}` for registry "
                "`{1}`".format(cls, self.__class__)
            )

        # If item has not been forced yet, add/replace its' value in the
        # registry.
        if force:

            if cls.uid not in self._forced:
                self._registry[cls.integrate_with][cls.uid] = cls
                self._forced[cls.integrate_with].append(cls.uid)
                return True
            else:
                return False

        else:

            if cls.uid in self._registry[cls.integrate_with]:
                return False
            else:
                self._registry[cls.integrate_with][cls.uid] = cls
                return True

    def unregister(self, cls):
        """Un-register."""
        if not issubclass(cls, self.type):
            raise InvalidRegistryItemType(
                "Invalid item type `{0}` for registry "
                "`{1}`".format(cls, self.__class__)
            )

        # Only non-forced items are allowed to be unregistered.
        if cls.uid in self._registry[cls.integrate_with] \
                and cls.uid not in self._forced[cls.integrate_with]:
            self._registry[cls.integrate_with].pop(cls.uid)
            return True
        else:
            return False

    def get(self, integrate_with, uid, default=None):
        """Get the given entry from the registry.

        :param str integrate_with:
        :param str uid:
        :param mixed default:
        :return mixed.
        """
        item = self._registry[integrate_with].get(uid, default)

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


class IntegrationFormElementPluginRegistry(BaseIntegrationPluginRegistry):
    """Integration form element plugin registry."""
    type = (IntegrationFormElementPlugin,)
    fail_on_missing_plugin = FAIL_ON_MISSING_INTEGRATION_FORM_ELEMENT_PLUGINS
    plugin_not_found_exception_cls = IntegrationFormElementPluginDoesNotExist


class IntegrationFormHandlerPluginRegistry(BaseIntegrationPluginRegistry):
    """Integration form handler plugin registry."""
    type = (IntegrationFormHandlerPlugin,)
    # TODO
    fail_on_missing_plugin = FAIL_ON_MISSING_INTEGRATION_FORM_HANDLER_PLUGINS
    # TODO
    plugin_not_found_exception_cls = IntegrationFormHandlerPluginDoesNotExist


class FormWizardHandlerPluginRegistry(BaseRegistry):
    """Form wizard handler plugins registry."""

    type = FormWizardHandlerPlugin
    fail_on_missing_plugin = FAIL_ON_MISSING_FORM_WIZARD_HANDLER_PLUGINS
    plugin_not_found_exception_cls = FormWizardHandlerPluginDoesNotExist


class ThemeRegistry(BaseRegistry):
    """Themes registry."""
    type = BaseTheme


class FormCallbackRegistry(object):
    """Registry of callbacks.

    Holds callbacks for stages listed in the
    ``fobi.constants.CALLBACK_STAGES``.
    """

    def __init__(self):
        """Constructor."""
        self._registry = {}

        for stage in CALLBACK_STAGES:
            self._registry[stage] = []

    def uidfy(self, cls):
        """Makes a UID string from the class given.

        :param mixed cls:
        :return string:
        """
        return "{0}.{1}".format(cls.__module__, cls.__name__)

    def register(self, cls):
        """Registers the plugin in the registry.

        :param mixed cls:
        """
        if not issubclass(cls, FormCallback):
            raise InvalidRegistryItemType(
                "Invalid item type `{0}` for registry "
                "`{1}`".format(cls, self.__class__)
            )

        # uid = self.uidfy(cls)
        # If item has not been forced yet, add/replace its' value in the
        # registry.

        if cls in self._registry[cls.stage]:
            return False
        else:
            self._registry[cls.stage].append(cls)
            return True

    def get_callbacks(self, stage=None):
        """Get callbacks for the stage given.

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


class IntegrationFormCallbackRegistry(object):
    """Registry of callbacks for integration plugins.

    Holds callbacks for stages listed in the
    ``fobi.constants.CALLBACK_STAGES``.
    """

    def __init__(self):
        """Constructor."""
        self._registry = defaultdict(lambda: defaultdict(list))

    @property
    def registry(self):
        return self._registry

    def uidfy(self, cls):
        """Makes a UID string from the class given.

        :param mixed cls:
        :return string:
        """
        return "{0}.{1}".format(cls.__module__, cls.__name__)

    def register(self, cls):
        """Registers the plugin in the registry.

        :param mixed cls:
        """
        if not issubclass(cls, IntegrationFormCallback):
            raise InvalidRegistryItemType(
                "Invalid item type `{0}` for registry "
                "`{1}`".format(cls, self.__class__)
            )
        if cls in self._registry[cls.integrate_with][cls.stage]:
            return False
        else:
            self._registry[cls.integrate_with][cls.stage].append(cls)
            return True

    def get_callbacks(self, integrate_with, stage=None):
        """Get callbacks for the stage given.

        :param str integrate_with:
        :param string stage:
        :return list:
        """
        if stage:
            return self._registry[integrate_with].get(stage, [])
        else:
            callbacks = []
            for stage_callbacks in self._registry[integrate_with].values():
                callbacks += stage_callbacks
            return callbacks


class BasePluginWidgetRegistry(object):
    """Registry of plugins widgets (renderers)."""
    type = None

    def __init__(self):
        assert self.type
        self._registry = {}
        self._forced = []

    @staticmethod
    def namify(theme, plugin_uid):
        """Namify."""
        return '{0}.{1}'.format(theme, plugin_uid)

    def register(self, cls, force=False):
        """Register the plugin renderer in the registry.

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

            if uid not in self._forced:
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
        """Un-register."""
        if not issubclass(cls, self.type):
            raise InvalidRegistryItemType(
                "Invalid item type `{0}` for registry "
                "`{1}`".format(cls, self.__class__)
            )

        uid = BasePluginWidgetRegistry.namify(cls.theme_uid, cls.plugin_uid)

        # Only non-forced items are allowed to be unregistered.
        if uid in self._registry and uid not in self._forced:
            self._registry.pop(uid)
            return True
        else:
            return False

    def get(self, uid, default=None):
        """Get the given entry from the registry.

        :param string uid:
        :return mixed:
        """
        item = self._registry.get(uid, default)
        if not item:
            logger.debug(
                "Can't find plugin widget with uid `%s` in `%s` registry",
                uid,
                self.__class__
            )
        return item


class FormElementPluginWidgetRegistry(BasePluginWidgetRegistry):
    """Registry of form element plugins."""

    type = FormElementPluginWidget


class FormHandlerPluginWidgetRegistry(BasePluginWidgetRegistry):
    """Registry of form handler plugins."""

    type = FormHandlerPluginWidget


class FormWizardHandlerPluginWidgetRegistry(BasePluginWidgetRegistry):
    """Registry of form wizard handler plugins."""

    type = FormWizardHandlerPluginWidget


# Register form field plugins by calling form_field_plugin_registry.register()
form_element_plugin_registry = FormElementPluginRegistry()

# Register action plugins by calling form_action_plugin_registry.register()
form_handler_plugin_registry = FormHandlerPluginRegistry()

# Register integration form element plugins by calling
# integration_form_element_plugin_registry.register()
integration_form_element_plugin_registry = \
    IntegrationFormElementPluginRegistry()

# Register integration form handler plugins by calling
# integration_form_handler_plugin_registry.register()
integration_form_handler_plugin_registry = \
    IntegrationFormHandlerPluginRegistry()

# Register action plugins by calling form_action_plugin_registry.register()
form_wizard_handler_plugin_registry = FormWizardHandlerPluginRegistry()

# Register themes by calling theme_registry.register()
theme_registry = ThemeRegistry()

# Register action plugins by calling form_action_plugin_registry.register()
form_callback_registry = FormCallbackRegistry()

# Register action plugins by calling form_action_plugin_registry.register()
integration_form_callback_registry = IntegrationFormCallbackRegistry()

# Register plugin widgets by calling
# form_element_plugin_widget_registry.register()
form_element_plugin_widget_registry = FormElementPluginWidgetRegistry()

# Register plugin widgets by calling
# form_handler_plugin_widget_registry.register()
form_handler_plugin_widget_registry = FormHandlerPluginWidgetRegistry()

# Register plugin widgets by calling
# form_wizard_handler_plugin_widget_registry.register()
form_wizard_handler_plugin_widget_registry = \
    FormWizardHandlerPluginWidgetRegistry()

# *****************************************************************************
# *****************************************************************************
# ******************************** Helpers ************************************
# *****************************************************************************
# *****************************************************************************


def ensure_autodiscover():
    """Ensure that plugins are auto-discovered.

    The form callbacks registry is intentionally left out, since they will be
    auto-discovered in any case if other modules are discovered.
    """
    if not (form_element_plugin_registry._registry
            and form_handler_plugin_registry._registry
            and theme_registry._registry):
        autodiscover()


def assemble_form_field_widget_class(base_class, plugin):
    """Assemble form field widget class.

    Finish this or remove.

    #TODO
    """
    class DeclarativeMetaclass(type):
        """Wrapped class."""

        def __new__(cls, name, bases, attrs):
            """New."""
            new_class = super(DeclarativeMetaclass, cls).__new__(
                cls, name, bases, attrs
            )
            return new_class

        def render(self, name, value, attrs=None, **kwargs):
            """Smart render."""
            widget = plugin.get_widget()
            if widget.hasattr('render') and callable(widget.render):
                return widget.render(name, value, attrs=attrs)
            else:
                super(DeclarativeMetaclass, self).render(
                    name, value, attrs=attrs, **kwargs
                )

    class WrappedWidget(with_metaclass(DeclarativeMetaclass, base_class)):
        """
        Dynamically created form element plugin class.
        """

    return WrappedWidget

# *****************************************************************************
# *********************************** Generic *********************************
# *****************************************************************************


def get_registered_plugins(registry, as_instances=False, sort_items=True):
    """Get registered plugins.

    Get a list of registered plugins in a form of tuple (plugin name, plugin
    description). If not yet auto-discovered, auto-discovers them.

    :param registry:
    :param bool as_instances:
    :param bool sort_items:
    :return list:
    """
    ensure_autodiscover()

    if as_instances:
        return registry._registry

    registered_plugins = []

    for uid, plugin in registry._registry.items():
        plugin_name = safe_text(plugin.name)
        registered_plugins.append((uid, plugin_name))

    if sort_items:
        registered_plugins.sort()

    return registered_plugins


def get_registered_plugins_grouped(registry,
                                   sort_items=True,
                                   sort_by_value=SORT_PLUGINS_BY_VALUE):
    """Get registered plugins grouped.

    Gets a list of registered plugins in a form of tuple (plugin name, plugin
    description). If not yet auto-discovered, auto-discovers them.

    :return dict:
    """
    ensure_autodiscover()

    registered_plugins = {}

    for uid, plugin in registry._registry.items():
        plugin_name = safe_text(plugin.name)
        plugin_group = safe_text(plugin.group)

        if plugin_group not in registered_plugins:
            registered_plugins[plugin_group] = []
        registered_plugins[plugin_group].append((uid, plugin_name))

    if not sort_items:
        return registered_plugins

    ordered_registered_plugins = OrderedDict()
    for key, prop in sorted(registered_plugins.items()):
        if sort_by_value:
            ordered_registered_plugins[key] = sorted(prop, key=lambda t: t[1])
        else:
            ordered_registered_plugins[key] = sorted(prop)

    return ordered_registered_plugins


def get_registered_plugin_uids(registry, flattern=True, sort_items=True):
    """Get a list of registered plugin uids as a list .

    If not yet auto-discovered, auto-discovers them.

    The `sort_items` is applied only if `flattern` is True.

    :param registry:
    :param bool flattern:
    :param bool sort_items:
    :return list:
    """
    ensure_autodiscover()

    registered_plugin_uids = registry._registry.keys()

    if flattern:
        registered_plugin_uids = list(registered_plugin_uids)
        if sort_items:
            registered_plugin_uids.sort()

    return registered_plugin_uids


def validate_plugin_uid(registry, plugin_uid):
    """Validate the plugin uid.

    :param string plugin_uid:
    :return bool:
    """
    return plugin_uid in get_registered_plugin_uids(registry, flattern=True)

# *****************************************************************************
# ***************************** Form element specific *************************
# *****************************************************************************


def get_registered_form_element_plugins():
    """Get registered form element plugins.

    Gets a list of registered plugins in a form of tuple (plugin name, plugin
    description). If not yet auto-discovered, auto-discovers them.

    :return list:
    """
    return get_registered_plugins(form_element_plugin_registry)


def get_registered_form_element_plugins_grouped(
        sort_by_value=SORT_PLUGINS_BY_VALUE
):
    """Get registered form element plugins grouped.

    Gets a list of registered plugins in a form of tuple (plugin name, plugin
    description). If not yet auto-discovered, auto-discovers them.

    :return dict:
    """
    return get_registered_plugins_grouped(
        form_element_plugin_registry,
        sort_by_value=sort_by_value
    )


def get_registered_form_element_plugin_uids(flattern=True):
    """Get registered form element plugin uids.

    Gets a list of registered plugins in a form of tuple (plugin name, plugin
    description). If not yet auto-discovered, auto-discovers them.

    :return list:
    """
    return get_registered_plugin_uids(
        form_element_plugin_registry, flattern=flattern
    )


def validate_form_element_plugin_uid(plugin_uid):
    """Validate the form element plugin uid.

    :param string plugin_uid:
    :return bool:
    """
    return validate_plugin_uid(form_element_plugin_registry, plugin_uid)


def submit_plugin_form_data(form_entry, request, form,
                            form_element_entries=None, **kwargs):
    """Submit plugin form data for all plugins.

    :param fobi.models.FormEntry form_entry: Instance of
        ``fobi.models.FormEntry``.
    :param django.http.HttpRequest request:
    :param django.forms.Form form:
    :param iterable form_element_entries:
    """
    if not form_element_entries:
        form_element_entries = form_entry.formelemententry_set.all()
    for form_element_entry in form_element_entries:
        # Get the plugin.
        form_element_plugin = form_element_entry.get_plugin(request=request)
        updated_form = form_element_plugin._submit_plugin_form_data(
            form_entry=form_entry,
            request=request,
            form=form,
            form_element_entries=form_element_entries,
            **kwargs
        )
        if updated_form:
            form = updated_form

    return form


# def submit_custom_instances_plugin_form_data(integrate_with,
#                                              form_entry,
#                                              request,
#                                              form_element_entries=None,
#                                              **kwargs):
#     """
#     Find all the plugins and their custom field instances. Then one by one
#     run the ``submit_plugin_form_data`` method on each of them.
#
#     # TODO
#     Submit plugin form data for all plugins.
#
#     :param str integrate_with:
#     :param fobi.models.FormEntry form_entry: Instance of
#         ``fobi.models.FormEntry``.
#     :param django.http.HttpRequest request:
#     :param iterable form_element_entries:
#     """
#     if not form_element_entries:
#         form_element_entries = form_entry.formelemententry_set.all()
#     for form_element_entry in form_element_entries:
#         # Get the plugin.
#         form_element_plugin = form_element_entry.get_plugin(request=request)
#         custom_plugin_cls = custom_field_instance_plugin_registry.get(
#             integrate_with, form_element_plugin.uid
#         )
#         if custom_plugin_cls:
#             custom_plugin = custom_plugin_cls()
#
#         updated_form = form_element_plugin._submit_plugin_form_data(
#             form_entry=form_entry,
#             request=request,
#             form=form,
#             form_element_entries=form_element_entries,
#             **kwargs
#         )
#         if updated_form:
#             form = updated_form
#
#     return form


def get_ignorable_form_fields(form_element_entries):
    """Get ignorable form fields by getting those without values.

    :param iterable form_element_entries: Iterable of
        ``fobi.models.FormElementEntry`` objects.
    :return iterable: Iterable of ignorable form element entries - field
        names.
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
            except AttributeError:
                pass

    return ignorable_form_fields

# *****************************************************************************
# **************************** Form handler specific **************************
# *****************************************************************************


def get_cleaned_data(form, keys_to_remove=[], values_to_remove=[]):
    """Get cleaned data.

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
        keys=list(set(cleaned_data.keys()) - set(keys_to_remove)),
        values=values_to_remove
    )

    return cleaned_data


def get_field_name_to_label_map(form, keys_to_remove=[], values_to_remove=[]):
    """Get field name to label map.

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
    """Gets processed form data.

    Simply fires both ``fobi.base.get_cleaned_data`` and
    ``fobi.base.get_field_name_to_label_map`` functions and returns the
    result.

    :param django.forms.Form form:
    :param iterable form_element_entries: Iterable of form element entries.
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


def get_processed_form_wizard_data(form_wizard, form_list,
                                   form_element_entries):
    """Get processed form wizard data."""
    field_name_to_label_map = {}
    cleaned_data = {}
    for form in form_list:
        _field_name_to_label_map, _cleaned_data = get_processed_form_data(
            form,
            form_element_entries
        )
        field_name_to_label_map.update(_field_name_to_label_map)
        cleaned_data.update(_cleaned_data)

    return (
        field_name_to_label_map,
        cleaned_data
    )


def get_registered_form_handler_plugins(as_instances=False):
    """Get registered form handler plugins.

    Gets a list of registered plugins in a form of tuple (plugin name, plugin
    description). If not yet auto-discovered, auto-discovers them.

    :return list:
    """
    return get_registered_plugins(form_handler_plugin_registry,
                                  as_instances=as_instances)


def get_registered_form_handler_plugin_uids(flattern=True):
    """Get registered form handler plugin uids.

    Gets a list of UIDs of registered form handler plugins. If not yet
    auto-discovered, auto-discovers them.

    :return list:
    """
    return get_registered_plugin_uids(
        form_handler_plugin_registry, flattern=flattern
    )


def validate_form_handler_plugin_uid(plugin_uid):
    """Validate the plugin uid.

    :param string plugin_uid:
    :return bool:
    """
    return validate_plugin_uid(form_handler_plugin_registry, plugin_uid)


def get_ordered_form_handler_plugins():
    """Get ordered form handler plugins.

    Gets form handler plugins in the execution order as a sortable
    dictionary, which can be later on used to add real plugins to
    be executed.

    :return fobi.data_structures.SortableDict:
    """
    form_handler_plugins = SortableDict()

    # Priority goes to the ones specified as first in the settings
    for uid in FORM_HANDLER_PLUGINS_EXECUTION_ORDER:
        form_handler_plugins[uid] = []

    # Adding all the rest
    for uid in form_handler_plugin_registry._registry.keys():
        if uid not in form_handler_plugins:
            form_handler_plugins[uid] = []

    return form_handler_plugins


# For backwards compatibility, if someone had ever used this.
get_ordered_form_handlers = get_ordered_form_handler_plugins


def run_form_handlers(form_entry, request, form, form_element_entries=None):
    """Run form handlers.

    :param fobi.models.FormEntry form_entry:
    :param django.http.HttpRequest request:
    :param django.forms.Form form:
    :param iterable form_element_entries:
    :return tuple: List of success responses, list of error responses
    """
    # Errors list
    errors = []

    # Responses of successfully processed handlers
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
        # logger.debug("UID: {0}".format(uid))
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
# ************************ Form wizard handler specific ***********************
# *****************************************************************************


def get_registered_form_wizard_handler_plugins(as_instances=False):
    """Get registered form handler wizard plugins.

    Gets a list of registered plugins in a form of tuple (plugin name, plugin
    description). If not yet auto-discovered, auto-discovers them.

    :return list:
    """
    return get_registered_plugins(form_wizard_handler_plugin_registry,
                                  as_instances=as_instances)


def get_registered_form_wizard_handler_plugin_uids(flattern=True):
    """Get registered form handler plugin uids.

    Gets a list of UIDs of registered form wizard handler plugins. If not yet
    auto-discovered, auto-discovers them.

    :return list:
    """
    return get_registered_plugin_uids(
        form_wizard_handler_plugin_registry, flattern=flattern
    )


def validate_form_wizard_handler_plugin_uid(plugin_uid):
    """Validate the plugin uid.

    :param string plugin_uid:
    :return bool:
    """
    return validate_plugin_uid(form_wizard_handler_plugin_registry, plugin_uid)


def get_ordered_form_wizard_handler_plugins():
    """Get ordered form wizard_handler plugins.

    Gets form wizard handler plugins in the execution order as a sortable
    dictionary, which can be later on used to add real plugins to
    be executed.

    :return fobi.data_structures.SortableDict:
    """
    form_wizard_handler_plugins = SortableDict()

    # Priority goes to the ones specified as first in the settings
    for uid in FORM_WIZARD_HANDLER_PLUGINS_EXECUTION_ORDER:
        form_wizard_handler_plugins[uid] = []

    # Adding all the rest
    for uid in form_wizard_handler_plugin_registry._registry.keys():
        if uid not in form_wizard_handler_plugins:
            form_wizard_handler_plugins[uid] = []

    return form_wizard_handler_plugins


# For backwards compatibility, if someone had ever used this.
get_ordered_form_wizard_handlers = get_ordered_form_wizard_handler_plugins


def run_form_wizard_handlers(form_wizard_entry, request, form_list,
                             form_wizard, form_element_entries=None):
    """Run form wizard handlers.

    :param fobi.models.FormWizardEntry form_wizard_entry:
    :param django.http.HttpRequest request:
    :param list form_list: List of :class:`django.forms.Form` objects.
    :param fobi.wizard.views.dynamic.DynamicWizardView form_wizard: The
        form wizard view object.
    :param iterable form_element_entries: Iterable
        of :class:`fobi.base.FormElementEntry` objects.
    :return tuple: List of success responses, list of error responses
    """
    # Errors list
    errors = []

    # Responses of successfully processed handlers
    responses = []

    # Getting form handler plugins in their execution order.
    ordered_form_wizard_handlers = get_ordered_form_wizard_handler_plugins()

    # Getting the form handlers to be executed.
    form_wizard_handlers = form_wizard_entry.formwizardhandlerentry_set \
                                            .order_by('plugin_uid')[:]

    # Assembling a new dictionary of the form handlers to iterate later.
    for form_wizard_handler in form_wizard_handlers:
        ordered_form_wizard_handlers[form_wizard_handler.plugin_uid].append(
            form_wizard_handler
        )

    # Iterating through the form handlers in the order
    # specified in the settings.
    for uid, form_wizard_handlers in ordered_form_wizard_handlers.items():
        # logger.debug("UID: {0}".format(uid))
        for form_wizard_handler in form_wizard_handlers:
            # Get the form handler plugin
            form_wizard_handler_plugin = form_wizard_handler.get_plugin(
                request=request
            )

            # Run the form handler
            success, response = form_wizard_handler_plugin._run(
                form_wizard_entry,
                request,
                form_list,
                form_wizard,
                form_element_entries
            )

            if success:
                responses.append((form_wizard_handler_plugin, response))
            else:
                errors.append((form_wizard_handler_plugin, response))

    return (responses, errors)

# *****************************************************************************
# ******************************* Theme specific ******************************
# *****************************************************************************


def get_registered_themes():
    """Get registered themes.

    Gets a list of registered themes in form of tuple (plugin name, plugin
    description). If not yet auto-discovered, auto-discovers them.

    :return list:
    """
    return get_registered_plugins(theme_registry)


def get_registered_theme_uids(flattern=True):
    """Get registered theme uids.

    Gets a list of registered themes in a form of tuple (plugin name, plugin
    description). If not yet auto-discovered, auto-discovers them.

    :return list:
    """
    return get_registered_plugin_uids(theme_registry, flattern=flattern)


def validate_theme_uid(plugin_uid):
    """Validate the theme uid.

    :param string plugin_uid:
    :return bool:
    """
    return validate_plugin_uid(theme_registry, plugin_uid)


def get_theme(request=None, theme_uid=None, as_instance=False):
    """Get theme.

    Gets the theme by ``theme_uid`` given. If left empty, takes the default
    one chosen in ``settings`` module.

    Raises a ``fobi.exceptions.ThemeDoesNotExist`` when no default layout
    could be found.

    :param django.http.HttpRequest request:
    :param int theme_uid:
    :param bool as_instance:
    :return fobi.base.BaseTheme: Subclcass of `fobi.base.BaseTheme`.
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


def get_default_theme():
    """Get default theme."""
    return get_theme(as_instance=True)


def get_theme_by_uid(theme_uid):
    """Get theme by uid."""
    return get_theme(theme_uid=theme_uid, as_instance=True)


# *****************************************************************************
# **************************** Form callbacks specific ************************
# *****************************************************************************


def get_registered_form_callbacks(stage=None):
    """Get registered form callbacks for the stage given."""
    return form_callback_registry.get_callbacks(stage=stage)


def fire_form_callbacks(form_entry, request, form, stage=None):
    """Fire form callbacks.

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
    """Get the plugin widget for the ``plugin_uid`` given.

    Looks up in the ``registry`` provided.

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
    """Get the form element plugin widget for the ``plugin_uid`` given.

    :param str plugin_uid: UID of the plugin to get the widget for.
    :param django.http.HttpRequest request:
    :param bool as_instance:
    :param fobi.base.BaseTheme theme: Subclass of.
    :return BasePluginWidget: Subclass of.
    """
    return get_plugin_widget(
        registry=form_element_plugin_widget_registry,
        plugin_uid=plugin_uid,
        request=request,
        as_instance=as_instance,
        theme=theme
    )


def get_form_handler_plugin_widget(plugin_uid, request=None, as_instance=False,
                                   theme=None):
    """Get the form handler plugin widget for the ``plugin_uid`` given.

    :param str plugin_uid: UID of the plugin to get the widget for.
    :param django.http.HttpRequest request:
    :param bool as_instance:
    :param fobi.base.BaseTheme theme: Subclass of.
    :return BasePluginWidget: Subclass of.
    """
    return get_plugin_widget(
        registry=form_handler_plugin_widget_registry,
        plugin_uid=plugin_uid,
        request=request,
        as_instance=as_instance,
        theme=theme
    )


def get_form_wizard_handler_plugin_widget(plugin_uid, request=None,
                                          as_instance=False, theme=None):
    """Get the form wizard handler plugin widget for the ``plugin_uid`` given.

    :param str plugin_uid: UID of the plugin to get the widget for.
    :param django.http.HttpRequest request:
    :param bool as_instance:
    :param fobi.base.BaseTheme theme: Subclass of.
    :return BasePluginWidget: Subclass of.
    """
    return get_plugin_widget(
        registry=form_wizard_handler_plugin_widget_registry,
        plugin_uid=plugin_uid,
        request=request,
        as_instance=as_instance,
        theme=theme
    )


# *****************************************************************************
# ****************** Integration form element plugin specific *****************
# *****************************************************************************


def get_registered_integration_form_element_plugins():
    """Get registered custom field instance plugins.

    Gets a list of registered plugins in a form if tuple (plugin name, plugin
    description). If not yet auto-discovered, auto-discovers them.

    :return list:
    """
    return get_registered_plugins(integration_form_element_plugin_registry)


def get_registered_integration_form_element_plugins_grouped():
    """Get registered custom field instance plugins grouped.

    Gets a list of registered plugins in a form if tuple (plugin name, plugin
    description). If not yet auto-discovered, auto-discovers them.

    :return dict:
    """
    return get_registered_plugins_grouped(
        integration_form_element_plugin_registry
    )


def get_registered_integration_form_element_plugin_uids(flattern=True):
    """Get registered custom field instance plugin uids.

    Gets a list of registered plugins in a form if tuple (plugin name, plugin
    description). If not yet auto-discovered, auto-discovers them.

    :return list:
    """
    return get_registered_plugin_uids(
        integration_form_element_plugin_registry, flattern=flattern
    )


def validate_integration_form_element_plugin_uid(plugin_uid):
    """Validate the custom field instance plugin uid.

    :param string plugin_uid:
    :return bool:
    """
    return validate_plugin_uid(
        integration_form_element_plugin_registry,
        plugin_uid
    )


# *****************************************************************************
# ****************** Integration form handler plugin specific *****************
# *****************************************************************************


def get_registered_integration_form_handler_plugins():
    """Get registered integration form handler plugins.

    Gets a list of registered plugins in a form if tuple (plugin name, plugin
    description). If not yet auto-discovered, auto-discovers them.

    :return list:
    """
    return get_registered_plugins(integration_form_handler_plugin_registry)


def get_registered_integration_form_handler_plugins_grouped():
    """Get registered integration form handler plugins grouped.

    Gets a list of registered plugins in a form if tuple (plugin name, plugin
    description). If not yet auto-discovered, auto-discovers them.

    :return dict:
    """
    return get_registered_plugins_grouped(
        integration_form_handler_plugin_registry
    )


def get_registered_integration_form_handler_plugin_uids(flattern=True):
    """Get registered integration form handler plugin uids.

    Gets a list of registered plugins in a form if tuple (plugin name, plugin
    description). If not yet auto-discovered, auto-discovers them.

    :return list:
    """
    return get_registered_plugin_uids(
        integration_form_handler_plugin_registry,
        flattern=flattern
    )


def validate_integration_form_handler_plugin_uid(plugin_uid):
    """Validate the integration form handler plugin uid.

    :param string plugin_uid:
    :return bool:
    """
    return validate_plugin_uid(
        integration_form_handler_plugin_registry,
        plugin_uid
    )

# *****************************************************************************
# ******************************** Media specific *****************************
# *****************************************************************************


def collect_plugin_media(form_element_entries, request=None):
    """Collect the plugin media for form element entries given.

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
                "No widget for form element entry %s",
                form_element_entry.__dict__
            )
    return {'js': media_js, 'css': media_css}
