class TestData:
    """CHROME DRIVER PATH USED ON THE BEGINING OF THE PROJECT"""
    CHROME_DRIVER = 'C:/Users/Gajdzio/PycharmProjects/PythonAutomation/Drivers/chromedriver.exe'

    BASE_URL ='http://automationpractice.com/'
    LOGIN_URL ='http://automationpractice.com/index.php?controller=authentication&back=my-account'
    CONTACT_US_URL = 'http://automationpractice.com/index.php?controller=contact'

    WRONG_USER_LOGIN = 'test1'
    WRONG_PASSWORD = '???'

    NEW_USER_LOGIN = 'newtest@test.test'

    USER_LOGIN ='test@test.test1'
    PASSWORD = 'test123'

    """Login page variables"""
    STRING_FOR_EXISTING_EMAIL = 'An email address required.'
    STRING_FOR_INVALID_EMAIL_DURING_LOGIN ='Invalid email address.'
    STRING_FOR_INVALID_PASSWORD_DURING_LOGIN ='Invalid password.'
    """Forgot password page variables"""
    STRING_FOR_SUCCESSFUL_PASSWORD_SENT_MESSAGE  = 'A confirmation email has been sent to your address: test @ test.test1'
    """Account page variables"""
    ACCOUNT_PAGE_TITLE = 'My Account - My Store'
    ACCOUNT_SUB_HEADER ='MY ACCOUNT'
    """Contact Us page variables"""
    STRING_FOR_INVALID_EMAIL_DURING_CONTACT_US = 'Invalid email address.'
    DROP_DOWN_VALUE = 'Webmaster'
    SUB_TITLE_CONTACT_US_MESSAGE ='CUSTOMER SERVICE - CONTACT US'
    SUCCESS_MESSAGE_AFTER_MESSAGE_SENT ='Your message has been successfully sent to our team.'
    """Home page variables"""
    VALID_SEARCH = 'DRESS'
    INVALID_SEARCH = 'X'
    """FOUNDITHEMS page variables"""
    NO_RESULTS_ON_PAGE ='No results were found for your search "X"'
    """cart page variables"""
    EMPTY_CART_MESSAGE ='Your shopping cart is empty.'
    """register page variables"""

    FIRST_NAME = 'JOANNA'
    LAST_NAME = 'TEST'
    PASSWORD = 'test123'
    ADDRESS = 'MIAMI'
    CITY = 'MIAMI2'
    STATE = 'Alaska'
    COUNTRY = 'United States'
    POSTCODE = '00000'
    PHONE = '085749621'


    NO_PHONE='You must register at least one phone number.'
    NO_LAST_NAME ='lastname is required.'
    NO_FIRST_NAME ='firstname is required.'
    NO_PASSWORD ='passwd is required.'
    NO_ADDRESS ='address1 is required.'
    NO_CITY ='city is required.'
    NO_ZIP_CODE ='The Zip/Postal code you''ve entered is invalid. It must follow this format: 00000'
    NO_COUNTRY ='This country requires you to choose a State.'

