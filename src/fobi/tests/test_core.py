import unittest

from django.test import TestCase, RequestFactory

from fobi.base import (
    get_registered_form_element_plugins, get_registered_form_handler_plugins,
    get_registered_themes, get_registered_form_callbacks
)
from fobi.models import FormEntry
from fobi.forms import FormEntryForm
from fobi.tests.constants import TEST_FORM_NAME, TEST_FORM_SLUG
from fobi.tests.base import print_info
from fobi.tests.helpers import setup_fobi, get_or_create_admin_user

__title__ = 'fobi.tests.test_core'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('FobiCoreTest',)


class FobiCoreTest(TestCase):
    """Tests of django-fobi core functionality."""

    def setUp(self):
        """Set up."""
        setup_fobi(fobi_sync_plugins=True)

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
            '/en/fobi/forms/edit/27/',
            data={
                'name': "John Doe",
                'is_public': False,
                'success_page_title': '',
                'success_page_message': '',
                'action': action_url,
            }
        )
        request.META['SERVER_NAME'] = 'localhost'
        form = FormEntryForm(request.POST, request=request,
                             instance=form_entry)

        saved = False
        try:

            if form.is_valid():
                form.save()
                saved = True
        except Exception as err:
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

    @print_info
    def test_05_action_url(self):
        """Test `action` field of the URL."""
        form_entry = self._create_form_entry()

        # Local URL, OK test
        saved = self._test_form_action_url(
            form_entry, '/en/fobi/forms/edit/27/'
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


if __name__ == '__main__':
    unittest.main()
