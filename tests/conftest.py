import pytest

from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver