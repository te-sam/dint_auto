"""Модуль для работы со страницей работы с проектом"""

from time import sleep
from typing import Literal

from PIL import Image, ImageChops
from loguru import logger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage

locator_wall = (By.CSS_SELECTOR, '.item[data-tool="wall"]')
locator_canvas = (By.ID, "canvas")
locator_canvas_3D = (By.ID, "view3d")
locator_2d = (By.CSS_SELECTOR, '[data-view="2D"]')
locator_3d = (By.CSS_SELECTOR, '[data-mode="orbit"][data-view="3D"]')
locator_walk = (By.CSS_SELECTOR, '[data-mode="firstPerson"][data-view="3D"]')
locator_auth_btn = (By.CSS_SELECTOR, ".auth-btn")
locator_name = (By.CSS_SELECTOR, "div.logo > span > input")
locator_dashboard = (By.CSS_SELECTOR, "div.logo > a")
locator_auth_btn = (By.CSS_SELECTOR, ".auth-btn")
locator_email_login = (By.ID, "login")
locator_password_login = (By.ID, "password")
locator_enter_btn = (By.ID, "enterButton")
locator_error_login = (By.XPATH, '//*[@id="login_form"]/div[1]/label[2]')
locator_error_password = (By.XPATH, '//*[@id="passwordGroup"]/div/label[2]')
locator_project_dots = (By.CLASS_NAME, "project_dots")
locator_new_project_button = (By.ID, "new_project")
locator_dialog_guest_constraint = (By.ID, "reg_modal")
# locator_close_dialog_constraint = (By.ID, "close")
locator_dialog_upgrade_walk = (By.ID, "fp_upgrade_tarif")
locator_close_dialog_constraint = (By.CSS_SELECTOR, '[title="Close (Esc)"]')
locator_save_button = (By.ID, "save_project")
locator_save_screen_button = (By.ID, "screenshot")
locator_save_to_pdf_button = (By.ID, "print")
locator_save_3d_button = (By.ID, "export")
locator_share_button = (By.ID, "share_project")
locator_close_share_button = (By.CSS_SELECTOR, "div.modal-header > button")
locator_dialog_share = (By.ID, "modal_share_project")
locator_dialog_upgrade = (By.ID, "upgrade_tarif")
locator_alcove_button = (By.CSS_SELECTOR, '[data-tool="alcove"]')  # Ниши
locator_apperture_button = (
    By.CSS_SELECTOR,
    '[data-tool="apperture"]',
)  # Проемы
locator_buttons_catalog_textures = (
    By.CLASS_NAME,
    "img-block",
)  # Каталог текстур
locator_catalog_models = (By.ID, "models")

locator_edit_height = (By.ID, "model_height")
locator_trackbar_height_windowsill = (By.ID, "sill-height")
locator_button_expand_settings_windowsill = (By.CSS_SELECTOR, "#open")
locator_button_turn_column_90_left = (
    By.CSS_SELECTOR,
    "div.column-info > div.content > div.model-shortcut-panel > div.right-model-shortcut-panel > button:nth-child(2)",
)
locator_button_turn_column_90_right = (
    By.CSS_SELECTOR,
    "div.column-info > div.content > div.model-shortcut-panel > div.right-model-shortcut-panel > button:nth-child(3)",
)
locator_start_paint_btn = (By.CLASS_NAME, "empty_btn")


