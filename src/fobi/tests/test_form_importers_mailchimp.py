import unittest

# from django.contrib.auth import get_user_model
from django.test import TestCase

from fobi.contrib.plugins.form_importers \
         .mailchimp_importer.fobi_form_importers import MailChimpImporter
from fobi.models import FormEntry, FormElementEntry

from .core import print_info
from .data import TEST_MAILCHIMP_IMPORTER_FORM_DATA
from .helpers import setup_app, get_or_create_admin_user

__title__ = 'fobi.tests.test_form_importers_mailchimp'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('FormImportersMailchimpTest',)


class FormImportersMailchimpTest(TestCase):
    """Tests of form importers mailchimp functionality."""

    def setUp(self):
        """Set up."""
        setup_app(fobi_sync_plugins=True)

    @print_info
    def test_01_test_mailchimp_importer(self):
        """Test mailchimp importer."""
        user = get_or_create_admin_user()

        form_properties = {
            'name': 'Test mailchimp form',
            'user': user
        }

        importer = MailChimpImporter(
            form_entry_cls=FormEntry,
            form_element_entry_cls=FormElementEntry
        )

        importer.import_data(
            form_properties=form_properties,
            form_data=TEST_MAILCHIMP_IMPORTER_FORM_DATA
        )

        form_entry = FormEntry.objects.get(**form_properties)

        self.assertIsNotNone(form_entry.pk)


if __name__ == '__main__':
    unittest.main()
