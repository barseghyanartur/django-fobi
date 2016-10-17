import datetime

import simplejson as json

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from fobi.base import (
    # General
    get_processed_form_data,
    get_processed_form_wizard_data,

    # Form
    FormHandlerPlugin,
    form_handler_plugin_registry,
    get_form_handler_plugin_widget,

    # Form wizard
    FormWizardHandlerPlugin,
    form_wizard_handler_plugin_registry,
    get_form_wizard_handler_plugin_widget,
)
from fobi.helpers import get_form_element_entries_for_form_wizard_entry
from . import UID
from .models import SavedFormDataEntry, SavedFormWizardDataEntry

__title__ = 'fobi.contrib.plugins.form_handlers.db_store.fobi_form_handlers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'DBStoreHandlerPlugin',
    'DBStoreWizardHandlerPlugin',
)

# *****************************************************************************
# **************************** Form handler ***********************************
# *****************************************************************************


class DBStoreHandlerPlugin(FormHandlerPlugin):
    """DB store form handler plugin.

    Can be used only once per form.
    """

    uid = UID
    name = _("DB store")
    allow_multiple = False

    def run(self, form_entry, request, form, form_element_entries=None):
        """Run.

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        :param iterable form_element_entries: Iterable of
            ``fobi.models.FormElementEntry`` objects.
        """
        # Clean up the values, leave our content fields and empty values.
        field_name_to_label_map, cleaned_data = get_processed_form_data(
            form,
            form_element_entries
        )

        for key, value in cleaned_data.items():
            if isinstance(value, (datetime.datetime, datetime.date)):
                cleaned_data[key] = value.isoformat() \
                    if hasattr(value, 'isoformat') \
                    else value

        saved_form_data_entry = SavedFormDataEntry(
            form_entry=form_entry,
            user=request.user if request.user and request.user.pk else None,
            form_data_headers=json.dumps(field_name_to_label_map),
            saved_data=json.dumps(cleaned_data)
        )
        saved_form_data_entry.save()

    def custom_actions(self, form_entry, request=None):
        """Custom actions.

        Adding a link to view the saved form entries.

        :return iterable:
        """
        widget = get_form_handler_plugin_widget(
            self.uid, request=request, as_instance=True
        )

        if widget:
            view_entries_icon_class = widget.view_entries_icon_class
            export_entries_icon_class = widget.export_entries_icon_class
        else:
            view_entries_icon_class = 'glyphicon glyphicon-list'
            export_entries_icon_class = 'glyphicon glyphicon-export'

        return (
            (
                reverse('fobi.contrib.plugins.form_handlers.db_store.'
                        'view_saved_form_data_entries',
                        args=[form_entry.pk]),
                _("View entries"),
                view_entries_icon_class
            ),
            (
                reverse('fobi.contrib.plugins.form_handlers.db_store.'
                        'export_saved_form_data_entries',
                        args=[form_entry.pk]),
                _("Export entries"),
                export_entries_icon_class
            ),
        )


form_handler_plugin_registry.register(DBStoreHandlerPlugin)

# *****************************************************************************
# ************************ Form wizard handler ********************************
# *****************************************************************************


class DBStoreWizardHandlerPlugin(FormWizardHandlerPlugin):
    """DB store form wizard handler plugin.

    Can be used only once per form.
    """

    uid = UID
    name = _("DB store")
    allow_multiple = False

    def run(self, form_wizard_entry, request, form_list, form_wizard,
            form_element_entries=None):
        """Run.

        :param fobi.models.FormWizardEntry form_wizard_entry: Instance
            of :class:`fobi.models.FormWizardEntry`.
        :param django.http.HttpRequest request:
        :param list form_list: List of :class:`django.forms.Form` instances.
        :param fobi.wizard.views.dynamic.DynamicWizardView form_wizard:
            Instance of :class:`fobi.wizard.views.dynamic.DynamicWizardView`.
        :param iterable form_element_entries: Iterable of
            ``fobi.models.FormElementEntry`` objects.
        """
        if not form_element_entries:
            form_element_entries = \
                get_form_element_entries_for_form_wizard_entry(
                    form_wizard_entry
                )

        # Clean up the values, leave our content fields and empty values.
        field_name_to_label_map, cleaned_data = get_processed_form_wizard_data(
            form_wizard,
            form_list,
            form_element_entries
        )

        for key, value in cleaned_data.items():
            if isinstance(value, (datetime.datetime, datetime.date)):
                cleaned_data[key] = value.isoformat() \
                    if hasattr(value, 'isoformat') \
                    else value

        saved_form_wizard_data_entry = SavedFormWizardDataEntry(
            form_wizard_entry=form_wizard_entry,
            user=request.user if request.user and request.user.pk else None,
            form_data_headers=json.dumps(field_name_to_label_map),
            saved_data=json.dumps(cleaned_data)
        )
        saved_form_wizard_data_entry.save()

    def custom_actions(self, form_wizard_entry, request=None):
        """Custom actions.

        Adding a link to view the saved form entries.

        :return iterable:
        """
        widget = get_form_wizard_handler_plugin_widget(
            self.uid, request=request, as_instance=True
        )

        if widget:
            view_entries_icon_class = widget.view_entries_icon_class
            export_entries_icon_class = widget.export_entries_icon_class
        else:
            view_entries_icon_class = 'glyphicon glyphicon-list'
            export_entries_icon_class = 'glyphicon glyphicon-export'

        return (
            (
                reverse('fobi.contrib.plugins.form_handlers.db_store.'
                        'view_saved_form_wizard_data_entries',
                        args=[form_wizard_entry.pk]),
                _("View entries"),
                view_entries_icon_class
            ),
            (
                reverse('fobi.contrib.plugins.form_handlers.db_store.'
                        'export_saved_form_wizard_data_entries',
                        args=[form_wizard_entry.pk]),
                _("Export entries"),
                export_entries_icon_class
            ),
        )


form_wizard_handler_plugin_registry.register(DBStoreWizardHandlerPlugin)
