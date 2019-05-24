import logging
import unittest

from selenium.webdriver.support.wait import WebDriverWait

import factories

from .base import BaseFobiBrowserBuldDynamicFormsTest

__title__ = 'fobi.tests.test_browser_build_dynamic_forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'FeinCMSIntegrationTest',
)

logger = logging.getLogger(__name__)

TIMEOUT = 4
LONG_TIMEOUT = 8
WAIT = False
WAIT_FOR = 0


class FeinCMSIntegrationTest(BaseFobiBrowserBuldDynamicFormsTest):
    """FeinCMS integration tests."""

    def setUp(self):
        super(FeinCMSIntegrationTest, self).setUp()

        self.fobi_form_page = factories.FobiFormPageFactory()
        self.fobi_form_page_url = '{0}{1}'.format(
            self._get_live_server_url(),
            self.fobi_form_page.get_absolute_url()
        )

    def test_fobi_form_widget_public_form(self):
        """Test fobi form widget."""
        self.driver.get(self.fobi_form_page_url)
        # Wait until the edit widget form opens
        WebDriverWait(self.driver, timeout=TIMEOUT).until(
            lambda driver: driver.find_element_by_xpath(
                '//body[contains(@class, "theme-bootstrap3")]'
            )
        )
        # TODO:

    # def test_fobi_form_widget_private_form(self):
    #     """Test fobi form widget."""
    #     self.driver.get(self.fobi_form_page_url)
    #     # Wait until the edit widget form opens
    #     WebDriverWait(self.driver, timeout=TIMEOUT).until(
    #         lambda driver: driver.find_element_by_xpath(
    #             '//body[contains(@class, "theme-bootstrap3")]'
    #         )
    #     )
    #     # TODO:


if __name__ == '__main__':
    unittest.main()
