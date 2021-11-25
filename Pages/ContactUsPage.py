from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from self import self

from Configs.config import TestData
from Pages.AccountPage import AccountPage
from Pages.BasePage import BasePage
from Pages.ForgotPasswordPage import ForgotPasswordPage


class ContactUsPage(BasePage):

    def __init__(self ,driver):
        super().__init__(driver)
        self.driver.get(TestData.CONTACT_US_URL)

        SEND_BTN = (By.ID , 'submitMessage')
        EMAIL_CONTACT_US = (By.ID ,'email')
        HEADING_DROP_DOWN = (By.ID,'id_contact')
        MESSAGE = (By.ID,'message')
        INVALID_ERROR_MESSAGE = (By.XPATH, '//div[contains(@class,''alert alert-danger'')]')
        SUB_TITLE_CONTACT_US = (By.XPATH, '/*[@id="center_column"]/h1')
        CONTACT_US_SUCCESS_MESSAGE = (By.XPATH,'// *[ @ id = "center_column"] / p')
    def get_error_when_no_email_passed(self):
        if self.is_enabled(self.CONTACT_US_SUCCESS_MESSAGE):
            return self.get_element_text(self.CONTACT_US_SUCCESS_MESSAGE)

    def contact_us_submit_btn(self):
        self.do_click(self.SEND_BTN)
        if self.is_enabled(self.INVALID_ERROR_MESSAGE):
            return self.get_element_text(self.INVALID_ERROR_MESSAGE)

    def enter_email(self,login):
        self.do_send_keys(self.EMAIL_CONTACT_US,login)


    def enter_message(self,text):
        self.do_send_keys(self.MESSAGE,text)


    def select_values(HEADING_DROP_DOWN, value):
        select = Select(HEADING_DROP_DOWN)
        select.select_by_visible_text(value)


    def get_sub_title_contact_us_header(self):
        self.get_element_text(self.SUB_TITLE_CONTACT_US)