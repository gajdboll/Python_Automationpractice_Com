from selenium.webdriver.common.by import By

from Configs.config import TestData
from Pages.BasePage import BasePage


class AccountPage(BasePage):
    """ By locators - object repository """
    MY_ACCOUNT_SUB_HEADER = (By.XPATH ,'//h1[@class=''page-heading'']')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.LOGIN_URL)

    """Page Actions"""
    def my_account_title(self,title):
        return self.get_the_title(title)

    def my_account_Sub_heder_exist(self):
        return self.is_enabled(self.MY_ACCOUNT_SUB_HEADER)

    def get_sub_header_text (self):
        return self.get_element_text(self.MY_ACCOUNT_SUB_HEADER)
