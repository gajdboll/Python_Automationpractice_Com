import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome"], scope ='class')#"firefox"
def init_driver(request):
    """
    Set Up part for setting up env before each time test runs
    :param request:
    :return:
    """
    if request.param == "chrome":
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        #code below got replaced - I no longer use Driver - instead i use DriverManager
       #ser = Service(TestData.CHROME_DRIVER)
       #op = webdriver.ChromeOptions()
       #web_driver = webdriver.Chrome(service=ser, options=op)
    if request.param == "firefox":
        s = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=s)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield
    """
      Set Up part for setting up env before each time test runs
      :param request: 
      :return: 
      """
    driver.close()
    driver.quit()