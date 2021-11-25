import time

import pytest

from selenium.webdriver.support.ui import WebDriverWait

from Configs.config import TestData
from Pages.AccountPage import AccountPage
from Pages.ContactUsPage import ContactUsPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Contact_Us(BaseTest):

    def navigation_to_Contact_us_11(self):
        home = HomePage(self.driver)
        contact = home.contact_us_click()
        text = contact.get_sub_title_contact_us_header()
        assert  text == TestData.SUB_TITLE_CONTACT_US_MESSAGE

        # intention to change that code for method chaining
    def Contact_us_Message_Sent12(self):
        contact = ContactUsPage(self.driver)
        contact.select_values(TestData.DROP_DOWN_VALUE)
        contact.enter_email(TestData.USER_LOGIN)
        contact.enter_message(TestData.WRONG_PASSWORD)
        text =contact.contact_us_submit_btn
        assert  text == TestData.SUB_TITLE_CONTACT_US_MESSAGE

    def Contact_us_invalid_email_entered_13(self):
        contact = ContactUsPage(self.driver)
        contact.enter_email(TestData.WRONG_USER_LOGIN)
        error_text = contact.get_error_when_no_email_passed()
        assert error_text == TestData.SUCCESS_MESSAGE_AFTER_MESSAGE_SENT