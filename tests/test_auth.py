"""Тесты авторизации."""

import allure
from loguru import logger

from core.config import settings
from pages.login_page import LoginPage, get_activation_link
from utils import get_host


@allure.feature("Авторизация")
@allure.title("Регистрация аккаунта")
def test_registration(driver, delete_account):
    """Тест регистрации аккаунта, подвтерждение по ссылке"""
    auth = LoginPage(driver)

    with allure.step("Открыть страницу авторизации"):
        auth.open_login()
    with allure.step('Килкнуть по кнопке "Зарегистрироваться"'):
        auth.click_register_login_btn()
    with allure.step("Ввести учетные данные"):
        auth.enter_login(settings.EMAIL_ICMP)
        auth.enter_password(settings.EMAIL_ICMP)
        auth.enter_password2(settings.EMAIL_ICMP)
    with allure.step('Кликнуть по кнопке "Зарегистрироваться"'):
        auth.click_register_start_btn()

    with allure.step("Подтвердить аккаунт"):
        activation_link = get_activation_link()
        assert activation_link
        auth.driver.get(activation_link)

    with allure.step("Перейти в личный кабинет"):
        host = get_host(add_credentials=True)
        link_account = f"{host}/app/lk/client/index.php?r=clientSettings"
        auth.driver.get(link_account)
        assert auth.true_url(link_account)
        logger.success("Аккаунт зарегистрирован")
