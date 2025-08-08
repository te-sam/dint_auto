"""Базовый класс для работы со страницами."""

from time import sleep

from loguru import logger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.config import settings
from pages.locators.locators_order import locator_price_contatiner
from pages.locators.locators_work import (
    locator_btn_in_dialog_from_above,
    locator_close_dialog_constraint,
    locator_start_video,
    locator_stimulate_dialog_from_above,
)
from utils import get_host


class BasePage:
    """Базовый класс для работы со страницами."""

    def __init__(self, driver):
        """Инициализация драйвера."""
        self.driver = driver

    @staticmethod
    def get_url_without_credentials(url: str) -> str:
        """Удаление логина и пароля из URL-адреса.

        Args:
            url: URL-адрес.

        Returns:
            str: URL-адрес без логина и пароля.

        """
        if settings.MODE == "TEST":
            if "@" in url:
                parts_url = url.split("//")
                url = "".join([parts_url[0], "//", parts_url[1].split("@")[1]])

        return url

    def open_main(self) -> None:
        """Открытие главной страницы."""
        host = get_host(add_credentials=True)

        if not self.true_url(
            f"{host}/app/".replace(f"{settings.USER}:{settings.PASSWORD}@", "")
        ):
            self.driver.get(f"{host}/app/")

        script = 'window.localStorage.setItem("videoShow", true);'
        self.driver.execute_script(script)

        if self.find(locator_start_video).is_displayed():
            self.find(locator_close_dialog_constraint).click()

    def find(self, args):
        """Поиск элемента."""
        return self.driver.find_element(*args)

    def finds(self, args) -> None:
        """Поиск нескольких элементов."""
        return self.driver.find_elements(*args)

    def switch_new_tab(self) -> None:
        """Переключение на новую вкладку."""
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])

    def scroll_to_element(self, element):
        """Прокрутка до элемента.

        Args:
            element: искомый элемент.

        """
        ActionChains(self.driver).scroll_to_element(element).perform()

    def wait(self, locator: tuple) -> None:
        """Ожидание появления элемента.

        Args:
            locator: локатор искомого элемента.

        """
        wait = WebDriverWait(self.driver, 5, poll_frequency=0.8)
        wait.until(EC.presence_of_element_located(locator))

    def await_clickable(self, element) -> None:
        """Ожидание кликабельности элемента.

        Args:
            element: искомый элемент.

        """
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable(element))

    def await_visibility(self, element) -> None:
        """Ожидание видимости элемента.

        Args:
            element: искомый элемент.

        """
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(element))

    def true_url(self, true_url: str) -> bool:
        """Проверка на корректность URL-адреса.

        Args:
            true_url: правильный URL-адрес.

        """
        current_url = self.get_url_without_credentials(self.driver.current_url)
        true_url = self.get_url_without_credentials(true_url)

        logger.debug(f"Текущий URL: {current_url}")
        logger.debug(f"Ожидаемый URL: {true_url}")

        return current_url == true_url

    def create_screenshot(self, path: str) -> None:
        """Создание скриншота страницы."""
        sleep(1)
        self.driver.save_screenshot(path)

    def create_screenshot_element(
        self, locator: tuple, saving_path: str
    ) -> None:
        """Создание скриншота элемента.

        Args:
            locator (tuple): локатор элемента для скриншота
            saving_path(str): путь сохранения скриншота

        """
        element = self.find(locator)
        element.screenshot(saving_path)

    def switch_to_tab(self, number: int) -> None:
        """Переключение на вкладку.

        Args:
            number (int): номер вкладки, начиная с 1.

        """
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[number - 1])

    def check_stimulate_dialog_from_above(self, show_dialog: bool) -> None:
        """Проверить, отображается ли стимулирующий диалог сверху над сценой."""
        dialog = self.find(locator_stimulate_dialog_from_above)
        if show_dialog:
            assert dialog.is_displayed(), (
                "Стимулирующий диалог сверху не появился"
            )
        else:
            assert not dialog.is_displayed(), (
                "Стимулирующий диалог сверху появился"
            )

    def click_btn_in_dialog_from_above(self) -> None:
        """Кликнуть по кнопке в стимулирующем диалоге сверху."""
        self.await_visibility(locator_btn_in_dialog_from_above)
        self.find(locator_btn_in_dialog_from_above).click()
        self.wait(locator_price_contatiner)
