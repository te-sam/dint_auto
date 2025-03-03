from time import sleep

import allure
import pytest

from config import settings
from pages.dashboard_page import DashboardPage
from pages.work_page import WorkPage, locator_3d


# @allure.title('Проверка ограничений функционала у Гостя')
# @pytest.mark.usefixtures("driver_class")
# class TestsGuestConstraints:
#     def test_constraint_rename(self, close_dialog_constraint_for_guest):
#         work = WorkPage(self.driver_class)  # Используем общий драйвер
#         work.open_main()
#         work.rename_project("new")
#         work.send_enter()
#         with allure.step('Переименовать проект'):
#             work.check_dialog_constraint('guest')

#     def test_constraint_save_screen(self, close_dialog_constraint_for_guest):
#         work = WorkPage(self.driver_class)
#         with allure.step('Сохранить скриншот'):
#             work.click_save_screen()
#             work.switch_to_tab(1)
#             work.check_dialog_constraint('guest')

#     def test_constraint_save_to_pdf(self, close_dialog_constraint_for_guest):
#         work = WorkPage(self.driver_class)
#         with allure.step('Сохранить в PDF'):
#             work.click_save_to_pdf()
#             work.check_dialog_constraint('guest')

#     def test_constraint_save_3d(self, close_dialog_constraint_for_guest):
#         work = WorkPage(self.driver_class)
#         with allure.step('3D экспорт'):
#             work.click_save_3d()
#             work.check_dialog_constraint('guest')

#     def test_constraint_share_project(self, close_dialog_constraint_for_guest):
#         work = WorkPage(self.driver_class)
#         work.click_share()
#         work.check_dialog_constraint('guest')


class BaseConstraints:
    @allure.title('Поделиться проектом проектом')
    def rename_project(self, block=False):  # Переименовать проект
        name_project = "test"
        work = WorkPage(self.driver_class)
        dash = DashboardPage(self.driver_class)

        with allure.step('Открыть главную страницу'):
            work.open_main()
            sleep(2)

        with allure.step('Переименовать проект'):
            work.rename_project(name_project)
            sleep(2)

        with allure.step('Открыть дашборд'):
            work.open_dashboard()

        with allure.step('Проверить переименовался ли проект'):
            if not block:
                assert dash.is_project_named(name_project), 'Проект не переименовался'
    

    @allure.title('Поделиться проектом')
    def share_project(self, block=False):  # Поделиться проектом
        work = WorkPage(self.driver_class)

        with allure.step('Открыть главную страницу'):
            work.open_main()
            sleep(2)

        with allure.step('Кликнуть "Поделиться проеком"'):
            work.click_share()
            sleep(2)

        with allure.step('Проверить появление диалога ограничений'):
            if not block:
                work.check_dialog_share()


    @allure.title('Ниши ограничение')
    def constraint_alcove(self, block=False):  # Ниши
        work = WorkPage(self.driver_class)

        with allure.step('Открыть главную страницу'):
            work.open_main()
            sleep(2)

        with allure.step('Кликнуть "Ниши"'):
            work.click_alcove()

        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block)


    allure.title('Сохранить в 3D ограничние')
    def constraint_save_3d(self, block=False):  # Сохранение в 3D
        work = WorkPage(self.driver_class)

        with allure.step('Кликнуть "3D экспорт"'):
            work.click_save_3d()

        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block)


    def constraint_save_to_pdf(self, block=False):  # Сохранение в PDF
        work = WorkPage(self.driver_class)

        with allure.step('Кликнуть "Экспорт в PDF"'):
            work.click_save_to_pdf()

        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block)


    def constraint_apperture(self, block=False):  # Проемы
        work = WorkPage(self.driver_class)

        with allure.step('Кликнуть "Проемы"'):
            work.click_apperture()

        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block)

    
    def constraint_walk(self, block=False):  # Прогулка
        work = WorkPage(self.driver_class)

        with allure.step('Кликнуть "Прогулка"'):
            work.click_walk()

        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block)

    
    def constraint_change_hight(self, block=False):  # Изменение высоты мебели
        work = WorkPage(self.driver_class)

        with allure.step('Перейти в 3D'):
            work.click_3d()
        
        with allure.step('Кликнуть по дивану'):
            work.first_click_by_canvas('3d',168, 23)

        with allure.step('Изменить высоту объекта'):
            work.change_height(10)

        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block)

    
    def constraint_change_texture(self, block=False): # Изменение текстуры мебели
        work = WorkPage(self.driver_class)
        with allure.step('Перейти в 3D'):
            work.click_3d()
        
        with allure.step('Кликнуть по дивану'):
            work.first_click_by_canvas('3d',168, 23)
        
        with allure.step('Перейти в каталог текстур'):
            work.click_texture_for_furniture(1)
        
        with allure.step('Перейти по активной текстуре'):
            work.click_texture_from_catalog()
        
        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block)

    
    def constraint_change_windowsill(self, block=False):  # Изменение подконника
        work = WorkPage(self.driver_class)
        with allure.step('Кликнуть по окну'):
            work.first_click_by_canvas('3d',140, -158.5)
        
        with allure.step('Развернуть настройки подоконника'):
            work.expand_settings_windowsill()
        
        with allure.step('Изменить высоту подоконника'):
            work.change_hight_windowsill(10)
        
        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block)


    def constraint_change_column(self, block=False):  # Настройки колонны, поворот на 90
        work = WorkPage(self.driver_class)
        with allure.step('Кликнуть по колонне'):
            # X = -1, Y = -97.5
            work.first_click_by_canvas('3d', -1, -97.5)
        
        # sleep(10000)
        with allure.step('Повернуть колонную на 90 влево'):
            work.turn_column_90_left()

        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block)

    
    # def test_animation_door(self):


