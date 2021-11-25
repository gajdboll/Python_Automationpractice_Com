from selenium.webdriver.common.by import By

from Configs.config import TestData
from Pages import FoundItemsPage
from Pages.AccountPage import AccountPage
from Pages.BasePage import BasePage
from Pages.ContactUsPage import ContactUsPage
from Pages.ForgotPasswordPage import ForgotPasswordPage


class CartPage(BasePage):

    def __init__(self ,driver):
        super().__init__(driver)


        """elements_= on the page needed for those tests"""
        cart_subheader = 'cart_title'
        EMPTY_CART = (By.XPATH,'//*[@id="center_column"]/p')

    def get_empty_cart_text(self):
        self.get_element_text(self.EMPTY_CART)

    def cart_sub_header_exist(self):
        self.is_enabled(self.cart_subheader)
