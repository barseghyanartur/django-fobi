from django.core.management.base import BaseCommand

from fobi.utils import sync_plugins

class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Adds the missing plugins to database. This command shall be ran every
        time a developer adds a new plugin. The following plugins are affected:

        - ``fobi.models.FormElementPlugin``
        - ``fobi.models.FormHandlerPlugin``
        """
        sync_plugins()