@allure.title('Проверка ограничений функционала на Бесплатном')
@pytest.mark.usefixtures("auth_base",  "drop_all_project", "paste_project")
class TestsFreeConstraints(BaseConstraints):
    @allure.feature('Ограничения Бесплатный тариф')
    @allure.title('Переименование проекта')
    def test_rename_project(self, ):
        super().rename_project(block=False)  # Переименование

    @allure.feature('Ограничения Бесплатный тариф')
    @allure.title('Поделиться проектом')
    def test_share_project(self):  # Поделиться проектом
        super().share_project(block=False)

    @allure.feature('Ограничения Бесплатный тариф')
    @allure.title('Ниши')
    def test_constraint_alcove(self, close_dialog_upgrade):  # Ниши
        super().constraint_alcove(block=True)

    @allure.feature('Ограничения Бесплатный тариф')
    @allure.title('Экспорт 3D')
    def test_constraint_save_3d(self, close_dialog_upgrade):  # Сохранение в 3D
        super().constraint_save_3d(block=True)

    @allure.feature('Ограничения Бесплатный тариф')
    @allure.title('Экспорт PDF')
    def test_constraint_save_to_pdf(self, close_dialog_upgrade):  # Сохранение в PDF
        super().constraint_save_to_pdf(block=True)

    @allure.feature('Ограничения Бесплатный тариф')
    @allure.title('Проемы')
    def test_constraint_apperture(self, close_dialog_upgrade):  # Проемы
        super().constraint_apperture(block=True)

    @allure.feature('Ограничения Бесплатный тариф')
    @allure.title('Прогулка')
    def test_constraint_walk(self, close_dialog_upgrade): # Прогулка
        super().constraint_walk(block=True)

    @allure.feature('Ограничения Бесплатный тариф')
    @allure.title('Изменение высоты мебели')
    def test_constraint_change_hight(self, close_dialog_upgrade):  # Изменение высоты мебели
        super().constraint_change_hight(block=True)

    @allure.feature('Ограничения Бесплатный тариф')
    @allure.title('Изменение текстуры мебели')
    def test_constraint_change_texture(self, close_dialog_upgrade):  # Изменение текстуры мебели
        super().constraint_change_texture(block=True)

    @allure.feature('Ограничения Бесплатный тариф')
    @allure.title('Изменение подконника')
    def test_constraint_change_windowsill(self, close_dialog_upgrade):  # Изменение подконника
        super().constraint_change_windowsill(block=True)

    @allure.feature('Ограничения Бесплатный тариф')
    @allure.title('Настройки колонны, поворот на 90')
    def test_constraint_change_column(self, close_dialog_upgrade):  # Настройки колонны, поворот на 90
        super().constraint_change_column(block=True)  
        

