import time

from selenium.webdriver.common.by import By

from Configs.config import TestData
from Pages.BasePage import BasePage


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    FORGOT_PASSWORD_EMAIL = (By.ID, 'email')
    FORGOT_PASSWORD_BTN = (By.XPATH,'//*[@type="form_forgotpassword"]/fieldset/p/button/span')
    FORGOT_PASSWORD_SUCCESSFUL_MESSAGE_ELEMENT = (By.XPATH,'// *[contains( @class ,"alert alert-success")][contains(.,"A confirmation email has been sent to your address: test@test.test")]')

    def enter_email_to_retrieve_password(self,login,):
        self.do_send_keys(self.FORGOT_PASSWORD_EMAIL,login)
        self.do_click(self.FORGOT_PASSWORD_BTN)

    def get_forgot_password_successful_message(self):
        return self.get_element_text(self.FORGOT_PASSWORD_SUCCESSFUL_MESSAGE_ELEMENT)