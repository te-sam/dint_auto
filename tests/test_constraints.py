from time import sleep
from typing import Literal

import allure
import pytest
from loguru import logger

from pages.dashboard_page import DashboardPage
from pages.work_page import WorkPage


class BaseConstraints:
    """Базовый класс для тестов ограничений"""

    def rename_project(self, block=False):
        """Проверка ограничений для переименования проекта

        Args:
            block (bool, optional): Должен ли появиться диалог ограничений.

        """
        logger.info(f"Тариф = {self.tarif}")
        name_project = "test"
        work = WorkPage(self.driver_class)
        dash = DashboardPage(self.driver_class)

        with allure.step("Открыть главную страницу"):
            work.open_main()
            sleep(2)

        with allure.step("Переименовать проект"):
            work.rename_project(name_project)
            if self.tarif == "guest":
                with allure.step("Проверка диалога ограничений"):
                    work.check_dialog_constraint_upgrade(block, self.tarif)
            else:  # Иначе проверяем, что проект переименовался
                sleep(2)

                with allure.step("Открыть дашборд"):
                    work.open_dashboard()

                with allure.step("Проверить переименовался ли проект"):
                    if not block:
                        assert dash.is_project_named(name_project), (
                            "Проект не переименовался"
                        )

    def share_project(self, block=False):
        """Проверка ограничений для функции "Поделиться проектом"

        Args:
            block (bool, optional): Должен ли появиться диалог ограничений.

        """
        work = WorkPage(self.driver_class)

        with allure.step("Открыть главную страницу"):
            work.open_main()
            sleep(2)

        with allure.step('Кликнуть "Поделиться проеком"'):
            work.click_share()
            sleep(2)

        with allure.step("Проверить появление диалога ограничений"):
            if not block:
                work.check_dialog_share()
                # work.driver.refresh()
            if self.tarif == "guest":
                work.check_dialog_constraint_upgrade(block, self.tarif)

    def constraint_alcove(self, block=False):
        """Проверка ограничений для ниш

        Args:
            block (bool, optional): Должен ли появиться диалог ограничений.

        """
        work = WorkPage(self.driver_class)

        with allure.step("Открыть главную страницу"):
            work.open_main()
            sleep(2)
        with allure.step('Кликнуть "Ниши"'):
            work.click_alcove()
        with allure.step("Проверить появление диалога ограничений"):
            work.check_dialog_constraint_upgrade(block, self.tarif)

    def constraint_save_3d(self, block=False):
        """Проверка ограничений для экспорта в 3D

        Args:
            block (bool, optional): Должен ли появиться диалог ограничений.

        """
        work = WorkPage(self.driver_class)

        with allure.step('Кликнуть "3D экспорт"'):
            work.click_save_3d()

        with allure.step("Проверить появление диалога ограничений"):
            work.check_dialog_constraint_upgrade(block, self.tarif)

    def constraint_save_to_pdf(self, block=False):
        """Проверка ограничений для экспорта в PDF.

        Args:
            block (bool, optional): Должен ли появиться диалог ограничений.

        """
        work = WorkPage(self.driver_class)

        with allure.step('Кликнуть "Экспорт в PDF"'):
            work.click_save_to_pdf()

        with allure.step("Проверить появление диалога ограничений"):
            work.check_dialog_constraint_upgrade(block, self.tarif)

        if not block:
            self.driver_class.refresh()

    def constraint_apperture(
        self,
        block=False,
    ):
        """Проверка ограничений для проемов.

        Args:
            block (bool, optional): Должен ли появиться диалог ограничений.

        """
        work = WorkPage(self.driver_class)

        with allure.step('Кликнуть "Проемы"'):
            work.click_apperture()

        with allure.step("Проверить появление диалога ограничений"):
            work.check_dialog_constraint_upgrade(block, self.tarif)

    def constraint_walk(self, block=False):
        """Проверка ограничений для режима прогулки

        Args:
            block (bool, optional): Должен ли появиться диалог ограничений.

        """
        work = WorkPage(self.driver_class)

        with allure.step('Кликнуть "Прогулка"'):
            work.click_walk()

        with allure.step("Проверить появление диалога ограничений"):
            if self.tarif == "free":
                work.check_dialog_constraint_walk(block)
            else:
                work.check_dialog_constraint_upgrade(block, self.tarif)

    def constraint_change_hight(self, block=False):
        """Проверка ограничений для изменения высоты объекта

        Args:
            block (bool, optional): Должен ли появиться диалог ограничений.

        """
        work = WorkPage(self.driver_class)

        with allure.step("Перейти в 3D"):
            work.click_3d()

        with allure.step("Кликнуть по дивану"):
            work.first_click_by_canvas("3d", 168, 23)

        with allure.step("Изменить высоту объекта"):
            work.change_height(10)

        with allure.step("Проверить появление диалога ограничений"):
            work.check_dialog_constraint_upgrade(block, self.tarif)

    def constraint_change_texture(self, block=False):
        """Проверка ограничений для изменения текстуры.

        Args:
            block (bool, optional): Должен ли появиться диалог ограничений.

        """
        work = WorkPage(self.driver_class)
        with allure.step("Перейти в 3D"):
            work.click_3d()

        with allure.step("Кликнуть по дивану"):
            work.first_click_by_canvas("3d", 168, 23)

        with allure.step("Перейти в каталог текстур"):
            work.click_texture_for_furniture(1)

        with allure.step("Перейти по активной текстуре"):
            work.click_texture_from_catalog()

        with allure.step("Проверить появление диалога ограничений"):
            work.check_dialog_constraint_upgrade(block, self.tarif)

    def constraint_change_windowsill(self, id_trackbar, block=False):
        """Проверка ограничений для изменений подоконника.

        Args:
            id_trackbar (int): ID трекбара для изменения подоконника
            block (bool, optional): Должен ли появиться диалог ограничений.

        """
        work = WorkPage(self.driver_class)
        with allure.step("Кликнуть по окну"):
            work.first_click_by_canvas("3d", 140, -158.5)

        # with allure.step("Развернуть настройки подоконника"):
        #     work.expand_settings_windowsill()

        with allure.step("Изменить характеристику подоконника"):
            work.change_windowsill(id_trackbar)

        with allure.step("Проверить появление диалога ограничений"):
            work.check_dialog_constraint_upgrade(block=block, tarif=self.tarif)

    def constraint_turn_column(
        self, direction: Literal["left", "right"], block: bool = False
    ):
        """Проверка ограничений для изменений колонны.

        Args:
            block (bool, optional): Должен ли появиться диалог ограничений.

        """
        work = WorkPage(self.driver_class)
        with allure.step("Кликнуть по колонне"):
            # X = 0, Y = -79.5
            x, y = 0, -79.5

            if self.tarif == "premium" or self.tarif == "profi":
                x, y = 20, -78.5

            logger.info(f"Тариф = {self.tarif}")
            work.first_click_by_canvas("3d", x, y)
        with allure.step("Повернуть колонную на 90 влево"):
            work.turn_column(direction=direction)

        with allure.step("Проверить появление диалога ограничений"):
            work.check_dialog_constraint_upgrade(block, self.tarif)

    def constraint_animation_door(self, id_animation, block=False):
        """Проверка ограничений для анимации двери.

        Args:
            id_animation (int): ID анимации двери
            block (bool, optional): Должен ли появиться диалог ограничений.

        """
        work = WorkPage(self.driver_class)
        with allure.step("Кликнуть по двери"):
            # X = -133, Y = -207.5
            x, y = -133, -207.5

            if self.tarif == "premium" or self.tarif == "profi":
                x, y = -116, -184.5

            work.first_click_by_canvas("3d", x, y)
        with allure.step(f"Изменить анимацию {id_animation}"):
            work.click_animation_door(id_animation)
        with allure.step("Проверить появление диалога ограничений"):
            work.check_dialog_constraint_upgrade(block, self.tarif)

    def constraint_favorites(self, block=False):
        """Проверка ограничений для избранного.

        Args:
            block (bool, optional): Должен ли появиться диалог ограничений.

        """
        work = WorkPage(self.driver_class)
        with allure.step("Перейти в катлог мебели"):
            work.click_button_models()
        with allure.step("Выбрать первую категорию"):
            work.click_category_menu_models(3)
        with allure.step("Выбрать первую подкатегорию"):
            work.click_subcategory(1)
        with allure.step("Добавить мебель в избранное"):
            work.add_in_favorite_from_catalog()
        with allure.step("Проверить появление диалога ограничений"):
            work.check_dialog_constraint_upgrade(block, self.tarif)


