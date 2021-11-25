from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Configs.config import TestData
from Pages.BasePage import BasePage


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.CONTACT_US_URL)

    NO_ZIP_ELEMENT = (By.XPATH,'//*[@id="center_column"]/div/ol/li')


    TITLE = (By.ID,'uniform-id_gender2')
    FIRST_NAME =(By.NAME,'customer_firstname')
    LAST_NAME =(By.NAME,'customer_lastname')
    PASSWORD =(By.NAME,'passwd')
    ADDRESS=(By.NAME,'address1')
    CITY = (By.NAME, 'city')
    STATE = (By.NAME, 'id_state')
    COUNTRY = (By.NAME, 'id_country')
    POSTCODE=(By.NAME,'postcode')
    PHONE = (By.NAME, 'phone_mobile')
    Submit_BUTTON = (By.NAME, 'submitAccount')

    def select_title(self):
        self.do_click(self.TITLE)

    def enter_name(self,name):
        self.do_send_keys(self.FIRST_NAME, name)

    def enter_lastname(self,lastname):
        self.do_send_keys(self.LAST_NAME, lastname)

    def enter_PHONE(self,phone_no):
        self.do_send_keys(self.PHONE, phone_no)

    def enter_PASSWORD(self,passw):
        self.do_send_keys(self.PASSWORD, passw)

    def enter_ADDRESS(self,address):
        self.do_send_keys(self.ADDRESS, address)

    def enter_CITY(self,city):
        self.do_send_keys(self.CITY, city)

    def select_state(self,STATE,state):
        select = Select(STATE)
        select.select_by_visible_text(state)

    def select_COUNTRY(self,COUNTRY,country):
        select = Select(COUNTRY)
        select.select_by_visible_text(country)

    def enter_POSTCODE(self, postcode):
        self.do_send_keys(self.POSTCODE, postcode)

    def enter_PHONE(self,phone):
        self.do_send_keys(self.PHONE, phone)

    def click_register(self):
        self.do_click(self.Submit_BUTTON)
        #return CartPage(self.driver)

    def get_no_zip_error(self):
        self.get_element_text(self.POSTCODE)

    def get_no_address_error(self):
        self.get_element_text(self.ADDRESS)

    def get_no_password_error(self):
        self.get_element_text(self.PASSWORD)

    def get_no_first_name_error(self):
        self.get_element_text(self.FIRST_NAME)

    def get_no_last_name_error(self):
        self.get_element_text(self.LAST_NAME)





def search_click(self):
    self.do_click(self.SEARCH_BTN)
    return FoundItemsPage(self.driver)
