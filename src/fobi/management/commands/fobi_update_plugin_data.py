from django.core.management.base import BaseCommand

from fobi.utils import update_plugin_data_for_entries
from fobi.models import FormElementEntry, FormHandlerEntry

class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Updates the plugin data for all entries of all users. Rules for update
        are specified in the plugin itself.

        This command shall be ran if significant changes have been made to the
        system for which the data shall be updated.
        """
        form_element_entries = FormElementEntry._default_manager.all()
        update_plugin_data_for_entries(entries=form_element_entries)

        form_handler_entries = FormHandlerEntry._default_manager.all()
        update_plugin_data_for_entries(entries=form_handler_entries)
