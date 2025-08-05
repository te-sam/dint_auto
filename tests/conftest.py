from time import sleep

from loguru import logger
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from core.config import settings
from pages.work_page import (
    WorkPage,
    locator_3d,
    locator_close_dialog_constraint,
    locator_dialog_guest_constraint,
    locator_dialog_upgrade,
)
from tests.fixtures.auth_fixtures import (
    auth_base_class,
    auth_standart_class,
    auth_premium_class,
    auth_profi_class,
    auth_base_function,
    auth_standart_function,
    auth_premium_function,
    auth_profi_function,
)
from tests.fixtures.project_fixtures import (
    drop_all_project_class,
    paste_project_class,
    drop_all_projects_function,
    paste_project_function,
    drop_project,
    paste_project,
)
from utils import get_auth, get_host, get_phpsessid


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


@pytest.fixture(scope="function")
def close_dialog_constraint_for_guest(driver_class, request):
    """Фикстура для закрытия диалога ограничений для гостя."""
    yield
    work = WorkPage(driver_class)
    dialog_constraint = driver_class.find_element(
        *locator_dialog_guest_constraint
    )
    button_close_dialog_constraint = driver_class.find_element(
        *locator_close_dialog_constraint
    )

    # Получаем параметр из request.param
    param_value = request.param if hasattr(request, "param") else None

    if (
        dialog_constraint.is_displayed()
        and button_close_dialog_constraint.is_displayed()
    ):
        button_close_dialog_constraint.click()
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


@pytest.fixture(scope="function")
def close_dialog_upgrade(driver_class, request):
    """Фикстура для закрытия диалога ограничений для платного тарифа."""
    yield
    work = WorkPage(driver_class)
    work.await_clickable(locator_3d)
    element_3d = work.find(locator_3d)
    dialog_upgrade = work.find(locator_dialog_upgrade)
    button_close_dialog_upgrade = work.find(locator_close_dialog_constraint)

    # Получаем параметр из request.param
    param_value = request.param if hasattr(request, "param") else None

    if (
        dialog_upgrade.is_displayed()
        and button_close_dialog_upgrade.is_displayed()
    ):
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


@pytest.fixture(scope="function")
def delete_account(driver):
    """Фикстура для удаления аккаунта."""
    yield
    phpsessid = get_phpsessid(driver)
    auth = get_auth(driver)
    host = get_host()

    if phpsessid:
        response = requests.post(
            f"{host}/app/lk/client/index.php?r=clientSettings/deleteAccount",
            cookies={"PHPSESSID": phpsessid, "auth": auth},
        )
        if not response.json()["success"]:
            logger.error(
                f"Не удалось удалить аккаунт. Ответ сервера -  {response.json()}"
            )
        else:
            logger.success("Аккаунт удален")
    else:
        logger.warning("Не найдены cookie")
