"""Модуль для работы со страницей работы с проектом"""

from time import sleep
from typing import Literal

from core.logger import logger
from PIL import Image, ImageChops
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.locators.locators_order import l_price_contatiner
from pages.locators.locators_work import (
    l_2d,
    l_3d,
    l_alcove_button,
    l_apperture_button,
    l_auth_btn,
    l_btn_in_dialog_count_models,
    l_button_expand_settings_windowsill,
    l_button_turn_column_90_left,
    l_button_turn_column_90_right,
    l_canvas,
    l_canvas_3D,
    l_catalog_models,
    l_close_dialog_constraint,
    l_close_share_button,
    l_dashboard,
    l_dialog_count_models,
    l_dialog_guest_constraint,
    l_dialog_share,
    l_dialog_upgrade,
    l_dialog_upgrade_walk,
    l_edit_height,
    l_email_login,
    l_enter_btn,
    l_error_login,
    l_error_password,
    l_name,
    l_password_login,
    l_save_3d_button,
    l_save_button,
    l_save_screen_button,
    l_save_to_pdf_button,
    l_share_button,
    l_start_paint_btn,
    l_start_video,
    l_walk,
    l_wall,
)


class WorkPage(BasePage):
    """Класс страницы работы с проектом."""

    @staticmethod
    def check_dialog_constraint(
        self, block: bool, l_dialog: tuple
    ) -> None:
        """Проверка диалога ограничений.

        Args:
            block (bool): True - ограничения должны появляться, False - ограничения не должны появляться.
            l_dialog (tuple): локатор диалога ограничений.

        """
        self.wait(l_dialog)
        dialog_constraint = self.find(l_dialog)
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

    def close_start_video(self) -> None:
        if self.find(l_start_video).is_displayed():
            self.find(l_close_dialog_constraint).click()

    def click_wall(self) -> None:
        """Кликнуть по кнопке 'Рисовать стены'."""
        self.await_clickable(l_wall)
        self.find(l_wall).click()

    def click_2d(self) -> None:
        """Кликнуть по кнопке '2D'."""
        self.await_clickable(l_2d)
        self.find(l_2d).click()

    def click_3d(self) -> None:
        """Кликнуть по кнопке '3D'."""
        self.await_clickable(l_3d)
        self.await_visibility(l_3d)
        self.find(l_3d).click()

    def click_walk(self) -> None:
        """Кликнуть по кнопке 'Прогулка'."""
        self.await_clickable(l_walk)
        self.find(l_walk).click()

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
            self.await_visibility(l_canvas)
            canvas = self.find(l_canvas)
        if view == "3d":
            self.await_visibility(l_canvas_3D)
            canvas = self.find(l_canvas_3D)
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
        self.wait(l_name)
        self.await_clickable(l_3d)
        input_element = self.find(l_name)
        input_element.send_keys(Keys.CONTROL, "a")
        input_element.send_keys(Keys.DELETE)
        input_element.send_keys(new_name)
        input_element.send_keys(Keys.ENTER)

    def open_dashboard(self) -> None:
        """Открытие дашборда по кнопке домика."""
        self.wait(l_dashboard)
        self.find(l_dashboard).click()

    def click_auth_btn(self) -> None:
        """Клик по кнопке входа в правом верхнем углу."""
        self.wait(l_auth_btn)
        self.find(l_auth_btn).click()

    def enter_login(self, email: str) -> None:
        """Ввод логина в модальное окно входа.

        Args:
            email (str): Электронная почта

        """
        self.find(l_email_login).send_keys(email)

    def enter_password(self, password: str) -> None:
        """Ввод пароля в модальное окно входа.

        Args:
            password (str): Пароль

        """
        self.find(l_password_login).send_keys(password)

    def click_enter_btn(self) -> None:
        """Клик по кнопке входа в модальном окне входа."""
        self.wait(l_enter_btn)
        self.find(l_enter_btn).click()

    def get_state_label_email(self, attribute: str) -> str:
        """Получение атрибута элемента в модальном окне входа."""
        return self.find(l_error_login).get_attribute(attribute)

    def get_text_label_email(self) -> str:
        """Получение текста элемента в модальном окне входа."""
        return self.find(l_error_login).text

    def get_state_label_password(self, attribute: str) -> str:
        """Получение состояния атрибута парля в модальном окне входа."""
        return self.find(l_error_password).get_attribute(attribute)

    def get_text_label_password(self) -> str:
        """Получение текста элемента в модальном окне входа."""
        return self.find(l_error_password).text

    def check_dialog_constraint_upgrade(self, block: bool, tarif: str) -> None:
        """Проверка диалога ограничений.

        Args:
            block (bool): Должен ли появиться диалог ограничений.
            tarif (str): Тариф.

        """
        if tarif == "guest":
            l_dialog = l_dialog_guest_constraint
        else:
            l_dialog = l_dialog_upgrade

        self.check_dialog_constraint(
            self, block=block, l_dialog=l_dialog
        )

    def check_dialog_constraint_walk(self, block: bool = True) -> None:
        """Проверка диалога ограничений для режима прогулки.

        Args:
            block (bool): True - диалог должен появляться, False - диалог не должен появляться.

        """
        self.check_dialog_constraint(
            self, block=block, l_dialog=l_dialog_upgrade_walk
        )

    def check_dialog_share(self) -> None:
        """Проверка диалога 'Поделиться проектом'."""
        dialog_share = self.find(l_dialog_share)
        assert dialog_share.is_displayed(), (
            "Окно Поделиться проектом не появилось"
        )
        self.find(l_close_share_button).click()

    def click_save(self, l_button: str) -> None:
        """Кликнуть по главной кнопке 'Сохранить' и по подкнопке.

        Args:
            l_button (str): Локатор подкнопки.

        """
        self.await_clickable(l_save_button)
        save_button = self.find(l_save_button)
        save_something_button = self.find(l_button)
        ActionChains(self.driver).move_to_element(save_button).move_to_element(
            save_something_button
        ).click().perform()

    def click_save_screen(self) -> None:
        """Кликнуть по кнопке 'Сохранить скриншот'."""
        self.click_save(l_save_screen_button)

    def click_save_to_pdf(self) -> None:
        """Кликнуть по кнопке 'Сохранить в PDF'."""
        self.click_save(l_save_to_pdf_button)

    def click_save_3d(self) -> None:
        """Кликнуть по кнопке 'Сохранить в 3D'."""
        self.click_save(l_save_3d_button)

    def click_share(self) -> None:
        """Кликнуть по кнопке 'Поделиться'."""
        self.await_clickable(l_share_button)
        self.find(l_share_button).click()

    def click_alcove(self):
        """Кликнуть по кнопке 'Ниши'."""
        self.await_clickable(l_alcove_button)
        self.find(l_alcove_button).click()

    def click_apperture(self):
        """Кликнуть по кнопке 'Проем'."""
        self.await_clickable(l_apperture_button)
        self.find(l_apperture_button).click()

    def change_height(self, height: int) -> None:
        """Изменить высоту модели.

        Args:
            height (int): Высота модели.

        """
        self.find(l_edit_height).send_keys(height)

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
        l_windowsill_ranges = (By.CLASS_NAME, "windowsill-ranges")
        if (
            self.find(l_windowsill_ranges).get_attribute("style")
            != "display: block;"
        ):
            self.find(l_button_expand_settings_windowsill).click()

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

    def turn_column(self, direction: Literal["left", "right"]) -> None:
        """Кликнуть по кнопке 'Повернуть колонну'.

        Args:
            direction (Literal["left", "right"]): Направление поворота.

        """
        if direction == "left":
            locator = l_button_turn_column_90_left
        else:
            locator = l_button_turn_column_90_right

        self.await_clickable(locator)
        self.find(locator).click()

    def click_animation_door(self, id_animation: str):
        """Кликнуть по настройке анимации двери с id_animation.

        Args:
            id_animation (str): ID настройки анимации двери.

        """
        l_animation = (By.ID, id_animation)
        # self.await_visibility(l_animation)
        self.find(l_animation).click()

    def click_button_models(self) -> None:
        """Кликнуть по кнопке 'Мебель' слева."""
        self.await_clickable(l_catalog_models)
        self.find(l_catalog_models).click()

    def click_category_menu_models(self, num_category: int) -> None:
        """Кликнуть по категории в меню 'Мебель' с номером num_category.

        Args:
            num_category (int): Номер категории.

        """
        l_category = (
            By.CSS_SELECTOR,
            f"#main_menu_block > button:nth-child({num_category})",
        )
        self.await_clickable(l_category)
        self.find(l_category).click()

    def click_subcategory(self, num_subcategory: int) -> None:
        """Кликнуть по подкатегории с номером num_subcategory.

        Args:
            num_subcategory (int): Номер подкатегории.

        """
        l_subcategory = (
            By.CSS_SELECTOR,
            f"#ui > div.left-menu-block > div:nth-child(2) > div:nth-child(5) > div:nth-child({num_subcategory})",
        )
        self.await_clickable(l_subcategory)
        self.find(l_subcategory).click()

    def add_in_favorite_from_catalog(self) -> None:
        """Добавить в избранное из каталога."""
        locator = (By.ID, "set_like")
        self.await_clickable(locator)
        self.find(locator).click()

    def click_start_button(self):
        """Кликнуть по кнокпке 'Нарисуйте стены' по середине сцены."""
        start_paint_btn = self.find(l_start_paint_btn)
        if start_paint_btn.is_displayed():
            self.await_clickable(l_start_paint_btn)
            start_paint_btn.click()

    def check_dialog_count_models(self, show_dialog: bool) -> None:
        """Проверить, отображается ли диалог с количеством моделей.

        Args:
            show_dialog (bool): Показывать ли диалог.

        """
        dialog = self.find(l_dialog_count_models)
        if show_dialog:
            assert dialog.is_displayed(), (
                "Диалог с количеством моделей не появился"
            )
        else:
            assert not dialog.is_displayed(), (
                "Диалог с количеством моделей появился"
            )

    def click_btn_in_dialog_count_models(self) -> None:
        """Кликнуть по кнопке 'Подключить сейчас' в диалоге с количеством моделей."""
        self.await_clickable(l_btn_in_dialog_count_models)
        self.find(l_btn_in_dialog_count_models).click()
        self.wait(l_price_contatiner)
