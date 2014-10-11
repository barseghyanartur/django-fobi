__title__ = 'fobi.tests.test_core'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('FobiCoreTest',)

import unittest

from django.test import TestCase

from fobi.base import (
    get_registered_form_element_plugins, get_registered_form_handler_plugins,
    get_registered_themes, get_registered_form_callbacks
)

from fobi.tests.base import print_info
from fobi.tests.helpers import setup_fobi

class FobiCoreTest(TestCase):
    """
    Tests of django-fobi core functionality.
    """
    def setUp(self):
        setup_fobi(fobi_sync_plugins=True)

    @print_info
    def test_01_get_registered_form_element_plugins(self):
        """
        Test registered form element plugins
        (`get_registered_form_element_plugins`).
        """
        res = get_registered_form_element_plugins()
        self.assertTrue(len(res) > 0)
        return res

    @print_info
    def test_02_get_registered_form_handler_plugins(self):
        """
        Test registered form handlers (`get_registered_form_handler_plugins`).
        """
        res = get_registered_form_handler_plugins()
        self.assertTrue(len(res) > 0)
        return res

    @print_info
    def test_03_get_registered_form_callbacks(self):
        """
        Test registered form callbacks (`get_registered_form_callbacks`).
        """
        res = get_registered_form_callbacks()
        self.assertTrue(len(res) > 0)
        return res

    @print_info
    def test_04_get_registered_themes(self):
        """
        Test registered themes (`get_registered_themes`).
        """
        res = get_registered_themes()
        self.assertTrue(len(res) > 0)
        return res


if __name__ == '__main__':
    unittest.main()
