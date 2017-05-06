from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .data import (
    TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF,
    TEST_DYNAMIC_FORMS_OPTIONS_RESPONSE,
    TEST_DYNAMIC_FORMS_PUT_DATA,
)
from .helpers import create_form_with_entries

__title__ = 'fobi.tests.test_drf_integration'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'FobiDjangoRestFrameworkIntegrationTests',
)


class FobiDjangoRestFrameworkIntegrationTests(APITestCase):
    """DRF integration tests."""

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        form_entry = create_form_with_entries(
            user=None,
            data=TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF
        )
        url = reverse(
            'fobi_form_entry-detail',
            args=[form_entry.slug],
            # request=self.context['request']
        )

        # Testing OPTIONS action call
        options_response = self.client.options(url)
        self.assertEqual(options_response.status_code, status.HTTP_200_OK)
        self.assertEqual(options_response.data['actions']['PUT'],
                         TEST_DYNAMIC_FORMS_OPTIONS_RESPONSE)

        # Testing PUT action call
        put_response = self.client.put(
            url,
            TEST_DYNAMIC_FORMS_PUT_DATA,
            format='json'
        )
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(put_response.data),
                         dict(TEST_DYNAMIC_FORMS_PUT_DATA))
