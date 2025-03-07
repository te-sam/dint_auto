from time import sleep

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.work_page import (
    WorkPage, locator_3d,
    locator_close_dialog_constraint,
    locator_dialog_guest_constraint,
    locator_dialog_upgrade)
from tests.fixtures.auth_fixtures import (
    auth_base, 
    auth_premium, 
    auth_profi,
    auth_standart,
)
from tests.fixtures.project_fixtures import (
    drop_all_project, 
    drop_project,                          
    paste_project,
    paste_project_for_guest
)

# Настройка опций Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")  # Отключаем инфобары
chrome_options.add_argument("--start-maximized")   # Запуск в maximized режиме
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Отключаем автоматизацию
chrome_options.add_experimental_option("useAutomationExtension", False)  # Отключаем расширения автоматизации


def check_internet_with_requests(url="https://ya.ru/", timeout=3) -> bool:
    try:
        response = requests.get(url, timeout=timeout)
        print(response)
        return response.status_code == 200
    except requests.RequestException:
        return False


@pytest.fixture(scope="session", autouse=True)
def ensure_internet_connection():
    if not check_internet_with_requests():
        pytest.exit("Нет подключения к интернету. Проверьте соединение.")


@pytest.fixture(scope="module")  # autouse=True
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(2)
    return chrome_driver


@pytest.fixture(scope="class")
def driver_class(request):
    chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver.maximize_window()
    request.cls.driver_class = chrome_driver
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope="function")
def close_dialog_constraint_for_guest(driver_class):
    yield
    dialog_constraint = driver_class.find_element(*locator_dialog_guest_constraint)
    button_close_dialog_constraint = driver_class.find_element(*locator_close_dialog_constraint)
    if dialog_constraint.is_displayed() and button_close_dialog_constraint.is_displayed():
        button_close_dialog_constraint.click()


@pytest.fixture(scope="function")
def close_dialog_upgrade(driver_class, request):
    yield
    work = WorkPage(driver_class)
    work.await_clickable(locator_3d)
    element_3d = work.find(locator_3d)
    dialog_upgrade = work.find(locator_dialog_upgrade)
    button_close_dialog_upgrade = work.find(locator_close_dialog_constraint)

    # Получаем параметр из request.param
    param_value = request.param if hasattr(request, "param") else None

    if dialog_upgrade.is_displayed() and button_close_dialog_upgrade.is_displayed():
        button_close_dialog_upgrade.click()
    else:
        if param_value:  # Если дилалог должен был появиться, но не появился
            if "active" in element_3d.get_attribute("class"):
                driver_class.refresh()
                element_3d = work.find(locator_3d)
                sleep(2)
                work.click_3d()
            else:
                driver_class.refresh()
                sleep(2)