@pytest.mark.usefixtures("paste_project_class")
class TestsGuestConstraints(BaseConstraints):
    """Тесты ограничений для Гостя"""

    tarif = "guest"

    @allure.feature("Ограничения Гость")
    @allure.title("Переименование проекта")
    def test_rename_project(self, close_dialog_constraint_for_guest):
        """Переименование проекта

        Args:
            close_dialog_constraint_for_guest: фикстура для закрытия диалога ограничений Гостя

        """
        super().rename_project(block=True)  # Переименование

    @allure.feature("Ограничения Гость")
    @allure.title("Поделиться проектом")
    def test_share_project(self, close_dialog_constraint_for_guest):
        """Проверка ограничений для функции "Поделиться проектом"

        Args:
            close_dialog_constraint_for_guest: фикстура для закрытия диалога ограничений Гостя

        """
        super().share_project(block=True)

    @allure.feature("Ограничения Гость")
    @allure.title("Ниши")
    def test_constraint_alcove(self, close_dialog_constraint_for_guest):
        """Проверка ограничений для добавления Ниш

        Args:
            close_dialog_constraint_for_guest: фикстура для закрытия диалога ограничений Гостя

        """
        super().constraint_alcove(block=True)

    @allure.feature("Ограничения Гость")
    @allure.title("Экспорт 3D")
    def test_constraint_save_3d(self, close_dialog_constraint_for_guest):
        """Проверка ограничений для экспорта в 3D

        Args:
            close_dialog_constraint_for_guest: фикстура для закрытия диалога ограничений Гостя

        """
        super().constraint_save_3d(block=True)

    @allure.feature("Ограничения Гость")
    @allure.title("Экспорт PDF")
    def test_constraint_save_to_pdf(self, close_dialog_constraint_for_guest):
        """Проверка ограничений для экспорта в PDF

        Args:
            close_dialog_constraint_for_guest: фикстура для закрытия диалога ограничений Гостя

        """
        super().constraint_save_to_pdf(block=True)

    @allure.feature("Ограничения Гость")
    @allure.title("Сохранить скриншот")
    def test_constraint_save_screen(self, close_dialog_constraint_for_guest):
        """Проверка ограничений для сохранения скриншота

        Args:
            close_dialog_constraint_for_guest: фикстура для закрытия диалога ограничений Гостя

        """
        work = WorkPage(self.driver_class)
        with allure.step("Сохранить скриншот"):
            work.click_save_screen()
            work.switch_to_tab(1)
            work.check_dialog_constraint_upgrade(block=True, tarif=self.tarif)

    @allure.feature("Ограничения Гость")
    @allure.title("Проемы")
    def test_constraint_apperture(self, close_dialog_constraint_for_guest):
        """Проверка ограничений для добавления Проемов

        Args:
            close_dialog_constraint_for_guest: фикстура для закрытия диалога ограничений Гостя

        """
        super().constraint_apperture(block=True)

    @allure.feature("Ограничения Гость")
    @allure.title("Прогулка")
    def test_constraint_walk(self, close_dialog_constraint_for_guest):
        """Проверка ограничений для режима прогулки

        Args:
            close_dialog_constraint_for_guest: фикстура для закрытия диалога ограничений Гостя

        """
        super().constraint_walk(block=True)

    @allure.feature("Ограничения Гость")
    @allure.title("Изменение высоты мебели")
    def test_constraint_change_hight(self, close_dialog_constraint_for_guest):
        """Проверка ограничений для изменения высоты мебели

        Args:
            close_dialog_constraint_for_guest: фикстура для закрытия диалога ограничений Гостя

        """
        super().constraint_change_hight(block=True)

    @allure.feature("Ограничения Гость")
    @allure.title("Изменение текстуры мебели")
    def test_constraint_change_texture(
        self, close_dialog_constraint_for_guest
    ):
        """Проверка ограничений для изменения текстуры мебели

        Args:
            close_dialog_constraint_for_guest: фикстура для закрытия диалога ограничений Гостя

        """
        super().constraint_change_texture(block=True)

    @allure.feature("Ограничения Гость")
    @allure.title("Изменение подконника")
    @pytest.mark.parametrize(
        "id_trackbar", ["sill-height", "sill-radius", "shift_hor", "shift_ver"]
    )
    def test_constraint_change_windowsill(
        self, id_trackbar, close_dialog_constraint_for_guest
    ):
        """Проверка ограничений для изменения подконника

        Args:
            id_trackbar: ID трекбара свойств подоконника
            close_dialog_constraint_for_guest: фикстура для закрытия диалога ограничений Гостя

        """
        super().constraint_change_windowsill(id_trackbar, block=True)

    @allure.feature("Ограничения Гость")
    @allure.title("Настройки колонны, поворот на 90")
    @pytest.mark.parametrize("direction", ["left", "right"])
    def test_constraint_change_column(
        self, direction, close_dialog_constraint_for_guest
    ):
        """Проверка ограничений для настройки колонны, поворот на 90

        Args:
            close_dialog_constraint_for_guest: фикстура для закрытия диалога ограничений Гостя

        """
        super().constraint_turn_column(block=True, direction=direction)

    @allure.feature("Ограничения Гость")
    @allure.title("Анимация двери")
    @pytest.mark.parametrize(
        "id_animation", ["mirror-width", "mirror-depth", "open-inside"]
    )
    def test_constraint_animation_door(
        self, id_animation, close_dialog_constraint_for_guest
    ):
        """Проверка ограничений для анимации дверей

        Args:
            id_animation: идентификатор анимации
            close_dialog_constraint_for_guest: фикстура для закрытия диалога ограничений Гостя

        """
        super().constraint_animation_door(id_animation, block=True)

    @allure.feature("Ограничения Гость")
    @allure.title("Добавление в избранное")
    def test_add_to_favorites(self, close_dialog_constraint_for_guest):
        """Проверка ограничений для добавления в избранное

        Args:
            close_dialog_constraint_for_guest: фикстура для закрытия диалога ограничений Гостя

        """
        super().constraint_favorites(block=True)


