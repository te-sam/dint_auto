import pytest

from config import settings
from pages.dashboard_page import locator_new_project_button
from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def auth_base(driver_class):
    auth = LoginPage(driver_class)
    auth.open_login()
    auth.enter_login(settings.BASE)
    auth.enter_password(settings.BASE)
    auth.click_enter_btn()
    # сюда надо проверку, если не вышло авторизоваться
    auth.wait(locator_new_project_button)
    yield driver_class


@pytest.fixture(scope="class")
def auth_standart(driver_class):
    auth = LoginPage(driver_class)
    auth.open_login()
    auth.enter_login(settings.STANDART)
    auth.enter_password(settings.STANDART)
    auth.click_enter_btn()
    # сюда надо проверку, если не вышло авторизоваться
    auth.wait(locator_new_project_button)
    yield driver_class


@pytest.fixture(scope="class")
def auth_premium(driver_class):
    auth = LoginPage(driver_class)
    auth.open_login()
    auth.enter_login(settings.PREMIUM)
    auth.enter_password(settings.PREMIUM)
    auth.click_enter_btn()
    # сюда надо проверку, если не вышло авторизоваться
    auth.wait(locator_new_project_button)
    yield driver_class


@pytest.fixture(scope="class")
def auth_profi(driver_class):
    auth = LoginPage(driver_class)
    auth.open_login()
    auth.enter_login(settings.PROFI)
    auth.enter_password(settings.PROFI)
    auth.click_enter_btn()
    # сюда надо проверку, если не вышло авторизоваться
    auth.wait(locator_new_project_button)
    yield driver_class


@pytest.fixture(scope="module", params=[settings.BASE])
def auth_module(driver, request):
    auth = LoginPage(driver)
    auth.open_login()
    auth.enter_login(request.param)
    auth.enter_password(request.param)
    auth.click_enter_btn()
    # сюда надо проверку, если не вышло авторизоваться
    auth.wait(locator_new_project_button)
    yield driver