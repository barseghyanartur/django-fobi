from admin_tools.dashboard.models import DashboardPreferences
from django.core.management import BaseCommand

__all__ = ("Command",)


class Command(BaseCommand):
    """Clears dashboard preferences."""

    help = """Clears dashboard preferences."""

    def handle(self, *args, **options):
        """Handle."""
        DashboardPreferences._default_manager.all().delete()