@allure.title("Проверка ограничений функционала на Бесплатном")
@pytest.mark.usefixtures(
    "auth_base_class", "drop_all_project_class", "paste_project_class"
)
class TestsFreeConstraints(BaseConstraints):
    """Проверка ограничений функционала на Бесплатном тарифе"""

    tarif = "free"

    @allure.feature("Ограничения Бесплатный тариф")
    @allure.title("Переименование проекта")
    def test_rename_project(self):
        """Проверка ограничения переименования проекта"""
        super().rename_project(block=False)

    @allure.feature("Ограничения Бесплатный тариф")
    @allure.title("Поделиться проектом")
    def test_share_project(self):
        """Проверка ограничения поделиться проектом"""
        super().share_project(block=False)

    @allure.feature("Ограничения Бесплатный тариф")
    @allure.title("Ниши")
    def test_constraint_alcove(self, close_dialog_upgrade):
        """Проверка ограничений для добавления Ниши

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_alcove(block=True)

    @allure.feature("Ограничения Бесплатный тариф")
    @allure.title("Экспорт 3D")
    def test_constraint_save_3d(self, close_dialog_upgrade):
        """Проверка ограничений для экспорта в 3D

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_save_3d(block=True)

    @allure.feature("Ограничения Бесплатный тариф")
    @allure.title("Экспорт PDF")
    def test_constraint_save_to_pdf(self, close_dialog_upgrade):
        """Проверка ограничений для экспорта в PDF

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_save_to_pdf(block=True)

    @allure.feature("Ограничения Бесплатный тариф")
    @allure.title("Проемы")
    def test_constraint_apperture(self, close_dialog_upgrade):
        """Проверка ограничений для добавления Проемов

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_apperture(block=True)

    @allure.feature("Ограничения Бесплатный тариф")
    @allure.title("Прогулка")
    def test_constraint_walk(self, close_dialog_upgrade_walk):
        """Проверка ограничений для перехода в режим прогулки

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_walk(block=True)

    @allure.feature("Ограничения Бесплатный тариф")
    @allure.title("Изменение высоты мебели")
    def test_constraint_change_hight(self, close_dialog_upgrade):
        """Проверка ограничений для изменения высоты мебели

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_change_hight(block=True)

    @allure.feature("Ограничения Бесплатный тариф")
    @allure.title("Изменение текстуры мебели")
    def test_constraint_change_texture(self, close_dialog_upgrade):
        """Проверка ограничений для изменения текстуры мебели

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_change_texture(block=True)

    @allure.feature("Ограничения Бесплатный тариф")
    @allure.title("Изменение подконника")
    @pytest.mark.parametrize(
        "id_trackbar", ["sill-height", "sill-radius", "shift_hor", "shift_ver"]
    )
    def test_constraint_change_windowsill(
        self, id_trackbar, close_dialog_upgrade
    ):
        """Проверка ограничений для изменения подконника

        Args:
            id_trackbar: id трекбара свойств подоконника
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_change_windowsill(id_trackbar, block=True)

    @allure.feature("Ограничения Бесплатный тариф")
    @allure.title("Настройки колонны, поворот на 90")
    @pytest.mark.parametrize("direction", ["left", "right"])
    def test_constraint_change_column(self, direction, close_dialog_upgrade):
        """Проверка ограничений для изменения колонны

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_turn_column(block=True, direction=direction)

    @allure.feature("Ограничения Бесплатный тариф")
    @allure.title("Анимация двери")
    @pytest.mark.parametrize(
        "id_animation", ["mirror-width", "mirror-depth", "open-inside"]
    )
    def test_constraint_animation_door(
        self, id_animation: str, close_dialog_upgrade
    ):
        """Проверка ограничений для анимации дверей

        Args:
            id_animation: идентификатор анимации
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_animation_door(id_animation)


