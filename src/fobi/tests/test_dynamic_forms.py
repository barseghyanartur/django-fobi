import unittest

from django.test import TestCase

from fobi.dynamic import assemble_form_class

from .core import print_info
from .data import TEST_DYNAMIC_FORMS_DEFINITION_DATA
from .helpers import (
    create_form_with_entries,
    get_or_create_admin_user,
    setup_app,
)

__title__ = 'fobi.tests.test_dynamic_forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('FobiDynamicFormsTest',)


class FobiDynamicFormsTest(TestCase):
    """Tests of django-fob dynamic forms functionality."""

    def setUp(self):
        """Set up."""
        setup_app(fobi_sync_plugins=True)
        self.user = get_or_create_admin_user()
        self.form_entry = create_form_with_entries(
            self.user,
            data=TEST_DYNAMIC_FORMS_DEFINITION_DATA
        )

    @print_info
    def test_01_assemble_form_class_and_render_form(self):
        """Test form class assembling and rendering."""
        flow = []

        # Getting entry with created plugins
        # form_entry = create_form_with_entries(
        #     data=TEST_DYNAMIC_FORMS_DEFINITION_DATA
        # )
        flow.append(self.form_entry)

        form_class = assemble_form_class(self.form_entry)
        flow.append(form_class)

        form = form_class()
        flow.append(form)

        rendered_form = form.as_p()
        flow.append(rendered_form)

        return flow


if __name__ == '__main__':
    unittest.main()
