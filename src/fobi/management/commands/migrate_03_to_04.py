from __future__ import print_function

from django.core.management.base import BaseCommand

from fobi.models import FormElementEntry

class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Database related changes necessary to upgrade fobi==0.3.* to
        fobi==0.4. The full list of changes is listed below:

        - Change the "birthday" occurances to "date_drop_down".
        """
        n_updated = FormElementEntry._default_manager \
                                    .filter(plugin_uid='birthday') \
                                    .only('id', 'plugin_uid') \
                                    .update(plugin_uid='date_drop_down')

        print("{0} form element entries updated!".format(n_updated))