@pytest.mark.usefixtures(
    "auth_standart_class", "drop_all_project_class", "paste_project_class"
)
class TestsStandartConstraints(BaseConstraints):
    tarif = "standart"

    @allure.feature("Ограничения Стандартный тариф")
    @allure.title("Переименование проекта")
    def test_rename_project(self):
        """Проверка ограничений для переименования проекта"""
        super().rename_project(block=False)

    @allure.feature("Ограничения Стандартный тариф")
    @allure.title("Поделиться проектом")
    def test_share_project(self):
        """Проверка ограничений для функции 'Поделиться проектом'"""
        super().share_project(block=False)

    @allure.feature("Ограничения Стандартный тариф")
    @allure.title("Ниши")
    def test_constraint_alcove(self, close_dialog_upgrade):
        """Проверка ограничений для добавления Ниши

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_alcove(block=True)

    @allure.feature("Ограничения Стандартный тариф")
    @allure.title("Экспорт 3D")
    def test_constraint_save_3d(self, close_dialog_upgrade):
        """Проверка ограничений для экспорта в 3D

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_save_3d(block=True)

    @allure.feature("Ограничения Стандартный тариф")
    @allure.title("Экспорт PDF")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_save_to_pdf(self, close_dialog_upgrade):
        """Проверка ограничений для экспорта в PDF

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_save_to_pdf(block=False)

    @allure.feature("Ограничения Стандартный тариф")
    @allure.title("Проемы")
    def test_constraint_apperture(self, close_dialog_upgrade):
        """Проверка ограничений для добавления Проемов

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_apperture(block=True)

    @allure.feature("Ограничения Стандартный тариф")
    @allure.title("Прогулка")
    def test_constraint_walk(self, close_dialog_upgrade):
        """Проверка ограничений для перехода в режим прогулки

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_walk(block=True)

    @allure.feature("Ограничения Стандартный тариф")
    @allure.title("Изменение высоты мебели")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_hight(self, close_dialog_upgrade):
        """Проверка ограничений для изменения высоты мебели

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_change_hight(block=False)

    @allure.feature("Ограничения Стандартный тариф")
    @allure.title("Изменение текстуры мебели")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_texture(self, close_dialog_upgrade):
        """Проверка ограничений для изменения текстуры мебели

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_change_texture(block=False)

    @allure.feature("Ограничения Стандартный тариф")
    @allure.title("Изменение подконника")
    @pytest.mark.parametrize(
        "id_trackbar", ["sill-height", "sill-radius", "shift_hor", "shift_ver"]
    )
    def test_constraint_change_windowsill(
        self, id_trackbar, close_dialog_upgrade
    ):
        """Проверка ограничений для изменения подконника

        Args:
            id_trackbar: id трекбара свойств подоконника
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_change_windowsill(id_trackbar, block=True)

    @allure.feature("Ограничения Стандартный тариф")
    @allure.title("Настройки колонны, поворот на 90")
    @pytest.mark.parametrize(
        "direction, close_dialog_upgrade",
        [("left", False), ("right", False)],
        indirect=["close_dialog_upgrade"],
    )
    def test_constraint_change_column(self, direction, close_dialog_upgrade):
        """Проверка ограничений для изменения колонны

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_turn_column(block=False, direction=direction)

    @allure.feature("Ограничения Стандартный тариф")
    @allure.title("Анимация двери")
    @pytest.mark.parametrize(
        "id_animation", ["mirror-width", "mirror-depth", "open-inside"]
    )
    def test_constraint_animation_door(
        self, id_animation, close_dialog_upgrade
    ):
        """Проверка ограничений для анимации дверей

        Args:
            id_animation: идентификатор анимации
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_animation_door(id_animation)


