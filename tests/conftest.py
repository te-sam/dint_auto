import pytest

from selenium import webdriver
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


@pytest.fixture(scope="class")  # autouse=True
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture(scope="function")
def auth(driver):
    auth = LoginPage(driver)
    auth.open_main()
    auth.click_auth_btn()
    auth.enter_login_data('art.samohwalov@yandex.ru', '123456')
    auth.click_enter_btn()


@pytest.fixture(scope="function")
def drop_project(driver):
    yield
    dash = DashboardPage(driver)
    if not dash.true_url("https://online-dint.ulapr.ru/app/projects.php"):
        dash.get_dashboard()
    dash.drop_all_projects()


        