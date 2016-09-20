from django.core.management.base import BaseCommand

from fobi.utils import sync_plugins


class Command(BaseCommand):
    """Adds the missing plugins to database.

    This command shall be ran every time a developer adds a new plugin.
    The following plugins are affected:

        - ``fobi.models.FormElementPlugin``
        - ``fobi.models.FormHandlerPlugin``
    """

    def handle(self, *args, **options):
        """Handle."""
        sync_plugins()
