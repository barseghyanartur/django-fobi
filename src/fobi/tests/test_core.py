import datetime
import unittest

from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.utils import timezone

from fobi.base import (
    get_registered_form_element_plugins,
    get_registered_form_handler_plugins,
    get_registered_themes,
    get_registered_form_callbacks,
)
from fobi.models import FormEntry, FormWizardEntry
from fobi.forms import FormEntryForm

from .core import print_info
from .constants import TEST_FORM_NAME, TEST_FORM_SLUG
from .helpers import setup_app, get_or_create_admin_user

__title__ = 'fobi.tests.test_core'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('FobiCoreTest',)


class FobiCoreTest(TestCase):
    """Tests of django-fobi core functionality."""

    def setUp(self):
        """Set up."""
        setup_app(fobi_sync_plugins=True)

    @print_info
    def test_01_get_registered_form_element_plugins(self):
        """Test registered form element plugins.

        Calling the `get_registered_form_element_plugins`.
        """
        res = get_registered_form_element_plugins()
        self.assertTrue(len(res) > 0)
        return res

    @print_info
    def test_02_get_registered_form_handler_plugins(self):
        """Test registered form handlers.

        Calling `get_registered_form_handler_plugins`.
        """
        res = get_registered_form_handler_plugins()
        self.assertTrue(len(res) > 0)
        return res

    @print_info
    def test_03_get_registered_form_callbacks(self):
        """Test registered form callbacks.

        Calling `get_registered_form_callbacks`.
        """
        res = get_registered_form_callbacks()
        self.assertTrue(len(res) > 0)
        return res

    @print_info
    def test_04_get_registered_themes(self):
        """Test registered themes.

        Calling `get_registered_themes`.
        """
        res = get_registered_themes()
        self.assertTrue(len(res) > 0)
        return res

    def _test_form_action_url(self, form_entry, action_url):
        """Test form action URL."""
        request_factory = RequestFactory()
        request = request_factory.post(
            reverse('fobi.edit_form_entry', args=[form_entry.pk]),
            data={
                'name': "John Doe",
                'is_public': False,
                'success_page_title': '',
                'success_page_message': '',
                'action': action_url,
            }
        )
        form = FormEntryForm(
            request.POST,
            request=request,
            instance=form_entry
        )

        saved = False
        try:

            if form.is_valid():
                form.save()
                saved = True
        except Exception:
            pass

        return saved

    def _create_form_entry(self):
        """Create form entry."""
        user = get_or_create_admin_user()
        self.assertTrue(user is not None)

        form_entry = FormEntry(
            name=TEST_FORM_NAME,
            slug=TEST_FORM_SLUG,
            user=user
        )
        form_entry.save()
        return form_entry

    def _create_form_wizard_entry(self):
        """Create form wizard entry."""
        user = get_or_create_admin_user()
        self.assertTrue(user is not None)

        form_wizard_entry = FormWizardEntry(
            name=TEST_FORM_NAME,
            slug=TEST_FORM_SLUG,
            user=user
        )
        form_wizard_entry.save()
        return form_wizard_entry

    @print_info
    def test_05_action_url(self):
        """Test `action` field of the URL."""
        form_entry = self._create_form_entry()

        # Local URL, OK test
        saved = self._test_form_action_url(
            form_entry, reverse('fobi.edit_form_entry', args=[27])
        )
        self.assertTrue(saved)

        # Local URL, fail test
        saved = self._test_form_action_url(
            form_entry, '/en/idontexist/'
        )
        self.assertTrue(not saved)

        # External URL, OK test
        saved = self._test_form_action_url(
            form_entry, 'http://delusionalinsanity.com/portfolio/'
        )
        self.assertTrue(saved)

        # External URL, fail test
        saved = self._test_form_action_url(
            form_entry, 'http://delusionalinsanity.com2/portfolio/'
        )
        self.assertTrue(not saved)

        # External URL, fail test
        saved = self._test_form_action_url(
            form_entry, 'http://delusionalinsanity2.com/portfolio/'
        )
        self.assertTrue(not saved)

    @print_info
    def test_06_form_entry_get_absolute_url(self):
        """Test ``get_absolute_url`` of the form entry."""
        form_entry = self._create_form_entry()
        absolute_url = form_entry.get_absolute_url()
        self.assertTrue(
            absolute_url,
            '/en/fobi/view/{}/'.format(TEST_FORM_SLUG)
        )

    @print_info
    def test_07_form_wizard_entry_get_absolute_url(self):
        """Test ``get_absolute_url`` of the form wizard entry."""
        form_wizard_entry = self._create_form_wizard_entry()
        absolute_url = form_wizard_entry.get_absolute_url()
        self.assertTrue(
            absolute_url,
            '/en/fobi/wizard-view/{}/'.format(TEST_FORM_SLUG)
        )

    @print_info
    def test_08_form_entry_is_active(self):
        """Test ``is_active`` of the form entry."""
        form_entry = self._create_form_entry()
        self.assertTrue(form_entry.is_active)

        now = timezone.now()
        tomorrow = now + datetime.timedelta(days=1)
        yesterday = now - datetime.timedelta(days=1)

        form_entry.active_date_from = now
        form_entry.active_date_to = None
        self.assertTrue(form_entry.is_active)

        form_entry.active_date_from = yesterday
        form_entry.active_date_to = tomorrow
        self.assertTrue(form_entry.is_active)

        form_entry.active_date_from = tomorrow
        form_entry.active_date_to = yesterday
        self.assertFalse(form_entry.is_active)

        form_entry.active_date_from = None
        form_entry.active_date_to = now
        self.assertFalse(form_entry.is_active)


if __name__ == '__main__':
    unittest.main()
