import configparser
import pytest

from selenium import webdriver

from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    return chrome_driver

@pytest.fixture(scope="function")
def auth(driver):
    auth = LoginPage(driver)
    auth.open_main()
    auth.click_auth_btn()
    auth.enter_login_data('art.samohwalov@yandex.ru', '123456')
    auth.click_enter_btn()

@pytest.fixture(scope="session")
def credentials():
    config = configparser.ConfigParser()
    config.read('config.ini')
    username = config.get('credentials', 'username')
    password = config.get('credentials', 'password')
    return username, password