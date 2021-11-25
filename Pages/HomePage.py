from selenium.webdriver.common.by import By

from Configs.config import TestData
from Pages import FoundItemsPage
from Pages.AccountPage import AccountPage
from Pages.BasePage import BasePage
from Pages.CartPage import CartPage
from Pages.ContactUsPage import ContactUsPage
from Pages.ForgotPasswordPage import ForgotPasswordPage


class HomePage(BasePage):

    def __init__(self ,driver):
        super().__init__(driver)
        self.driver.get(TestData.Base_URL)

        """elements_= on the page needed for those tests"""
        SEARCH_BAR =(By.ID, '//*[@id="search_query_top"]')
        SEARCH_BTN = (By.XPATH,'//button[contains(@class,''btn btn-default button-search'')]')
        CONTACT_US_BTN =(By.CSS_SELECTOR,'#contact-link > a')
        CHECKOUT_BTN = (By.XPATH,'//*[contains(@class,''ajax_cart_no_product'')]')
        CART = (By.XPATH,'//*[contains(@title ,"View my shopping cart")]')

    def contact_us_click(self):
        self.do_click(self.CONTACT_US_BTN)
        return ContactUsPage(self.driver)

    def cart_click(self):
        self.do_click(self.CONTACT_US_BTN)
        return CartPage(self.driver)

    def enter_search_with_valid_item(self, valid):
        self.do_send_keys(self.SEARCH_BAR, valid)

    def enter_search_with_invalid_item(self, invalid):
        self.do_send_keys(self.SEARCH_BAR, invalid)

    def search_click(self):
        self.do_click(self.SEARCH_BTN)
        return FoundItemsPage(self.driver)

    def select_values(HEADING_DROP_DOWN, value):
        select = Select(HEADING_DROP_DOWN)
        select.select_by_visible_text(value)

    def get_error_when_no_email_passed(self):
        if self.is_enabled(self.CONTACT_US_SUCCESS_MESSAGE):
            return self.get_element_text(self.CONTACT_US_SUCCESS_MESSAGE)

    def contact_us_submit_btn(self):
        self.do_click(self.SEND_BTN)
        if self.is_enabled(self.INVALID_ERROR_MESSAGE):
            return self.get_element_text(self.INVALID_ERROR_MESSAGE)


