"""Модуль работы со страницей дашборда."""

from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from core.logger import logger
from pages.base_page import BasePage
from pages.locators.locators_dashboard import (
    l_confirm_delete,
    l_new_project_button,
    l_project_actions_menu,
    l_project_copy,
    l_project_delete,
    l_project_list_items,
    l_project_name_list,
)
from utils import get_host


class DashboardPage(BasePage):
    """Класс работы с дашбордом."""

    def open_dashboard(self) -> None:
        """Открытие дашборда."""
        host = get_host(add_credentials=True)
        sleep(2)
        self.driver.get(f"{host}/app/projects.php")

    def drop_first_project(self) -> None:
        """Удаление первого проекта."""
        project_list = self.find(l_project_actions_menu)
        delete_button = self.find(l_project_delete)
        confirm_delete_button = self.find(l_confirm_delete)

        ActionChains(self.driver).move_to_element(
            project_list
        ).move_to_element(delete_button).click().perform()
        confirm_delete_button.click()

    def copy_first_project(self) -> None:
        """Дублирование первого проекта."""
        project_list = self.find(l_project_actions_menu)
        copy_button = self.find(l_project_copy)
        initial_count = len(self.finds(l_project_list_items))
        logger.debug(f"Количество проектов: {initial_count}")

        ActionChains(self.driver).move_to_element(
            project_list
        ).move_to_element(copy_button).click().perform()

        WebDriverWait(self.driver, 10).until(
            lambda d: len(self.finds(l_project_list_items))
            == initial_count + 1,
            message="Количество проектов не изменилось после дублирования",
        )
        logger.debug(
            f"Количество проектов после дублирования: {len(self.finds(l_project_list_items))}"
        )

    def drop_last_project(self) -> None:
        """Удаление последнего проекта."""
        self.wait(l_project_actions_menu)

        projects = list(self.finds(l_project_actions_menu))
        delete_buttons = list(self.finds(l_project_delete))
        confirm_delete_button = self.find(l_confirm_delete)

        self.scroll_to_element(projects[-1])
        ActionChains(self.driver).move_to_element(
            projects[-1]
        ).move_to_element(delete_buttons[-1]).click().perform()
        confirm_delete_button.click()
        sleep(1)

    def drop_all_projects(self) -> None:
        """Удаление всех проектов."""
        self.await_visibility(l_new_project_button)
        try:
            self.wait(l_project_actions_menu)

            count_projects = len(self.finds(l_project_actions_menu))
            confirm_delete_button = self.find(l_confirm_delete)

            for i in range(count_projects):
                project = self.find(l_project_actions_menu)
                delete_button = self.find(l_project_delete)
                ActionChains(self.driver).move_to_element(
                    project
                ).move_to_element(delete_button).click().perform()
                confirm_delete_button.click()
                sleep(1)
        except:
            logger.info("Нет созданных проектов")

    def is_project_named(self, name_project: str) -> bool:
        """Проверка названия проекта.

        Args:
            name_project (str): Название проекта.

        Returns:
            bool: True - если проект с таким названием есть, False - если нет.

        """
        try:
            self.wait(l_project_name_list)
            project_names = list(self.finds(l_project_name_list))

            for project in project_names:
                logger.info(f"Название проект - {project.text}")
                if project.text == name_project:
                    return True
        except:
            return False

    def get_count_project(self) -> int:
        """Получение количества проектов.

        Returns:
            int: Количество проектов.

        """
        try:
            self.wait(l_project_actions_menu)
            return len(self.finds(l_project_actions_menu))
        except:
            return 0

    def click_new_project(self) -> None:
        """Клик по кнопке создания нового проекта."""
        self.wait(l_new_project_button)
        self.find(l_new_project_button).click()
