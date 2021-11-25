from Configs.config import TestData
from Pages.AccountPage import AccountPage
from Pages.ContactUsPage import ContactUsPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_From_Home(BaseTest):

    def items_are_listed_14(self):
        home = HomePage(self.driver)
        home.enter_search_with_valid_item(TestData.VALID_SEARCH)
        found_items = home.search_click()
        if found_items.seached_header_exist():
            print('true')

    def items_are_not_listed_15(self):
        home = HomePage(self.driver)
        home.enter_search_with_invalid_item(TestData.INVALID_SEARCH)
        found_items = home.search_click()
        text = found_items.no_results_found()
        assert text == TestData.NO_RESULTS_ON_PAGE

    def empty_cart_validation_16(self):
        home = HomePage(self.driver)
        cart = home.cart_click()
        text = cart.get_empty_cart_text()
        assert text == TestData.EMPTY_CART_MESSAGE