from django.core.management.base import BaseCommand

from fobi.tests.helpers import (
    get_or_create_admin_user,
    create_form_with_entries
)

__all__ = ('Command',)


class Command(BaseCommand):
    """Creates test data to fill the dashboard with."""

    def handle(self, *args, **options):
        """Handle."""
        try:
            user = get_or_create_admin_user()
            create_form_with_entries(user, create_entries_if_form_exist=False)
        except Exception as err:
            pass
