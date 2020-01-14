import gc
import logging

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.wait import WebDriverWait

from django.core.management import call_command
from django.urls import reverse
from django.conf import settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from . import constants
from .helpers import (
    setup_app,
    get_or_create_admin_user,
    phantom_js_clean_up,
)

__title__ = 'fobi.tests.test_browser_build_dynamic_forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'BaseFobiBrowserBuldDynamicFormsTest',
)

logger = logging.getLogger(__name__)

TIMEOUT = 4
LONG_TIMEOUT = 8
WAIT = False
WAIT_FOR = 0


class BaseFobiBrowserBuldDynamicFormsTest(StaticLiveServerTestCase):
    """Browser tests django-fobi bulding forms functionality.

    Backed up by selenium. This test is based on the bootstrap3 theme.
    """

    reset_sequences = True
    cleans_up_after_itself = True

    try:
        LIVE_SERVER_URL = settings.LIVE_SERVER_URL
    except Exception as e:
        LIVE_SERVER_URL = None

    def tearDown(self):
        """Tear down."""
        super(BaseFobiBrowserBuldDynamicFormsTest, self).tearDown()
        call_command('flush',
                     verbosity=0,
                     interactive=False,
                     reset_sequences=True,
                     allow_cascade=True,
                     inhibit_post_migrate=False)
        # gc.collect()

    @classmethod
    def setUpClass(cls):
        """Set up class."""
        chrome_driver_path = getattr(
            settings,
            'CHROME_DRIVER_EXECUTABLE_PATH',
            None
        )
        chrome_driver_options = getattr(
            settings,
            'CHROME_DRIVER_OPTIONS',
            None
        )
        firefox_bin_path = getattr(settings, 'FIREFOX_BIN_PATH', None)
        phantom_js_executable_path = getattr(
            settings, 'PHANTOM_JS_EXECUTABLE_PATH', None
        )
        if chrome_driver_path is not None:
            cls.driver = webdriver.Chrome(
                executable_path=chrome_driver_path,
                options=chrome_driver_options
            )
        elif phantom_js_executable_path is not None:
            if phantom_js_executable_path:
                cls.driver = webdriver.PhantomJS(
                    executable_path=phantom_js_executable_path
                )
            else:
                cls.driver = webdriver.PhantomJS()
        elif firefox_bin_path:
            binary = FirefoxBinary(firefox_bin_path)
            cls.driver = webdriver.Firefox(firefox_binary=binary)
        else:
            cls.driver = webdriver.Firefox()

        setup_app(fobi_sync_plugins=True)
        # user = get_or_create_admin_user()
        # create_form_with_entries(user)

        super(BaseFobiBrowserBuldDynamicFormsTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        """Tear down class."""
        try:
            cls.driver.quit()
            phantom_js_clean_up()
        except Exception as err:
            print(err)

        super(BaseFobiBrowserBuldDynamicFormsTest, cls).tearDownClass()
        call_command('flush',
                     verbosity=0,
                     interactive=False,
                     reset_sequences=True,
                     allow_cascade=True,
                     inhibit_post_migrate=False)
        # gc.collect()

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++ Internals +++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++ General +++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def _maximize_window(self):
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1024 * 2, 768 * 2)
        self.driver.maximize_window()

    def _get_live_server_url(self):
        """Get live server URL."""
        return self.LIVE_SERVER_URL \
            if self.LIVE_SERVER_URL \
            else self.live_server_url

    def _authenticate(self):
        """Authenticate."""
        # Make sure the user exists
        user = get_or_create_admin_user()

        self.driver.get(
            '{0}{1}'.format(
                self._get_live_server_url(),
                reverse('auth_login')
            )
        )
        self._maximize_window()
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys(constants.FOBI_TEST_USER_USERNAME)
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys(constants.FOBI_TEST_USER_PASSWORD)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()

        # Wait until the list view opens
        WebDriverWait(self.driver, timeout=TIMEOUT).until(
            # lambda driver: driver.find_element_by_id('id_main')
            lambda driver: driver.find_element_by_xpath(
                '//body[contains(@class, "theme")]'
            )
        )

    def _sleep(self, wait=WAIT_FOR):
        """Sleep."""
        if WAIT and wait:
            self.driver.implicitly_wait(wait)

    def _click(self, element):
        """Click on any element."""
        self.driver.execute_script("arguments[0].click();", element)

    def _aggressive_click(self, element):
        """Aggressive click."""
        link = element.get_attribute('href')
        self.driver.get(link)

    def _scroll_to_element(self, form_element, simple=False):
        """Scroll to element."""
        coordinates = form_element.location_once_scrolled_into_view
        if simple:
            return

        x = coordinates.get('x', 0)
        y = coordinates.get('y', 0)
        self.driver.execute_script(
            "window.scrollTo({0}, {1});".format(x, y)
        )
        self.driver.execute_script(
            "window.scrollBy({0}, {1});".format(0, -100)
        )

    def _move_to_element(self, form_element, simple=False):
        """Move to element."""
        ActionChains(self.driver).move_to_element(form_element).perform()

    def _scroll_to(self, x, y):
        """Scroll to."""
        self.driver.execute_script(
            "window.scrollTo({0}, {1});".format(x, y)
        )

    def _scroll_by(self, x, y):
        """Scroll by."""
        self.driver.execute_script(
            "window.scrollBy({0}, {1});".format(x, y)
        )

    def _scroll_page_top(self):
        """Scroll to the page top."""
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.HOME)

    def _scroll_page_bottom(self):
        """Scroll to the page bottom."""
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
