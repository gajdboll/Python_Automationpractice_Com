import time

import pytest

from selenium.webdriver.support.ui import WebDriverWait

from Configs.config import TestData
from Pages.AccountPage import AccountPage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):


    def test_successful_Login_8(self):
        loginPage = LoginPage(self.driver)
        account_page = loginPage.enter_login(TestData.USER_LOGIN,TestData.PASSWORD)
        title = account_page.get_the_title(TestData.ACCOUNT_PAGE_TITLE)
        assert title == TestData.ACCOUNT_PAGE_TITLE

    def test_Unsuccessful_Login_Invalid_Login_9(self):
        loginPage = LoginPage(self.driver)
        loginPage.enter_login(TestData.WRONG_USER_LOGIN,TestData.PASSWORD)
        error_text = loginPage.get_error_message_for_invalid_login()
        assert error_text == TestData.STRING_FOR_INVALID_EMAIL_DURING_LOGIN

    def test_Unsuccessful_Login_Invalid_Password_10(self):
        loginPage = LoginPage(self.driver)
        loginPage.enter_login(TestData.USER_LOGIN,TestData.WRONG_PASSWORD)
        error_text = loginPage.get_error_message_for_invalid_password()
        assert error_text == TestData.STRING_FOR_INVALID_PASSWORD_DURING_LOGIN

    def test_forgot_password_functionality_22(self):
        loginPage = LoginPage(self.driver)
        forgot_password_page = loginPage.click_forgot_password()
        forgot_password_page.enter_email_to_retrieve_password(TestData.USER_LOGIN)
        error_text = forgot_password_page.get_forgot_password_successful_message()
        assert error_text == TestData.STRING_FOR_SUCCESSFUL_PASSWORD_SENT_MESSAGE