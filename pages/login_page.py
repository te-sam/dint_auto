"""Модуль для работы со страницей входа"""

import email
import imaplib
import time
from email import policy

from bs4 import BeautifulSoup
from loguru import logger
from selenium.webdriver.common.keys import Keys

from core.config import settings
from pages.base_page import BasePage
from pages.locators.locator_login import (
    locator_email_login,
    locator_enter_btn,
    locator_error_login,
    locator_password2_login,
    locator_password_login,
    locator_register_btn,
    locator_register_start_btn,
)
from utils import get_host


class LoginPage(BasePage):
    """Класс работы со страницей входа"""

    def enter_login_data(self, email: str, password: str) -> None:
        """Ввод логина и пароля.

        Args:
            email (str): Электронная почта.
            password (str): Пароль.

        """
        self.find(locator_email_login).send_keys(email)
        self.find(locator_password_login).send_keys(password)

    def enter_login(self, email: str) -> None:
        """Ввод логина.

        Args:
            email (str): Электронная почта.

        """
        element = self.find(locator_email_login)
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(email)

    def enter_password(self, password: str) -> None:
        """Ввод пароля.

        Args:
            password (str): Пароль.

        """
        element = self.find(locator_password_login)
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(password)

    def enter_password2(self, password: str) -> None:
        """Ввод пароля для подтверждения.

        Args:
            password (str): Пароль.

        """
        element = self.find(locator_password2_login)
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(password)

    def click_enter_btn(self):
        """Клик по кнопке входа."""
        self.wait(locator_enter_btn)
        self.find(locator_enter_btn).click()

    def get_state_label(self, attribute):
        """Получение состояния лейбла."""
        return self.find(locator_error_login).get_attribute(attribute)

    def get_text_label(self) -> str:
        """Получение текста лейбла."""
        return self.find(locator_error_login).text

    def open_login(self) -> None:
        """Открытие страницы входа"""
        host = get_host(add_credentials=True)
        self.driver.get(f"{host}/app/lk/client/index.php?r=loginClient")
        script = 'window.localStorage.setItem("videoShow", true);'
        self.driver.execute_script(script)

    def click_register_login_btn(self) -> None:
        """Клик по кнопке "Зарегистрироваться" сверху на странице входа"""
        self.wait(locator_register_btn)
        self.find(locator_register_btn).click()

    def click_register_start_btn(self) -> None:
        """Клик по кнопке "Зарегистрироваться" после ввода данных"""
        self.wait(locator_register_start_btn)
        self.find(locator_register_start_btn).click()


def get_activation_link() -> str:
    """Извлекает ссылку активации из письма"""
    try:
        mail = imaplib.IMAP4_SSL("imap.yandex.ru", 993)
        mail.login(settings.EMAIL_ICMP, settings.PASSWORD_ICMP)

        for _ in range(5):
            mail.select("inbox")
            status, messages = mail.search(None, '(UNSEEN FROM "RoomPlan")')
            if status != "OK":
                raise Exception("Ошибка поиска письма")

            if not messages[0]:
                logger.info("Нет непрочитанных писем от RoomPlan")
                time.sleep(2)
                continue
            else:
                break

        if not messages[0]:
            raise Exception("Нет непрочитанных писем от RoomPlan")

        latest_email_id = messages[0].split()[-1]
        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        if status != "OK":
            raise Exception("Ошибка загрузки письма")

        msg = email.message_from_bytes(msg_data[0][1], policy=policy.default)

        # Сохранение HTML-части
        html_content = None
        for part in msg.walk():
            if part.get_content_type() == "text/html":
                charset = part.get_content_charset() or "utf-8"
                html_content = part.get_content()
                break

        if html_content:
            soup = BeautifulSoup(html_content, "html.parser")
            link_texts = []

            for a_tag in soup.find_all("a", href=True):
                link_text = a_tag.get_text(strip=True)
                link_texts.append(link_text)

            if settings.MODE == "TEST":
                host = "online-dint.ulapr.ru"
                return link_texts[1].replace(
                    host, f"{settings.USER}:{settings.PASSWORD}@{host}"
                )
            else:
                return link_texts[1]
        else:
            raise Exception("HTML-часть письма не найдена")
    except Exception as e:
        logger.error(f"Ошибка извлечения ссылки для активации: {str(e)}")
    finally:
        if "mail" in locals():
            mail.logout()
