__title__ = 'fobi.tests.test_browser_build_dynamic_forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('FobiBrowserBuldDynamicFormsTest',)

import unittest
import logging

from time import sleep

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase
from django.conf import settings

from fobi.models import FormEntry

from fobi.tests.base import print_info, skip#, BaseBrowserTest
from fobi.tests.helpers import (
    setup_fobi, get_or_create_admin_user, db_clean_up
)
from fobi.tests import constants
from fobi.tests.data import (
    TEST_FORM_ELEMENT_PLUGIN_DATA, TEST_FORM_FIELD_DATA,
    TEST_FORM_HANDLER_PLUGIN_DATA
)

logger = logging.getLogger(__name__)

TIMEOUT = 4
WAIT = False
WAIT_FOR = 0

class FobiBrowserBuldDynamicFormsTest(LiveServerTestCase):
    """
    Browser tests django-fobi bulding forms functionality. Backed up
    by selenium.

    This test is based on the bootstrap3 theme.
    """
    """
    Base browser test.
    """
    try:
        LIVE_SERVER_URL = settings.LIVE_SERVER_URL
    except Exception as e:
        LIVE_SERVER_URL = None

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()

        setup_fobi(fobi_sync_plugins=True)
        #user = get_or_create_admin_user()
        #create_form_with_entries(user)

        super(FobiBrowserBuldDynamicFormsTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        try:
            cls.selenium.quit()
        except Exception as e:
            print(e)

        super(FobiBrowserBuldDynamicFormsTest, cls).tearDownClass()

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

    def __get_live_server_url(self):
        """
        Get live server URL.
        """
        return self.LIVE_SERVER_URL if self.LIVE_SERVER_URL \
                                    else self.live_server_url

    def __authenticate(self):
        """
        """
        # Make sure the user exists
        user = get_or_create_admin_user()

        self.selenium.get('{0}{1}'.format(self.__get_live_server_url(), settings.LOGIN_URL))
        self.selenium.maximize_window()
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(constants.FOBI_TEST_USER_USERNAME)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys(constants.FOBI_TEST_USER_PASSWORD)
        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()

        # Wait until the list view opens
        WebDriverWait(self.selenium, timeout=TIMEOUT).until(
            #lambda driver: driver.find_element_by_id('id_main')
            lambda driver: driver.find_element_by_xpath('//body[contains(@class, "theme")]')
            )

    def __sleep(self, wait=WAIT_FOR):
        if WAIT and wait:
            self.selenium.implicitly_wait(wait)

    def __go_to_dashboard(self, wait=WAIT_FOR):
        """
        Go to dashboard.
        """
        # Authenticate user.
        self.__authenticate()

        # Open the dashboard.
        url = reverse('fobi.dashboard')
        self.selenium.get('{0}{1}'.format(self.__get_live_server_url(), url))

        # Wait until the edit widget form opens
        WebDriverWait(self.selenium, timeout=TIMEOUT).until(
            lambda driver: driver.find_element_by_xpath('//body[contains(@class, "theme-bootstrap3")]')
            )

        self.__sleep(wait)

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ++++++++++++++++++++++ Form related +++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def __test_add_form(self, wait=WAIT_FOR):
        """
        Test add form.
        """
        # First open the dashboard
        self.__go_to_dashboard()

        # Follow the create form link.
        # Click the button to go to dashboard edit
        self.selenium.find_element_by_xpath('//a[contains(@class, "list-group-item")]').click()

        # Wait until the dashboard edit view opens
        WebDriverWait(self.selenium, timeout=TIMEOUT).until(
            #lambda driver: driver.find_element_by_id('id_main')
            lambda driver: driver.find_element_by_xpath('//body[contains(@class, "theme-bootstrap3")]')
            )

        form_data = {
            'name': constants.TEST_FORM_NAME,
            #'user': get_or_create_admin_user(),
            #'slug': constants.TEST_FORM_SLUG,
            'is_public': True,
            'success_page_title': "Success page title",
            'success_page_message': "Success page message",
        }

        if form_data:
            for field_name, field_value in form_data.items():
                field_input = self.selenium.find_element_by_name(field_name)
                field_input.send_keys(field_value)

        # Click add widget button
        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()

        logger.debug("""//div[contains(text(), 'Form {0} was created successfully.') and contains(@class, "alert-info")]""".format(constants.TEST_FORM_NAME))

        # Wait until the fobi fobi page opens with the form element in
        WebDriverWait(self.selenium, timeout=TIMEOUT).until(
            lambda driver: driver.find_element_by_xpath(
                """//div[contains(text(), 'Form {0} was created successfully.') and contains(@class, "alert-info")]""".format(constants.TEST_FORM_NAME)
                )
            )

        self.__sleep(wait)

    def __get_form(self):
        """
        Get form object.
        """
        return FormEntry._default_manager.get(name=constants.TEST_FORM_NAME)

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ++++++++++++++++++++ Form element specific ++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def __add_form_element(self, form_element_name, form_element_data, wait=WAIT_FOR):
        """
        Add a single plugin to the form. At this stage we should be in the
        edit form entry interface.
        """
        # Click the add form element button to add a new form element to the form
        add_form_element_link = self.selenium.find_element_by_xpath(
            """//a[contains(text(), 'Choose form element to add') and contains(@class, "dropdown-toggle")]"""
            )
        add_form_element_link.click()

        # Find the parent element
        add_form_element_parent_container = add_form_element_link.find_element_by_xpath('..')

        # Find the container of the available form elements
        add_form_element_available_elements_container = add_form_element_parent_container.find_element_by_xpath(
            '//ul[contains(@class, "dropdown-menu")]'
            )

        # Click on the element we want
        form_element_to_add = add_form_element_available_elements_container.find_element_by_xpath('//a[text()="{0}"]'.format(form_element_name))
        form_element_to_add.click()

        # Adding form data
        if form_element_data:
            # Wait until the add widget view opens
            WebDriverWait(self.selenium, timeout=TIMEOUT).until(
                lambda driver: driver.find_element_by_xpath("""//h1[contains(text(), 'Add "{0}" element to the form')]""".format(form_element_name))
                )

            for field_name, field_value in form_element_data.items():
                field_input = self.selenium.find_element_by_name(field_name)
                field_input.send_keys(field_value)

            # Click add widget button
            self.selenium.find_element_by_xpath('//button[@type="submit"]').click()

        logger.debug(form_element_name)

        # Wait until the fobi fobi page opens with the form element in.
        WebDriverWait(self.selenium, timeout=TIMEOUT).until(
            lambda driver: driver.find_element_by_xpath(
                """//div[contains(text(), 'The form element plugin "{0}" was added successfully.') and contains(@class, "alert-info")]""".format(form_element_name)
                )
            )

    def __test_add_form_elements(self, create_form=False):
        """
        Test of adding multiple form elements. At this point form
        should be created.
        """
        if create_form:
            # Adding a form first
            self.__test_add_form()

        # One by one adding form elements with data.
        # Example follows:
        #
        #self.__add_form_element(
        #    force_text(BooleanSelectPlugin.name),
        #    {
        #        'label': "Test boolean",
        #        'name': "test_boolean",
        #        'help_text': "Lorem ipsum boolean",
        #        'required': False,
        #    }
        #    )

        for plugin_name, plugin_data in TEST_FORM_ELEMENT_PLUGIN_DATA.items():
            # Add form eleement to the form
            self.__add_form_element(plugin_name, plugin_data)

    def __remove_form_element(self, form_element_name, form_element_data, wait=WAIT_FOR):
        """
        Add a single plugin to the form. At this stage we should be in the
        edit form entry interface.
        """
        # Get the label of the given form element in order to delete it later from the form
        delete_form_element_label = self.selenium.find_element_by_xpath(
            """//label[contains(text(), '({0})') and contains(@class, "control-label")]""".format(form_element_name)
            )

        # Get the parent of the label
        delete_form_element_label_parent_container = delete_form_element_label.find_element_by_xpath('..')

        # Click the add form element button to add a new form element to the form
        delete_form_element_link = delete_form_element_label_parent_container.find_element_by_partial_link_text('Delete')
        delete_form_element_link.click()

        logger.debug(form_element_name)

        # Wait until the fobi fobi page opens with the form element in.
        WebDriverWait(self.selenium, timeout=TIMEOUT).until(
            lambda driver: driver.find_element_by_xpath(
                """//div[contains(text(), 'The form element plugin "{0}" was deleted successfully.') and contains(@class, "alert-info")]""".format(form_element_name)
                )
            )

    def __test_remove_form_elements(self):
        """
        Test of removing multiple form elements. At this point form
        should be created.
        """
        for plugin_name, plugin_data in TEST_FORM_ELEMENT_PLUGIN_DATA.items():
            # Add form eleement to the form
            self.__remove_form_element(plugin_name, plugin_data)

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ++++++++++++++++++++ Form handler specific ++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def __add_form_handler(self, form_handler_name, form_handler_data, wait=WAIT_FOR):
        """
        Add a single handler to the form. At this stage we should be in the
        edit form entry interface.
        """
        # This part is necessary, since we need to activate the
        # tab with form handlers. Otherwise Selenium raises
        # an exception about non-visible element on the page
        # that we're trying to fetch.
        form_handlers_tab_link = self.selenium.find_element_by_xpath(
            """//a[@href="#tab-form-handlers"]"""
        )
        form_handlers_tab_link.click()

        # Click the add form element button to add a new form element to the form
        add_form_handler_link = self.selenium.find_element_by_xpath(
            """//a[contains(text(), 'Choose form handler to add') and contains(@class, "dropdown-toggle")]"""
            )
        add_form_handler_link.click()

        # Find the parent element
        add_form_handler_parent_container = add_form_handler_link.find_element_by_xpath('..')

        # Find the container of the available form elements
        add_form_handler_available_elements_container = add_form_handler_parent_container.find_element_by_xpath(
            '//ul[contains(@class, "dropdown-menu")]'
            )

        # Click on the element we want
        form_handler_to_add = add_form_handler_available_elements_container.find_element_by_xpath('//a[text()="{0}"]'.format(form_handler_name))
        form_handler_to_add.click()

        # If has config, there's a need to perform some extra tests.
        if form_handler_data:
            # Wait until the add widget view opens
            WebDriverWait(self.selenium, timeout=TIMEOUT).until(
                lambda driver: driver.find_element_by_xpath("""//h1[contains(text(), 'Add "{0}" handler to the form')]""".format(form_handler_name))
                )

            # Config
            for field_name, field_value in form_handler_data.items():
                field_input = self.selenium.find_element_by_name(field_name)
                field_input.send_keys(field_value)

            # Click add widget button
            self.selenium.find_element_by_xpath('//button[@type="submit"]').click()

        # Wait until the fobi fobi page opens with the form element in.
        WebDriverWait(self.selenium, timeout=TIMEOUT).until(
            lambda driver: driver.find_element_by_xpath(
                """//div[contains(text(), 'The form handler plugin "{0}" was added successfully.') and contains(@class, "alert-info")]""".format(form_handler_name)
                )
            )

    def __test_add_form_handlers(self, create_form=False):
        """
        Test of adding multiple form handlers. At this point form
        should be created.
        """
        if create_form:
            # Adding a form first
            self.__test_add_form()

        # One by one adding form elements with data.
        # Example follows:
        #
        #self.__add_form_element(
        #    force_text(BooleanSelectPlugin.name),
        #    {
        #        'label': "Test boolean",
        #        'name': "test_boolean",
        #        'help_text': "Lorem ipsum boolean",
        #        'required': False,
        #    }
        #    )

        for plugin_name, plugin_data in TEST_FORM_HANDLER_PLUGIN_DATA.items():
            # Add form element to the form
            self.__add_form_handler(plugin_name, plugin_data)

    def __remove_form_handler(self, form_handler_name, form_handler_data, wait=WAIT_FOR):
        """
        Remove a single handler from the form. At this stage we should be in the
        edit form entry interface.
        """
        # This part is necessary, since we need to activate the
        # tab with form handlers. Otherwise Selenium raises
        # an exception about non-visible element on the page
        # that we're trying to fetch.
        form_handlers_tab_link = self.selenium.find_element_by_xpath(
            """//a[@href="#tab-form-handlers"]"""
        )
        form_handlers_tab_link.click()

        # Get the label of the given form element in order to delete it later from the form
        delete_form_handler_label = self.selenium.find_element_by_xpath(
            """//td[contains(text(), '{0}')]""".format(form_handler_name)
            )

        # Get the parent of the label
        delete_form_handler_label_parent_container = delete_form_handler_label.find_element_by_xpath('..')

        # Click the add form element button to add a new form element to the form
        delete_form_handler_link = delete_form_handler_label_parent_container.find_element_by_partial_link_text('Delete')
        delete_form_handler_link.click()

        logger.debug(form_handler_name)

        # Wait until the fobi fobi page opens with the form element in.
        WebDriverWait(self.selenium, timeout=TIMEOUT).until(
            lambda driver: driver.find_element_by_xpath(
                """//div[contains(text(), 'The form handler plugin "{0}" was deleted successfully.') and contains(@class, "alert-info")]""".format(form_handler_name)
                )
            )

    def __test_remove_form_handlers(self):
        """
        Test of removing multiple form handlers. At this point form
        should be created.
        """
        for plugin_name, plugin_data in TEST_FORM_HANDLER_PLUGIN_DATA.items():
            # Remove form handler from the form
            self.__remove_form_handler(plugin_name, plugin_data)

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++ Tests +++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++ General +++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    @skip
    @print_info
    def test_1001_open_dashboard(self):
        """
        Test open dashboard.
        """
        self.__go_to_dashboard()

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ++++++++++++++++++++++ Form specific ++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    @skip
    @print_info
    def test_2001_add_form(self):
        """
        Test add a new form.
        """
        # Clean up database
        db_clean_up()

        self.__test_add_form(wait=WAIT_FOR)

        # Make sure the success message is there
        #self.selenium.find_element_by_xpath(
        #    """//div[text()='Form {0} was created successfully.']""".format(constants.TEST_FORM_NAME)
        #    )

    @skip
    @print_info
    def test_2002_edit_form(self):
        """
        Test edit a form.
        """
        # TODO

    @skip
    @print_info
    def test_2003_delete_form(self):
        """
        Test delete a form.
        """
        # TODO

    @skip
    @print_info
    def test_2004_submit_form(self, wait=WAIT_FOR):
        """
        Test submit form.
        """
        # Clean up database
        db_clean_up()

        # Add form elements
        self.__test_add_form_elements(create_form=True)

        #self.__sleep(wait)

        # Getting a form object
        form = self.__get_form()

        # Getting the form URL
        url = reverse('fobi.view_form_entry', args=[form.slug])
        self.selenium.get('{0}{1}'.format(self.__get_live_server_url(), url))

        # Wait until the edit widget form opens
        WebDriverWait(self.selenium, timeout=TIMEOUT).until(
            lambda driver: driver.find_element_by_xpath('//body[contains(@class, "theme-bootstrap3")]')
            )

        for field_name, field_value in TEST_FORM_FIELD_DATA.items():
            field_input = self.selenium.find_element_by_name(field_name)
            field_input.send_keys(field_value)

        self.__sleep(2)

        # Click add widget button
        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()

        # Wait until the submit success page opens a clear success message.
        WebDriverWait(self.selenium, timeout=TIMEOUT).until(
            lambda driver: driver.find_element_by_xpath(
                """//div[contains(text(), 'Form {0} was submitted successfully.') and contains(@class, "alert-info")]""".format(constants.TEST_FORM_NAME)
                )
            )

        self.__sleep(wait)

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ++++++++++++++++++++ Form element specific ++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    @skip
    @print_info
    def test_3001_add_form_elements(self, wait=WAIT_FOR):
        """
        Test adding form elements.
        """
        # Clean up database
        db_clean_up()

        self.__test_add_form_elements(create_form=True)

        self.__sleep(wait)

    @skip
    @print_info
    def test_3002_remove_form_elements(self):
        """
        Test remove form element.
        """
        # Clean up database
        db_clean_up()

        self.__test_add_form_elements(create_form=True)

        self.__test_remove_form_elements()

    @skip
    @print_info
    def test_3003_edit_form_elements(self):
        """
        Test edit form element.
        """

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ++++++++++++++++++++ Form handler specific ++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    @skip
    @print_info
    def test_4001_add_form_handlers(self, wait=WAIT_FOR):
        """
        Test of adding a single form handler. At this point, if form isn't
        created, it should be.
        """
        # Clean up database
        db_clean_up()

        self.__test_add_form_handlers(create_form=True)

        self.__sleep(wait)

    @skip
    @print_info
    def test_4002_remove_form_handlers(self):
        """
        Test remove form handler.
        """
        # Clean up database
        db_clean_up()

        self.__test_add_form_handlers(create_form=True)

        self.__test_remove_form_handlers()

    @skip
    @print_info
    def test_4003_edit_form_handlers(self):
        """
        Test edit form handler.
        """


if __name__ == '__main__':
    unittest.main()