@pytest.mark.usefixtures("auth_standart",  "drop_all_project", "paste_project")
class TestsStandartConstraints(BaseConstraints):
    @allure.feature('Ограничения Стандартный тариф')
    @allure.title('Переименование проекта')
    def test_rename_project(self):
        super().rename_project(block=False)  # Переименование

    @allure.feature('Ограничения Стандартный тариф')
    @allure.title('Поделиться проектом')
    def test_share_project(self):  # Поделиться проектом
        super().share_project(block=False)

    @allure.feature('Ограничения Стандартный тариф')
    @allure.title('Ниши')
    def test_constraint_alcove(self, close_dialog_upgrade):  # Ниши
        super().constraint_alcove(block=True)

    @allure.feature('Ограничения Стандартный тариф')
    @allure.title('Экспорт 3D')
    def test_constraint_save_3d(self, close_dialog_upgrade):  # Сохранение в 3D
        super().constraint_save_3d(block=True)

    @allure.feature('Ограничения Стандартный тариф')
    @allure.title('Экспорт PDF')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_save_to_pdf(self, close_dialog_upgrade):  # Сохранение в PDF
        super().constraint_save_to_pdf(block=False)

    @allure.feature('Ограничения Стандартный тариф')
    @allure.title('Проемы')
    def test_constraint_apperture(self, close_dialog_upgrade):  # Проемы
        super().constraint_apperture(block=True)

    @allure.feature('Ограничения Стандартный тариф')
    @allure.title('Прогулка')
    def test_constraint_walk(self, close_dialog_upgrade): # Прогулка
        super().constraint_walk(block=True)

    @allure.feature('Ограничения Стандартный тариф')
    @allure.title('Изменение высоты мебели')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_hight(self, close_dialog_upgrade):  # Изменение высоты мебели
        super().constraint_change_hight(block=False)

    @allure.feature('Ограничения Стандартный тариф')
    @allure.title('Изменение текстуры мебели')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_texture(self, close_dialog_upgrade):  # Изменение текстуры мебели
        super().constraint_change_texture(block=False)

    @allure.feature('Ограничения Стандартный тариф')
    @allure.title('Изменение подконника')
    def test_constraint_change_windowsill(self, close_dialog_upgrade):  # Изменение подконника
        super().constraint_change_windowsill(block=True)

    @allure.feature('Ограничения Стандартный тариф')
    @allure.title('Настройки колонны, поворот на 90')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_column(self, close_dialog_upgrade):  # Настройки колонны, поворот на 90
        super().constraint_change_column(block=False)


@pytest.mark.usefixtures("auth_premium",  "drop_all_project", "paste_project")
class TestsPremiumConstraints(BaseConstraints):
    @allure.feature('Ограничения Премиум тариф')
    @allure.title('Переименование проекта')
    def test_rename_project(self):
        super().rename_project(block=False)  # Переименование

    @allure.feature('Ограничения Премиум тариф')
    @allure.title('Поделиться проектом')
    def test_share_project(self):  # Поделиться проектом
        super().share_project(block=False)

    @allure.feature('Ограничения Премиум тариф')
    @allure.title('Ниши')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_alcove(self, close_dialog_upgrade):  # Ниши
        super().constraint_alcove(block=False)

    @allure.feature('Ограничения Премиум тариф')
    @allure.title('Экспорт 3D')
    def test_constraint_save_3d(self, close_dialog_upgrade):  # Сохранение в 3D
        super().constraint_save_3d(block=True)

    @allure.feature('Ограничения Премиум тариф')
    @allure.title('Экспорт PDF')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_save_to_pdf(self, close_dialog_upgrade):  # Сохранение в PDF
        super().constraint_save_to_pdf(block=False)

    @allure.feature('Ограничения Премиум тариф')
    @allure.title('Проемы')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_apperture(self, close_dialog_upgrade):  # Проемы
        super().constraint_apperture(block=False)

    @allure.feature('Ограничения Премиум тариф')
    @allure.title('Прогулка')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_walk(self, close_dialog_upgrade): # Прогулка
        super().constraint_walk(block=False)

    @allure.feature('Ограничения Премиум тариф')
    @allure.title('Изменение высоты мебели')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_hight(self, close_dialog_upgrade):  # Изменение высоты мебели
        super().constraint_change_hight(block=False)

    @allure.feature('Ограничения Премиум тариф')
    @allure.title('Изменение текстуры мебели')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_texture(self, close_dialog_upgrade):  # Изменение текстуры мебели
        super().constraint_change_texture(block=False)

    @allure.feature('Ограничения Премиум тариф')
    @allure.title('Изменение подконника')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_windowsill(self, close_dialog_upgrade):  # Изменение подконника
        super().constraint_change_windowsill(block=False)

    @allure.feature('Ограничения Премиум тариф')
    @allure.title('Настройки колонны, поворот на 90')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_column(self, close_dialog_upgrade):  # Настройки колонны, поворот на 90
        super().constraint_change_column(block=False)




    

    
    