"""Модуль работы со страницей дашборда."""

from time import sleep

from loguru import logger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from core.config import settings
from pages.base_page import BasePage

locator_project_list = (By.CLASS_NAME, "project-actions")
locator_project_delete = (By.ID, "delete")
locator_confirm_delete = (By.CLASS_NAME, "btn-delete")
locator_projects = (By.CLASS_NAME, "project")
locator_project_name_list = (By.CLASS_NAME, "project-name")
locator_new_project_button = (By.CLASS_NAME, "new_project_text")


class DashboardPage(BasePage):
    """Класс работы с дашбордом."""

    def get_dashboard(self) -> None:
        """Открытие дашборда."""
        if settings.MODE == "TEST":
            url = f"https://{settings.USER}:{settings.PASSWORD}@online-dint.ulapr.ru/app/projects.php"
        if settings.MODE == "PROD":
            url = f"https://roomplan.ru/app/projects.php"

        sleep(2)
        self.driver.get(url)

    def drop_first_project(self) -> None:
        """Удаление первого проекта."""
        project_list = self.find(locator_project_list)
        delete_button = self.find(locator_project_delete)
        confirm_delete_button = self.find(locator_confirm_delete)

        ActionChains(self.driver).move_to_element(
            project_list
        ).move_to_element(delete_button).click().perform()
        confirm_delete_button.click()

    def drop_last_project(self) -> None:
        """Удаление последнего проекта."""
        self.wait(locator_project_list)

        projects = list(self.finds(locator_project_list))
        delete_buttons = list(self.finds(locator_project_delete))
        confirm_delete_button = self.find(locator_confirm_delete)

        self.scroll_to_element(projects[-1])
        ActionChains(self.driver).move_to_element(
            projects[-1]
        ).move_to_element(delete_buttons[-1]).click().perform()
        confirm_delete_button.click()
        sleep(1)

    def drop_all_projects(self) -> None:
        """Удаление всех проектов."""
        self.await_visibility(locator_new_project_button)
        try:
            self.wait(locator_project_list)

            count_projects = len(self.finds(locator_project_list))
            confirm_delete_button = self.find(locator_confirm_delete)

            for i in range(count_projects):
                project = self.find(locator_project_list)
                delete_button = self.find(locator_project_delete)
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
            self.wait(locator_project_name_list)
            project_names = list(self.finds(locator_project_name_list))

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
            self.wait(locator_project_list)
            return len(self.finds(locator_project_list))
        except:
            return 0

    def click_new_project(self) -> None:
        """Клик по кнопке создания нового проекта."""
        self.wait(locator_new_project_button)
        self.find(locator_new_project_button).click()
