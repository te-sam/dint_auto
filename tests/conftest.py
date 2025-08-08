"""Модуль фикстур для работы с тестами."""

import pytest
import requests
from core.logger import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from core.config import settings
from tests.fixtures.auth_fixtures import (
    auth_base_class,
    auth_base_function,
    auth_premium_class,
    auth_premium_function,
    auth_profi_class,
    auth_profi_function,
    auth_standart_class,
    auth_standart_function,
    delete_account,
)
from tests.fixtures.close_dialogs_fixtures import (
    close_dialog_constraint_for_guest,
    close_dialog_upgrade,
    close_dialog_upgrade_walk,
)
from tests.fixtures.project_fixtures import (
    drop_all_project_class,
    drop_all_projects_function,
    drop_project,
    paste_project,
    paste_project_class,
    paste_project_function,
)

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option(
    "excludeSwitches", ["enable-automation"]
)
chrome_options.add_experimental_option("useAutomationExtension", False)


def check_internet_with_requests(url="https://ya.ru/", timeout=3) -> bool:
    """Проверка подключения к интернету.

    Args:
        url (str, optional): URL для проверки.
        timeout (int, optional): таймаут проверки подключения.

    Returns:
        bool: True - подключение есть, False - нет.

    """
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            logger.info("Подключение к интернету есть")
        else:
            logger.error("Нет подключения к интернету")
        return response.status_code == 200
    except requests.RequestException:
        logger.error("Ошибка проверки интернет соединения")
        return False


@pytest.fixture(scope="session", autouse=True)
def ensure_internet_connection():
    """Фикстура для проверки подключения к интернету."""
    if not check_internet_with_requests():
        pytest.exit("Нет подключения к интернету. Проверьте соединение.")


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания драйвера."""
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(2)
    logger.info(f"Тестовая среда: {settings.MODE}")
    return chrome_driver


@pytest.fixture(scope="class")
def driver_class(request):
    """Фикстура для создания драйвера класса."""
    chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver.maximize_window()
    request.cls.driver_class = chrome_driver
    logger.info(f"Тестовая среда: {settings.MODE}")
    yield chrome_driver
    chrome_driver.quit()
