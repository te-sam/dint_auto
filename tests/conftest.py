import pytest

from selenium import webdriver
from pages.dashboard_page import DashboardPage
from pages.work_page import WorkPage, locator_wall



@pytest.fixture(scope="class")  # autouse=True
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture(scope="function")
def auth(driver):
    auth = WorkPage(driver)
    auth.open_main()
    auth.click_auth_btn()
    auth.enter_login('art.samohwalov@yandex.ru')
    auth.enter_password('123456')
    auth.click_enter_btn()
    auth.wait(locator_wall)


@pytest.fixture(scope="function")
def drop_project(driver):
    yield
    dash = DashboardPage(driver)
    if not dash.true_url("https://online-dint.ulapr.ru/app/projects.php"):
        dash.get_dashboard()
    dash.drop_all_projects()


        