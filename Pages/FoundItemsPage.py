from selenium.webdriver.common.by import By

from Configs.config import TestData
from Pages.AccountPage import AccountPage
from Pages.BasePage import BasePage
from Pages.ForgotPasswordPage import ForgotPasswordPage


class FoundItemsPage(BasePage):

    def __init__(self ,driver):
        super().__init__(driver)

    SEARCHED_SUBHEADER = (By.ID, '//*[@id="center_column"]/h1')
    NO_RESULTS_MESSAGE = (By.ID,'//*[@id="center_column"]/p')


    def seached_header_exist(self):
        self.is_enabled(self.SEARCHED_SUBHEADER)

    def no_results_found(self):
        self.get_element_text(self.NO_RESULTS_MESSAGE)

