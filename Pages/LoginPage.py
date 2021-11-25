import time

from selenium.webdriver.common.by import By

from Configs.config import TestData
from Pages.AccountPage import AccountPage
from Pages.BasePage import BasePage
from Pages.ForgotPasswordPage import ForgotPasswordPage


class LoginPage(BasePage):
    """ By locators - object repository """
#Registration panel
    EMAIL_FIELD =(By.CSS_SELECTOR,'#email_create')
    PASSWORD_FIELD = (By.ID, 'passwd')
    SIGN_IN_BTN = (By.CSS_SELECTOR, 'button[id=''SubmitLogin''] span')
    ERROR_MESSAGE_FOR_EXISTING_EMAIL = (By.XPATH, '//div[contains(@class,''alert alert-danger'')][contains(.,''An email address required.'')]')



# Login panel
    EMAIL_FIELD_Login = (By.CSS_SELECTOR, '#email')
    PASSWORD_FIELD_Login = (By.ID, 'passwd')
    SIGN_IN_BTN_Login = (By.CSS_SELECTOR, 'button[id=''SubmitLogin''] span')
    FORGOT_LINK = (By.XPATH,'//a[contains(@title,''Recover your forgotten password'')]')

    ERROR_MESSAGE_FOR_WRONG_LOGIN = (By.XPATH, '//div[contains(@class,''alert alert-danger'')]')
    ERROR_MESSAGE_FOR_WRONG_PASSWORD = (By.XPATH, '//div[contains(@class,''alert alert-danger'')]')

    """ variables for validation    """
    STRING_FOR_EXISTING_EMAIL = 'An email address required.'
    """ constructor"""
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.LOGIN_URL)

    """Page Actions"""

        #self.do_click(self.SIGN_IN_BTN)
    def enter_email(self,login):
        self.do_send_keys(self.EMAIL_FIELD,login)
        self.do_click(self.SIGN_IN_BTN)

       # self.get_element_text(self.ERROR_MESSAGE_FOR_EXISTING_EMAIL)

    def enter_login(self, login,password):
        self.do_send_keys(self.EMAIL_FIELD_Login, login)
        self.do_send_keys(self.PASSWORD_FIELD_Login,password)
        self.do_click(self.SIGN_IN_BTN_Login)
        return AccountPage(self.driver)
        #self.get_element_text(self.ERROR_MESSAGE_FOR_EXISTING_EMAIL)

    def get_error_message(self):
        if self.is_enabled(self.ERROR_MESSAGE_FOR_EXISTING_EMAIL):
            return self.get_element_text(self.ERROR_MESSAGE_FOR_EXISTING_EMAIL)

    def get_error_message_for_invalid_login(self):
        if self.is_enabled(self.ERROR_MESSAGE_FOR_WRONG_LOGIN):
            return self.get_element_text(self.ERROR_MESSAGE_FOR_WRONG_LOGIN)

    def get_error_message_for_invalid_password(self):
        if self.is_enabled(self. ERROR_MESSAGE_FOR_WRONG_PASSWORD):
           return self.get_element_text(self. ERROR_MESSAGE_FOR_WRONG_PASSWORD)

    def click_forgot_password(self):
        self.do_click(self.FORGOT_LINK)
        return ForgotPasswordPage(self.driver)