class WorkPage(BasePage):
    """Класс страницы работы с проектом."""

    @staticmethod
    def check_dialog_constraint(
        self, block: bool, locator_dialog: tuple
    ) -> None:
        """Проверка диалога ограничений.

        Args:
            block (bool): True - ограничения должны появляться, False - ограничения не должны появляться.
            locator_dialog (tuple): локатор диалога ограничений.

        """
        self.wait(locator_dialog)
        dialog_constraint = self.find(locator_dialog)
        sleep(0.5)

        if block:
            assert dialog_constraint.is_displayed(), (
                "Диалог ограничений не появился"
            )
        else:
            logger.info("Диалог ограничений не должен появляться")
            assert not dialog_constraint.is_displayed(), (
                "Диалог ограничений появился"
            )

    def click_wall(self) -> None:
        """Кликнуть по кнопке 'Рисовать стены'."""
        self.await_clickable(locator_wall)
        self.find(locator_wall).click()

    def click_2d(self) -> None:
        """Кликнуть по кнопке '2D'."""
        self.await_clickable(locator_2d)
        self.find(locator_2d).click()

    def click_3d(self) -> None:
        """Кликнуть по кнопке '3D'."""
        self.await_clickable(locator_3d)
        self.await_visibility(locator_3d)
        self.find(locator_3d).click()

    def click_walk(self) -> None:
        """Кликнуть по кнопке 'Прогулка'."""
        self.await_clickable(locator_walk)
        self.find(locator_walk).click()

    def first_click_by_canvas(
        self, view: Literal["2d", "3d"], x: int, y: int
    ) -> None:
        """Первый клик по сцене в 2D или 3D.

        Args:
            view (Literal["2d", "3d"]): 2D или 3D.
            x (int): Координата X.
            y (int): Координата Y.

        """
        if view == "2d":
            self.await_visibility(locator_canvas)
            canvas = self.find(locator_canvas)
        if view == "3d":
            self.await_visibility(locator_canvas_3D)
            canvas = self.find(locator_canvas_3D)
        ActionChains(self.driver).move_to_element_with_offset(
            canvas, x, y
        ).click().perform()

    def compare_img(
        self, base_image_path: str, actual_image_path: str
    ) -> bool:
        """Сравнение двух изображений.

        Args:
            base_image_path (str): Путь к базовому изображению.
            actual_image_path (str): Путь к актуальному изображению.

        Returns:
            bool: True - если изображения совпадают, False - если нет.

        """
        base_image = Image.open(base_image_path)
        actual_image = Image.open(actual_image_path)
        diff = ImageChops.difference(base_image, actual_image)

        if diff.getbbox() is None:
            logger.info("Изображения совпадают")
            return True
        else:
            logger.info("Изображения различаются")
            return False

    def rename_project(self, new_name: str) -> None:
        """Переименование проекта.

        Args:
            new_name (str): Новое название проекта.

        """
        self.wait(locator_name)
        self.await_clickable(locator_3d)
        input_element = self.find(locator_name)
        input_element.send_keys(Keys.CONTROL, "a")
        input_element.send_keys(Keys.DELETE)
        input_element.send_keys(new_name)
        input_element.send_keys(Keys.ENTER)

    def open_dashboard(self) -> None:
        """Открытие дашборда по кнопке домика."""
        self.wait(locator_dashboard)
        self.find(locator_dashboard).click()

    def click_auth_btn(self) -> None:
        """Клик по кнопке входа в правом верхнем углу."""
        self.wait(locator_auth_btn)
        self.find(locator_auth_btn).click()

    def enter_login(self, email: str) -> None:
        """Ввод логина в модальное окно входа.

        Args:
            email (str): Электронная почта

        """
        self.find(locator_email_login).send_keys(email)

    def enter_password(self, password: str) -> None:
        """Ввод пароля в модальное окно входа.

        Args:
            password (str): Пароль

        """
        self.find(locator_password_login).send_keys(password)

    def click_enter_btn(self) -> None:
        """Клик по кнопке входа в модальном окне входа."""
        self.wait(locator_enter_btn)
        self.find(locator_enter_btn).click()

    def get_state_label_email(self, attribute: str) -> str:
        """Получение атрибута элемента в модальном окне входа."""
        return self.find(locator_error_login).get_attribute(attribute)

    def get_text_label_email(self) -> str:
        """Получение текста элемента в модальном окне входа."""
        return self.find(locator_error_login).text

    def get_state_label_password(self, attribute: str) -> str:
        """Получение состояния атрибута парля в модальном окне входа."""
        return self.find(locator_error_password).get_attribute(attribute)

    def get_text_label_password(self) -> str:
        """Получение текста элемента в модальном окне входа."""
        return self.find(locator_error_password).text

    def check_dialog_constraint_upgrade(self, block: bool, tarif: str) -> None:
        """Проверка диалога ограничений.

        Args:
            block (bool): Должен ли появиться диалог ограничений.
            tarif (str): Тариф.

        """
        if tarif == "guest":
            locator_dialog = locator_dialog_guest_constraint
        else:
            locator_dialog = locator_dialog_upgrade

        self.check_dialog_constraint(
            self, block=block, locator_dialog=locator_dialog
        )

    def check_dialog_constraint_walk(self, block: bool = True) -> None:
        """Проверка диалога ограничений для режима прогулки.

        Args:
            block (bool): True - диалог должен появляться, False - диалог не должен появляться.

        """
        self.check_dialog_constraint(
            self, block=block, locator_dialog=locator_dialog_upgrade_walk
        )

    def check_dialog_share(self) -> None:
        """Проверка диалога 'Поделиться проектом'."""
        dialog_share = self.find(locator_dialog_share)
        assert dialog_share.is_displayed(), (
            "Окно Поделиться проектом не появилось"
        )
        self.find(locator_close_share_button).click()

    def click_save(self, locator_button: str) -> None:
        """Кликнуть по главной кнопке 'Сохранить' и по подкнопке.

        Args:
            locator_button (str): Локатор подкнопки.

        """
        self.await_clickable(locator_save_button)
        save_button = self.find(locator_save_button)
        save_something_button = self.find(locator_button)
        ActionChains(self.driver).move_to_element(save_button).move_to_element(
            save_something_button
        ).click().perform()

    def click_save_screen(self) -> None:
        """Кликнуть по кнопке 'Сохранить скриншот'."""
        self.click_save(locator_save_screen_button)

    def click_save_to_pdf(self) -> None:
        """Кликнуть по кнопке 'Сохранить в PDF'."""
        self.click_save(locator_save_to_pdf_button)

    def click_save_3d(self) -> None:
        """Кликнуть по кнопке 'Сохранить в 3D'."""
        self.click_save(locator_save_3d_button)

    def click_share(self) -> None:
        """Кликнуть по кнопке 'Поделиться'."""
        self.await_clickable(locator_share_button)
        self.find(locator_share_button).click()

    def click_alcove(self):
        """Кликнуть по кнопке 'Ниши'."""
        self.await_clickable(locator_alcove_button)
        self.find(locator_alcove_button).click()

    def click_apperture(self):
        """Кликнуть по кнопке 'Проем'."""
        self.await_clickable(locator_apperture_button)
        self.find(locator_apperture_button).click()

    def change_height(self, height: int) -> None:
        """Изменить высоту модели.

        Args:
            height (int): Высота модели.

        """
        self.find(locator_edit_height).send_keys(height)

    def click_texture_for_furniture(self, num_texture: int) -> None:
        """Кликнуть по текстуре для мебели.

        Args:
            num_texture (int): Номер текстуры.

        """
        locator = (
            By.CSS_SELECTOR,
            f"#ui > div.model-info > div > div.textures_block > div.textures-info > div:nth-child({num_texture})",
        )
        self.find(locator).click()

    def click_texture_from_catalog(self) -> None:
        """Кликнуть по текстуре из каталога."""
        locator = (By.CSS_SELECTOR, ".img-block.active")
        self.await_clickable(locator)
        self.find(locator).click()

    def expand_settings_windowsill(self) -> None:
        """Развернуть настройки подоконника."""
        locator_windowsill_ranges = (By.CLASS_NAME, "windowsill-ranges")
        if (
            self.find(locator_windowsill_ranges).get_attribute("style")
            != "display: block;"
        ):
            self.find(locator_button_expand_settings_windowsill).click()

    def change_windowsill(self, id_trackbar: str):
        """Кликнуть по трекбару настроек подоконника с id_trackbar.

        Args:
            id_trackbar (str): ID трекбара.

        """
        trackbar = self.find((By.ID, id_trackbar))
        self.await_visibility((By.ID, id_trackbar))
        actions = ActionChains(self.driver)
        actions.click_and_hold(trackbar).move_by_offset(
            0.07, 0
        ).release().perform()

    def turn_column_90_left(self) -> None:
        """Кликнуть по кнопке 'Повернуть колонну на 90 градусов влево'."""
        self.await_clickable(locator_button_turn_column_90_left)
        self.find(locator_button_turn_column_90_left).click()

    def turn_column_90_right(self) -> None:
        """Кликнуть по кнопке 'Повернуть колонну на 90 градусов вправо'."""
        self.await_clickable(locator_button_turn_column_90_right)
        self.find(locator_button_turn_column_90_right).click()

    def click_animation_door(self, id_animation: str):
        """Кликнуть по настройке анимации двери с id_animation.

        Args:
            id_animation (str): ID настройки анимации двери.

        """
        locator_animation = (By.ID, id_animation)
        # self.await_visibility(locator_animation)
        self.find(locator_animation).click()

    def click_button_models(self) -> None:
        """Кликнуть по кнопке 'Мебель' слева."""
        self.await_clickable(locator_catalog_models)
        self.find(locator_catalog_models).click()

    def click_category_menu_models(self, num_category: int) -> None:
        """Кликнуть по категории в меню 'Мебель' с номером num_category.

        Args:
            num_category (int): Номер категории.

        """
        locator_category = (
            By.CSS_SELECTOR,
            f"#main_menu_block > button:nth-child({num_category})",
        )
        self.await_clickable(locator_category)
        self.find(locator_category).click()

    def click_subcategory(self, num_subcategory: int) -> None:
        """Кликнуть по подкатегории с номером num_subcategory.

        Args:
            num_subcategory (int): Номер подкатегории.

        """
        locator_subcategory = (
            By.CSS_SELECTOR,
            f"#ui > div.left-menu-block > div:nth-child(2) > div:nth-child(5) > div:nth-child({num_subcategory})",
        )
        self.await_clickable(locator_subcategory)
        self.find(locator_subcategory).click()

    def add_in_favorite_from_catalog(self) -> None:
        """Добавить в избранное из каталога."""
        locator = (By.ID, "set_like")
        self.await_clickable(locator)
        self.find(locator).click()

    def click_start_button(self):
        """Кликнуть по кнокпке 'Нарисуйте стены' по середине сцены."""
        start_paint_btn = self.find(locator_start_paint_btn)
        if start_paint_btn.is_displayed():
            self.await_clickable(locator_start_paint_btn)
            start_paint_btn.click()
