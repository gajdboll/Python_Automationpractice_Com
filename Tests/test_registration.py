import time

import pytest

from selenium.webdriver.support.ui import WebDriverWait

from Configs.config import TestData
from Pages.AccountPage import AccountPage
from Pages.LoginPage import LoginPage
from Pages.RegistrationPage import RegistrationPage
from Tests.test_base import BaseTest


class Test_Registration(BaseTest):

    def test_successful_Register_1(self):
        loginPage = LoginPage(self.driver)
        loginPage.enter_email(TestData.NEW_USER_LOGIN)
        reg = RegistrationPage(self.driver)
        reg.select_title()
        reg.enter_name(TestData.FIRST_NAME)
        reg.enter_lastname(TestData.LAST_NAME)
        reg.enter_PHONE(TestData.PHONE)
        reg.enter_PASSWORD(TestData.PASSWORD)
        reg.enter_ADDRESS(TestData.ADDRESS)
        reg.enter_CITY(TestData.CITY)
        reg.select_state(self.STATE,TestData.STATE)
        reg.select_COUNTRY(self.COUNTRY,TestData.COUNTRY)
        reg.enter_POSTCODE(TestData.POSTCODE)
        reg.click_register()
        account = AccountPage(self.driver)
        sub_header = account.get_sub_header_text()
        assert sub_header == TestData.ACCOUNT_SUB_HEADER
        """                            """
    def test_Unsuccessful_Register_2(self):
        loginPage = LoginPage(self.driver)
        loginPage.enter_email(TestData.WRONG_USER_LOGIN)
        error_text = loginPage.get_error_message()
        assert error_text == TestData.STRING_FOR_EXISTING_EMAIL


    def test_Unsuccessful_Register_NO_ZIP_Code_3(self):
        loginPage = LoginPage(self.driver)
        loginPage.enter_email(TestData.NEW_USER_LOGIN)
        reg = RegistrationPage(self.driver)
        reg.select_title()
        reg.enter_name(TestData.FIRST_NAME)
        reg.enter_lastname(TestData.LAST_NAME)
        reg.enter_PHONE(TestData.PHONE)
        reg.enter_PASSWORD(TestData.PASSWORD)
        reg.enter_ADDRESS(TestData.ADDRESS)
        reg.enter_CITY(TestData.CITY)
        reg.select_state(self.STATE, TestData.STATE)
        reg.select_COUNTRY(self.COUNTRY, TestData.COUNTRY)
        #reg.enter_POSTCODE(TestData.POSTCODE)
        reg.click_register()
        error_text = reg.get_no_zip_error()
        assert error_text == TestData.NO_ZIP_CODE

    def test_Unsuccessful_Register_NO_Address_4(self):
        loginPage = LoginPage(self.driver)
        loginPage.enter_email(TestData.NEW_USER_LOGIN)
        reg = RegistrationPage(self.driver)
        reg.select_title()
        reg.enter_name(TestData.FIRST_NAME)
        reg.enter_lastname(TestData.LAST_NAME)
        reg.enter_PHONE(TestData.PHONE)
        reg.enter_PASSWORD(TestData.PASSWORD)
        #reg.enter_ADDRESS(TestData.ADDRESS)
        reg.enter_CITY(TestData.CITY)
        reg.select_state(self.STATE, TestData.STATE)
        reg.select_COUNTRY(self.COUNTRY, TestData.COUNTRY)
        reg.enter_POSTCODE(TestData.POSTCODE)
        reg.click_register()
        error_text = reg.get_no_address_error()
        assert error_text == TestData.NO_ADDRESS

    def test_Unsuccessful_Register_NO_PASSWORD_5(self):
        loginPage = LoginPage(self.driver)
        loginPage.enter_email(TestData.NEW_USER_LOGIN)
        reg = RegistrationPage(self.driver)
        reg.select_title()
        reg.enter_name(TestData.FIRST_NAME)
        reg.enter_lastname(TestData.LAST_NAME)
        reg.enter_PHONE(TestData.PHONE)
        #reg.enter_PASSWORD(TestData.PASSWORD)
        reg.enter_ADDRESS(TestData.ADDRESS)
        reg.enter_CITY(TestData.CITY)
        reg.select_state(self.STATE, TestData.STATE)
        reg.select_COUNTRY(self.COUNTRY, TestData.COUNTRY)
        reg.enter_POSTCODE(TestData.POSTCODE)
        reg.click_register()
        error_text = reg.get_no_password_error()
        assert error_text == TestData.NO_PASSWORD

    def test_Unsuccessful_Register_NO_first_name_6(self):
        loginPage = LoginPage(self.driver)
        loginPage.enter_email(TestData.NEW_USER_LOGIN)
        reg = RegistrationPage(self.driver)
        reg.select_title()
        #reg.enter_name(TestData.FIRST_NAME)
        reg.enter_lastname(TestData.LAST_NAME)
        reg.enter_PHONE(TestData.PHONE)
        reg.enter_PASSWORD(TestData.PASSWORD)
        reg.enter_ADDRESS(TestData.ADDRESS)
        reg.enter_CITY(TestData.CITY)
        reg.select_state(self.STATE, TestData.STATE)
        reg.select_COUNTRY(self.COUNTRY, TestData.COUNTRY)
        reg.enter_POSTCODE(TestData.POSTCODE)
        reg.click_register()
        error_text = reg.get_no_first_name_error()
        assert error_text == TestData.NO_FIRST_NAME

    def test_Unsuccessful_Register_NO_last_name_7(self):
        loginPage = LoginPage(self.driver)
        loginPage.enter_email(TestData.NEW_USER_LOGIN)
        reg = RegistrationPage(self.driver)
        reg.select_title()
        reg.enter_name(TestData.FIRST_NAME)
        #reg.enter_lastname(TestData.LAST_NAME)
        reg.enter_PHONE(TestData.PHONE)
        reg.enter_PASSWORD(TestData.PASSWORD)
        reg.enter_ADDRESS(TestData.ADDRESS)
        reg.enter_CITY(TestData.CITY)
        reg.select_state(self.STATE, TestData.STATE)
        reg.select_COUNTRY(self.COUNTRY, TestData.COUNTRY)
        reg.enter_POSTCODE(TestData.POSTCODE)
        reg.click_register()
        error_text = reg.get_no_last_name_error()
        assert error_text == TestData.NO_LAST_NAME