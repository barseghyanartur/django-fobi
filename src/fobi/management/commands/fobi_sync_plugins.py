from django.core.management.base import BaseCommand

from nine import versions

from fobi.utils import sync_plugins


class Command(BaseCommand):
    """Adds the missing plugins to database.

    This command shall be ran every time a developer adds a new plugin.
    The following plugins are affected:

        - ``fobi.models.FormElementPlugin``
        - ``fobi.models.FormHandlerPlugin``
    """

    if versions.DJANGO_GTE_2_0:
        def add_arguments(self, parser):
            parser.add_argument(
                '--noinput',
                '--no-input',
                action='store_false',
                dest='interactive',
                help='Tells Django to NOT prompt the user for input of any '
                     'kind.',
            )

    def handle(self, *args, **options):
        """Handle."""
        sync_plugins()
