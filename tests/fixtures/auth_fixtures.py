"""Модуль фикстур для работы с авторизацией."""

from loguru import logger
import pytest
import requests

from core.config import settings
from pages.dashboard_page import locator_new_project_button
from pages.login_page import LoginPage
from utils import get_auth, get_host, get_phpsessid


def auth(driver, email: str) -> None:
    """Авторизация.

    Args:    
        driver (WebDriver): Драйвер браузера.
        email (str): Электронная почта.
    """
    auth = LoginPage(driver)
    auth.open_login()
    auth.enter_login(email)
    auth.enter_password(email)
    auth.click_enter_btn()
    # сюда надо проверку, если не вышло авторизоваться
    auth.wait(locator_new_project_button)


@pytest.fixture(scope="function")
def auth_base_function(driver, email=settings.BASE):
    """Фикстура для авторизации аккаунта с бесплатным тарифом при работе с функцией."""
    auth(driver, email)


@pytest.fixture(scope="class")
def auth_base_class(driver_class, email=settings.BASE):
    """Фикстура для авторизации аккаунта с бесплатным тарифом при работе с классом."""
    auth(driver_class, email)


@pytest.fixture(scope="function")
def auth_standart_function(driver, email=settings.STANDART):
    """Фикстура для авторизации аккаунта со стандартным тарифом при работе с функцией."""
    auth(driver, email)


@pytest.fixture(scope="class")
def auth_standart_class(driver_class, email=settings.STANDART):
    """Фикстура для авторизации аккаунта со стандартным тарифом при работе с классом."""
    auth(driver_class, email)


@pytest.fixture(scope="function")
def auth_premium_function(driver, email=settings.PREMIUM):
    """"""
    auth(driver, email)


@pytest.fixture(scope="class")
def auth_premium_class(driver_class, email=settings.PREMIUM):
    """Фикстура для авторизации аккаунта с премиум тарифом при работе с классом."""
    auth(driver_class, email)


@pytest.fixture(scope="function")
def auth_profi_function(driver, email=settings.PROFI):
    auth(driver, email)


@pytest.fixture(scope="class")
def auth_profi_class(driver_class, email=settings.PROFI):
    """Фикстура для авторизации аккаунта с премиум тарифом при работе с классом."""
    auth(driver_class, email)


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