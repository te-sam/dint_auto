import configparser

import pytest

from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver

@pytest.fixture(scope="session")
def credentials():
    config = configparser.ConfigParser()
    config.read('config.ini')
    username = config.get('credentials', 'username')
    password = config.get('credentials', 'password')
    return username, password