@pytest.mark.usefixtures(
    "auth_premium_class", "drop_all_project_class", "paste_project_class"
)
class TestsPremiumConstraints(BaseConstraints):
    """Тесты ограничений Премиум тарифа."""

    tarif = "premium"

    @allure.feature("Ограничения Премиум тариф")
    @allure.title("Переименование проекта")
    def test_rename_project(self):
        """Проверка ограничений для переименования проекта"""
        super().rename_project(block=False)

    @allure.feature("Ограничения Премиум тариф")
    @allure.title("Поделиться проектом")
    def test_share_project(self):
        """Проверка ограничений для функции 'Поделиться проектом'"""
        super().share_project(block=False)

    @allure.feature("Ограничения Премиум тариф")
    @allure.title("Ниши")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_alcove(self, close_dialog_upgrade):
        """Проверка ограничений для добавения Ниши

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_alcove(block=False)

    @allure.feature("Ограничения Премиум тариф")
    @allure.title("Экспорт 3D")
    def test_constraint_save_3d(self, close_dialog_upgrade):
        """Проверка ограничений для экспорта в 3D

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_save_3d(block=True)

    @allure.feature("Ограничения Премиум тариф")
    @allure.title("Экспорт PDF")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_save_to_pdf(self, close_dialog_upgrade):
        """Проверка ограничений для экспорта в PDF

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_save_to_pdf(block=False)

    @allure.feature("Ограничения Премиум тариф")
    @allure.title("Проемы")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_apperture(self, close_dialog_upgrade):
        """Проверка ограничений для добавлеия проемов

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_apperture(block=False)

    @allure.feature("Ограничения Премиум тариф")
    @allure.title("Прогулка")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_walk(self, close_dialog_upgrade):
        """Проверка ограничений для функции 'Прогулка'

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_walk(block=False)

    @allure.feature("Ограничения Премиум тариф")
    @allure.title("Изменение высоты мебели")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_hight(self, close_dialog_upgrade):
        """Проверка ограничений для изменения высоты мебели

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_change_hight(block=False)

    @allure.feature("Ограничения Премиум тариф")
    @allure.title("Изменение текстуры мебели")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_texture(self, close_dialog_upgrade):
        """Проверка ограничений для изменения текстуры мебели

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_change_texture(block=False)

    @allure.feature("Ограничения Премиум тариф")
    @allure.title("Изменение подконника")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    @pytest.mark.parametrize(
        "id_trackbar", ["sill-height", "sill-radius", "shift_hor", "shift_ver"]
    )
    def test_constraint_change_windowsill(
        self, id_trackbar, close_dialog_upgrade
    ):
        """Проверка ограничений для изменения подконника

        Args:
            id_trackbar: id трекбара свойств подоконника
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_change_windowsill(id_trackbar, block=False)

    @allure.feature("Ограничения Премиум тариф")
    @allure.title("Настройки колонны, поворот на 90")
    @pytest.mark.parametrize(
        "direction, close_dialog_upgrade",
        [("left", False), ("right", False)],
        indirect=["close_dialog_upgrade"],
    )
    def test_constraint_change_column(self, direction, close_dialog_upgrade):
        """Проверка ограничений для изменения колонны

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_turn_column(block=False, direction=direction)

    @allure.feature("Ограничения Премиум тариф")
    @allure.title("Анимация двери")
    @pytest.mark.parametrize(
        "id_animation", ["mirror-width", "mirror-depth", "open-inside"]
    )
    def test_constraint_animation_door(
        self, id_animation, close_dialog_upgrade
    ):
        """Проверка ограничений для анимации дверей

        Args:
            id_animation: id трекбара свойств анимации дверей
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_animation_door(id_animation)


