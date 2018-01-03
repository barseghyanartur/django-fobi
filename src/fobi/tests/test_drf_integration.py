from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .constants import FOBI_TEST_USER_USERNAME, FOBI_TEST_USER_PASSWORD
from .data import (
    TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF,
    TEST_DYNAMIC_FORMS_OPTIONS_RESPONSE,
    TEST_DYNAMIC_FORMS_PUT_DATA,
    TEST_DYNAMIC_FORMS_PUT_DATA_ALL,
)
from .helpers import create_form_with_entries

__title__ = 'fobi.tests.test_drf_integration'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'FobiDjangoRestFrameworkIntegrationTests',
)


class FobiDjangoRestFrameworkIntegrationTests(APITestCase):
    """DRF integration tests."""

    def setUp(self):
        """Set up."""
        super(FobiDjangoRestFrameworkIntegrationTests, self).setUp()
        self.client.logout()

    def tearDown(self):
        """Set up."""
        super(FobiDjangoRestFrameworkIntegrationTests, self).tearDown()
        self.client.logout()

    @classmethod
    def setUpTestData(cls):
        """Load initial data for the TestCase"""
        # Public form entry
        cls.form_entry = create_form_with_entries(
            user=None,
            data=TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF,
            is_public=True
        )
        cls.url = reverse(
            'fobi_form_entry-detail',
            args=[cls.form_entry.slug],
            # request=self.context['request']
        )

        # Private form entry
        cls.non_public_form_entry = create_form_with_entries(
            user=None,
            data=TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF,
            is_public=False,
            name='Non public test form',
            slug='non-public-test-form'
        )
        cls.non_public_url = reverse(
            'fobi_form_entry-detail',
            args=[cls.non_public_form_entry.slug],
            # request=self.context['request']
        )

    def test_01_options_action_public_form(self):
        """Test OPTIONS action call for public form."""
        # Testing OPTIONS action call
        options_response = self.client.options(self.url)
        self.assertEqual(options_response.status_code, status.HTTP_200_OK)
        self.assertIn('actions', options_response.data)
        self.assertIn('PUT', options_response.data['actions'])
        self.assertEqual(options_response.data['actions']['PUT'],
                         TEST_DYNAMIC_FORMS_OPTIONS_RESPONSE)

    def test_02_put_action_public_form(self):
        """Test PUT action call for public form."""
        # Testing PUT action call
        put_response = self.client.put(
            self.url,
            TEST_DYNAMIC_FORMS_PUT_DATA,
            format='json'
        )
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(put_response.data),
                         dict(TEST_DYNAMIC_FORMS_PUT_DATA))

    def test_03_fail_put_action_public_form(self):
        """Test PUT action call fail test for public form."""
        # Testing PUT action call
        put_response = self.client.put(
            self.url,
            TEST_DYNAMIC_FORMS_PUT_DATA_ALL,
            format='json'
        )
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(put_response.data),
                         dict(TEST_DYNAMIC_FORMS_PUT_DATA))

    def test_04_fail_options_action_non_public_form(self):
        """Test OPTIONS action call fail test for non-public form."""
        # Testing OPTIONS action call
        options_response = self.client.options(self.non_public_url)
        self.assertEqual(options_response.status_code,
                         status.HTTP_200_OK)
        self.assertNotIn('actions', options_response.data)

    def test_05_fail_put_action(self):
        """Test PUT action call fail test for non-public form."""
        # Testing PUT action call
        put_response = self.client.put(
            self.non_public_url,
            TEST_DYNAMIC_FORMS_PUT_DATA,
            format='json'
        )
        self.assertEqual(put_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_06_options_action_non_public_form_auth_user(self):
        """Test OPTIONS action call for authorised user for non-public form."""
        # Testing OPTIONS action call
        self.client.login(username=FOBI_TEST_USER_USERNAME,
                          password=FOBI_TEST_USER_PASSWORD)
        options_response = self.client.options(self.non_public_url)
        self.assertEqual(options_response.status_code, status.HTTP_200_OK)
        self.assertIn('actions', options_response.data)
        self.assertIn('PUT', options_response.data['actions'])
        self.assertEqual(options_response.data['actions']['PUT'],
                         TEST_DYNAMIC_FORMS_OPTIONS_RESPONSE)

    def test_07_put_action_non_public_form_auth_user(self):
        """Test PUT action call for authorised user for non-public form."""
        # Testing PUT action call
        self.client.login(username=FOBI_TEST_USER_USERNAME,
                          password=FOBI_TEST_USER_PASSWORD)
        put_response = self.client.put(
            self.non_public_url,
            TEST_DYNAMIC_FORMS_PUT_DATA,
            format='json'
        )
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(put_response.data),
                         dict(TEST_DYNAMIC_FORMS_PUT_DATA))

    def test_08_get_action_public_form(self):
        """Test OPTIONS action call for public form."""
        # Testing GET action call
        get_response = self.client.get(self.url)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertIn('url', get_response.data)
        self.assertIn('id', get_response.data)
        self.assertIn('slug', get_response.data)
        self.assertEqual(get_response.data['id'], self.form_entry.pk)
        self.assertEqual(get_response.data['slug'], self.form_entry.slug)

    def test_09_get_action_non_public_form_auth_user(self):
        """Test GET action call for authorised user for non-public form."""
        # Testing GET action call
        self.client.login(username=FOBI_TEST_USER_USERNAME,
                          password=FOBI_TEST_USER_PASSWORD)
        get_response = self.client.get(self.non_public_url)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertIn('url', get_response.data)
        self.assertIn('id', get_response.data)
        self.assertIn('slug', get_response.data)
        self.assertEqual(get_response.data['id'],
                         self.non_public_form_entry.pk)
        self.assertEqual(get_response.data['slug'],
                         self.non_public_form_entry.slug)

    def test_10_fail_get_action_non_public_form(self):
        """Test GET action call fail test for non-public form."""
        # Testing GET action call
        get_response = self.client.get(self.non_public_url)
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)
