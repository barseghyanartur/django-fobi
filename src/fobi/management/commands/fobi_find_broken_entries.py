from __future__ import print_function

from django.core.management.base import BaseCommand

from fobi.models import FormElementEntry, FormHandlerEntry
from fobi.base import get_registered_form_handler_plugin_uids, get_registered_form_element_plugin_uids

class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Find the broken plugin records in the database:
        
        - ``fobi.models.FormElementEntry``
        - ``fobi.models.FormHandlerEntry``
        """
        form_element_entries = FormElementEntry._default_manager.all() \
                                               .only('id', 'plugin_uid', 'form_entry') \
                                               .values_list('id', 'plugin_uid', 'form_entry')
        form_handler_entries = FormHandlerEntry._default_manager.all() \
                                               .only('id', 'plugin_uid', 'form_entry') \
                                               .values_list('id', 'plugin_uid', 'form_entry')

        broken_form_element_entries = []
        broken_form_handler_entries = []

        registered_form_element_plugin_uids = \
            get_registered_form_element_plugin_uids()

        registered_form_handler_plugin_uids = \
            get_registered_form_handler_plugin_uids()

        for entry_id, plugin_uid, form_entry_id in form_element_entries:
            if not plugin_uid in registered_form_element_plugin_uids:
                broken_form_element_entries.append((form_entry_id, entry_id, plugin_uid))

        if broken_form_element_entries:
            print("Broken form element entries found (form ID, entry ID, plugin UID)!", \
                  broken_form_element_entries)

        for entry_id, plugin_uid, form_entry_id in form_handler_entries:
            if not plugin_uid in registered_form_handler_plugin_uids:
                broken_form_handler_entries.append((form_entry_id, entry_id, plugin_uid))

        if broken_form_handler_entries:
            print("Broken form handler entries found (form ID, entry ID, plugin UID)!", \
                  broken_form_handler_entries)