@pytest.mark.usefixtures(
    "auth_profi_class", "drop_all_project_class", "paste_project_class"
)
class TestsProfiConstraints(BaseConstraints):
    """Класс тестов для ограничений Профи тарифа"""

    tarif = "profi"

    @allure.feature("Ограничения Профи тариф")
    @allure.title("Переименование проекта")
    def test_rename_project(self):
        """Проверка ограничений для переименования проекта"""
        super().rename_project(block=False)

    @allure.feature("Ограничения Профи тариф")
    @allure.title("Поделиться проектом")
    def test_share_project(self):
        """Проверка ограничений для функции 'Поделиться проектом'"""
        super().share_project(block=False)

    @allure.feature("Ограничения Профи тариф")
    @allure.title("Ниши")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_alcove(self, close_dialog_upgrade):
        """Проверка ограничений для добавления Ниши

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_alcove(block=False)

    @allure.feature("Ограничения Профи тариф")
    @allure.title("Экспорт 3D")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_save_3d(self, close_dialog_upgrade):
        """Проверка ограничений для экспорта в 3D

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_save_3d(block=False)

    @allure.feature("Ограничения Профи тариф")
    @allure.title("Экспорт PDF")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_save_to_pdf(self, close_dialog_upgrade):
        """Проверка ограничений для экспорта в PDF

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_save_to_pdf(block=False)

    @allure.feature("Ограничения Профи тариф")
    @allure.title("Проемы")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_apperture(self, close_dialog_upgrade):
        """Проверка ограничений для добавлеия проема

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_apperture(block=False)

    @allure.feature("Ограничения Профи тариф")
    @allure.title("Прогулка")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_walk(self, close_dialog_upgrade):
        """Проверка ограничений для режима прогулки

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_walk(block=False)

    @allure.feature("Ограничения Профи тариф")
    @allure.title("Изменение высоты мебели")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_hight(self, close_dialog_upgrade):
        """Проверка ограничений для изменения высоты мебели

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_change_hight(block=False)

    @allure.feature("Ограничения Профи тариф")
    @allure.title("Изменение текстуры мебели")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_texture(self, close_dialog_upgrade):
        """Проверка ограничений для изменения текстуры мебели

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_change_texture(block=False)

    @allure.feature("Ограничения Профи тариф")
    @allure.title("Изменение подконника")
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    @pytest.mark.parametrize(
        "id_trackbar", ["sill-height", "sill-radius", "shift_hor", "shift_ver"]
    )
    def test_constraint_change_windowsill(
        self, id_trackbar, close_dialog_upgrade
    ):
        """Проверка ограничений для изменения подконника

        Args:
            id_trackbar: id трекбара свойств подоконника
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_change_windowsill(id_trackbar, block=False)

    @allure.feature("Ограничения Профи тариф")
    @allure.title("Настройки колонны, поворот на 90")
    @pytest.mark.parametrize(
        "direction, close_dialog_upgrade",
        [("left", False), ("right", False)],
        indirect=["close_dialog_upgrade"],
    )
    def test_constraint_change_column(self, direction, close_dialog_upgrade):
        """Проверка ограничений для изменения колонны

        Args:
            close_dialog_upgrade: фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_turn_column(block=False, direction=direction)

    @allure.feature("Ограничения Профи тариф")
    @allure.title("Анимация двери")
    @pytest.mark.parametrize(
        "id_animation", ["mirror-width", "mirror-depth", "open-inside"]
    )
    def test_constraint_animation_door(
        self, id_animation: str, close_dialog_upgrade
    ):
        """Проверка ограничений для анимации дверей

        Args:
            id_animation (str): ID анимации двери
            close_dialog_upgrade: Фикстура для закрытия диалога ограничений платного тарифа

        """
        super().constraint_animation_door(id_animation)
