from django.core.management.base import BaseCommand

from fobi.tests.helpers import (
    get_or_create_admin_user, create_form_with_entries
)

class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Creates test data to fill the dashboard with.
        """
        try:
            user = get_or_create_admin_user()
            create_form_with_entries(user, create_entries_if_form_exist=False)
        except Exception as e:
            pass
