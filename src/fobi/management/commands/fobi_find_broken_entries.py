from six import print_

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
        form_element_entries = FormElementEntry._default_manager.all().only('id', 'plugin_uid') \
                                               .values_list('id', 'plugin_uid')
        form_handler_entries = FormHandlerEntry._default_manager.all().only('id', 'plugin_uid') \
                                               .values_list('id', 'plugin_uid')

        broken_form_element_entries = []
        broken_form_handler_entries = []

        registered_form_element_plugin_uids = get_registered_form_element_plugin_uids()
        registered_form_handler_plugin_uids = get_registered_form_handler_plugin_uids()

        for entry_id, plugin_uid in form_element_entries:
            if not plugin_uid in registered_form_element_plugin_uids:
                broken_form_element_entries.append((entry_id, plugin_uid))

        if broken_form_element_entries:
            print_("Broken form element entries found!", broken_form_element_entries)

        for entry_id, plugin_uid in form_handler_entries:
            if not plugin_uid in registered_form_handler_plugin_uids:
                broken_form_handler_entries.append((entry_id, plugin_uid))

        if broken_form_handler_entries:
            print_("Broken form handler entries found!", broken_form_handler_entries)
