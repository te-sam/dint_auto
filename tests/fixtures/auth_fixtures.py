import pytest

from core.config import settings
from pages.dashboard_page import locator_new_project_button
from pages.login_page import LoginPage


def auth(driver, email: str):
    auth = LoginPage(driver)
    auth.open_login()
    auth.enter_login(email)
    auth.enter_password(email)
    auth.click_enter_btn()
    # сюда надо проверку, если не вышло авторизоваться
    auth.wait(locator_new_project_button)


@pytest.fixture(scope="function")
def auth_base_function(driver, email=settings.BASE):
    auth(driver, email)


@pytest.fixture(scope="class")
def auth_base_class(driver_class, email=settings.BASE):
    auth(driver_class, email)


@pytest.fixture(scope="function")
def auth_standart_function(driver, email=settings.STANDART):
    auth(driver, email)


@pytest.fixture(scope="class")
def auth_standart_class(driver_class, email=settings.STANDART):
    auth(driver_class, email)


@pytest.fixture(scope="function")
def auth_premium_function(driver, email=settings.PREMIUM):
    auth(driver, email)


@pytest.fixture(scope="class")
def auth_premium_class(driver_class, email=settings.PREMIUM):
    auth(driver_class, email)


@pytest.fixture(scope="function")
def auth_profi_function(driver, email=settings.PROFI):
    auth(driver, email)


@pytest.fixture(scope="class")
def auth_profi_class(driver_class, email=settings.PROFI):
    auth(driver_class, email)
