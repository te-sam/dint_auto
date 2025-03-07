from time import sleep

import allure
import pytest

from pages.dashboard_page import DashboardPage
from pages.work_page import WorkPage
from config import settings

@allure.title('Проверка ограничений функционала у Гостя')
@pytest.mark.usefixtures("driver_class")


class BaseConstraints:
    @allure.title('Поделиться проектом проектом')
    def rename_project(self, block=False, tarif="paid"):  # Переименовать проект
        name_project = "test"
        work = WorkPage(self.driver_class)
        dash = DashboardPage(self.driver_class)

        with allure.step('Открыть главную страницу'):
            work.open_main()
            sleep(2)

        with allure.step('Переименовать проект'):
            work.rename_project(name_project)
            if tarif == "guest":
                with allure.step('Проверка диалога ограничений'):
                    work.check_dialog_constraint(block, tarif)
            else:  # Иначе проверяем, что проект переименовался
                sleep(2)

                with allure.step('Открыть дашборд'):
                    work.open_dashboard()

                with allure.step('Проверить переименовался ли проект'):
                    if not block:
                        assert dash.is_project_named(name_project), 'Проект не переименовался'
    

    @allure.title('Поделиться проектом')
    def share_project(self, block=False, tarif="paid"):  # Поделиться проектом
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
                # work.driver.refresh()
            if tarif == "guest":
                work.check_dialog_constraint(block, tarif)


    @allure.title('Ниши ограничение')
    def constraint_alcove(self, block=False, tarif="paid"):  # Ниши
        work = WorkPage(self.driver_class)

        with allure.step('Открыть главную страницу'):
            work.open_main()
            sleep(2)

        with allure.step('Кликнуть "Ниши"'):
            work.click_alcove()

        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block, tarif)


    allure.title('Сохранить в 3D ограничние')
    def constraint_save_3d(self, block=False, tarif="paid"):  # Сохранение в 3D
        work = WorkPage(self.driver_class)

        with allure.step('Кликнуть "3D экспорт"'):
            work.click_save_3d()

        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block, tarif)


    def constraint_save_to_pdf(self, block=False, tarif="paid"):  # Сохранение в PDF
        work = WorkPage(self.driver_class)

        with allure.step('Кликнуть "Экспорт в PDF"'):
            work.click_save_to_pdf()

        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block, tarif)


    def constraint_apperture(self, block=False, tarif="paid"):  # Проемы
        work = WorkPage(self.driver_class)

        with allure.step('Кликнуть "Проемы"'):
            work.click_apperture()

        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block, tarif)

    
    def constraint_walk(self, block=False, tarif="paid"):  # Прогулка
        work = WorkPage(self.driver_class)

        with allure.step('Кликнуть "Прогулка"'):
            work.click_walk()

        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block, tarif)

    
    def constraint_change_hight(self, block=False, tarif="paid"):  # Изменение высоты мебели
        work = WorkPage(self.driver_class)

        with allure.step('Перейти в 3D'):
            work.click_3d()
        
        with allure.step('Кликнуть по дивану'):
            work.first_click_by_canvas('3d',168, 23)

        with allure.step('Изменить высоту объекта'):
            work.change_height(10)

        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block, tarif)

    
    def constraint_change_texture(self, block=False, tarif="paid"): # Изменение текстуры мебели
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
            work.check_dialog_constraint(block, tarif)

    
    def constraint_change_windowsill(self, id_trackbar, block=False, tarif="paid"):  # Изменение подконника
        work = WorkPage(self.driver_class)
        with allure.step('Кликнуть по окну'):
            work.first_click_by_canvas('3d',140, -158.5)
        
        with allure.step('Развернуть настройки подоконника'):
            work.expand_settings_windowsill()
        
        with allure.step('Изменить высоту подоконника'):
            work.change_windowsill(id_trackbar)
        
        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block=block, tarif=tarif)


    def constraint_change_column(self, block=False, tarif="paid"):  # Настройки колонны, поворот на 90
        work = WorkPage(self.driver_class)
        with allure.step('Кликнуть по колонне'):
            # X = -14, Y = -96.5
            work.first_click_by_canvas('3d', -14, -96.5)
        
        with allure.step('Повернуть колонную на 90 влево'):
            work.turn_column_90_left()


        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block, tarif)

    
    def constraint_animation_door(self, id_animation, block=False, tarif="paid"):
        work = WorkPage(self.driver_class)
        with allure.step('Кликнуть по двери'):
            # X = -145, Y = -177.5
            work.first_click_by_canvas('3d',  -145, -177.5)
        with allure.step(f'Изменить анимацию {id_animation}'):
            work.click_animation_door(id_animation)
        with allure.step('Проверить появление диалога ограничений'):
            work.check_dialog_constraint(block, tarif)
            



@pytest.mark.usefixtures("paste_project_for_guest")
class TestsGuestConstraints(BaseConstraints):
    @allure.feature('Ограничения Гость')
    @allure.title('Переименование проекта')
    def test_rename_project(self, close_dialog_constraint_for_guest):
        super().rename_project(block=True, tarif="guest")  # Переименование

    @allure.feature('Ограничения Гость')
    @allure.title('Поделиться проектом')
    def test_share_project(self, close_dialog_constraint_for_guest):  # Поделиться проектом
        super().share_project(block=True, tarif="guest")
    
    @allure.feature('Ограничения Гость')
    @allure.title('Ниши')
    def test_constraint_alcove(self, close_dialog_constraint_for_guest):  # Ниши
        super().constraint_alcove(block=True, tarif="guest")

    @allure.feature('Ограничения Гость')
    @allure.title('Экспорт 3D')
    def test_constraint_save_3d(self, close_dialog_constraint_for_guest):  # Сохранение в 3D
        super().constraint_save_3d(block=True, tarif="guest")

    @allure.feature('Ограничения Гость')
    @allure.title('Экспорт PDF')
    def test_constraint_save_to_pdf(self, close_dialog_constraint_for_guest):  # Сохранение в PDF
        super().constraint_save_to_pdf(block=True, tarif="guest")

    @allure.feature('Ограничения Гость')
    @allure.title('Сохранить скриншот')
    def test_constraint_save_screen(self, close_dialog_constraint_for_guest):
        work = WorkPage(self.driver_class)
        with allure.step('Сохранить скриншот'):
            work.click_save_screen()
            work.switch_to_tab(1)
            work.check_dialog_constraint(block=True, tarif="guest")

    @allure.feature('Ограничения Гость')
    @allure.title('Проемы')
    def test_constraint_apperture(self, close_dialog_constraint_for_guest):  # Проемы
        super().constraint_apperture(block=True, tarif="guest")

    @allure.feature('Ограничения Гость')
    @allure.title('Прогулка')
    def test_constraint_walk(self, close_dialog_constraint_for_guest): # Прогулка
        super().constraint_walk(block=True, tarif="guest")

    @allure.feature('Ограничения Гость')
    @allure.title('Изменение высоты мебели')
    def test_constraint_change_hight(self, close_dialog_constraint_for_guest):  # Изменение высоты мебели
        super().constraint_change_hight(block=True, tarif="guest")

    @allure.feature('Ограничения Гость')
    @allure.title('Изменение текстуры мебели')
    def test_constraint_change_texture(self, close_dialog_constraint_for_guest):  # Изменение текстуры мебели
        super().constraint_change_texture(block=True, tarif="guest")

    @allure.feature('Ограничения Гость')
    @allure.title('Изменение подконника')
    @pytest.mark.parametrize("id_trackbar", ["sill-height", "sill-radius", "shift_hor", "shift_ver"])
    def test_constraint_change_windowsill(self, id_trackbar, close_dialog_constraint_for_guest):  # Изменение подконника
        super().constraint_change_windowsill(id_trackbar, block=True, tarif="guest")

    @allure.feature('Ограничения Гость')
    @allure.title('Настройки колонны, поворот на 90')
    def test_constraint_change_column(self, close_dialog_constraint_for_guest):  # Настройки колонны, поворот на 90
        super().constraint_change_column(block=True, tarif="guest")
    
    @allure.feature('Ограничения Гость')
    @allure.title('Анимация двери')
    @pytest.mark.parametrize("id_animation", ["mirror-width", "mirror-depth", "open-inside"])
    def test_constraint_animation_door(self, id_animation, close_dialog_constraint_for_guest):  # Настройки колонны, поворот на 90
        super().constraint_animation_door(id_animation, block=True, tarif="guest")


@allure.title('Проверка ограничений функционала на Бесплатном')
@pytest.mark.usefixtures("auth_base",  "drop_all_project", "paste_project")
class TestsFreeConstraints(BaseConstraints):
    @allure.feature('Ограничения Бесплатный тариф')
    @allure.title('Переименование проекта')
    def test_rename_project(self):
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
    @pytest.mark.parametrize("id_trackbar", ["sill-height", "sill-radius", "shift_hor", "shift_ver"])
    def test_constraint_change_windowsill(self, id_trackbar, close_dialog_upgrade):  # Изменение подконника
        super().constraint_change_windowsill(id_trackbar, block=True)

    @allure.feature('Ограничения Бесплатный тариф')
    @allure.title('Настройки колонны, поворот на 90')
    def test_constraint_change_column(self, close_dialog_upgrade):  # Настройки колонны, поворот на 90
        super().constraint_change_column(block=True)  
    
    @allure.feature('Ограничения Бесплатный тариф')
    @allure.title('Анимация двери')
    @pytest.mark.parametrize("id_animation", ["mirror-width", "mirror-depth", "open-inside"])
    def test_constraint_animation_door(self, id_animation, close_dialog_upgrade):  # Анимация дверей
        super().constraint_animation_door(id_animation)
        

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
    @pytest.mark.parametrize("id_trackbar", ["sill-height", "sill-radius", "shift_hor", "shift_ver"])
    def test_constraint_change_windowsill(self, id_trackbar, close_dialog_upgrade):  # Изменение подконника
        super().constraint_change_windowsill(id_trackbar, block=True)

    @allure.feature('Ограничения Стандартный тариф')
    @allure.title('Настройки колонны, поворот на 90')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_column(self, close_dialog_upgrade):  # Настройки колонны, поворот на 90
        super().constraint_change_column(block=False)

    @allure.feature('Ограничения Стандартный тариф')
    @allure.title('Анимация двери')
    @pytest.mark.parametrize("id_animation", ["mirror-width", "mirror-depth", "open-inside"])
    def test_constraint_animation_door(self, id_animation, close_dialog_upgrade):  # Анимация дверей
        super().constraint_animation_door(id_animation)


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
    @pytest.mark.parametrize("id_trackbar", ["sill-height", "sill-radius", "shift_hor", "shift_ver"])
    def test_constraint_change_windowsill(self, id_trackbar, close_dialog_upgrade):  # Изменение подконника
        super().constraint_change_windowsill(id_trackbar, block=False)
        
    @allure.feature('Ограничения Премиум тариф')
    @allure.title('Настройки колонны, поворот на 90')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_column(self, close_dialog_upgrade):  # Настройки колонны, поворот на 90
        super().constraint_change_column(block=False)

    @allure.feature('Ограничения Премиум тариф')
    @allure.title('Анимация двери')
    @pytest.mark.parametrize("id_animation", ["mirror-width", "mirror-depth", "open-inside"])
    def test_constraint_animation_door(self, id_animation, close_dialog_upgrade):  # Анимация дверей
        super().constraint_animation_door(id_animation)

@pytest.mark.usefixtures("auth_profi",  "drop_all_project", "paste_project")
class TestsProfiConstraints(BaseConstraints):
    @allure.feature('Ограничения Профи тариф')
    @allure.title('Переименование проекта')
    def test_rename_project(self):
        super().rename_project(block=False)  # Переименование

    @allure.feature('Ограничения Профи тариф')
    @allure.title('Поделиться проектом')
    def test_share_project(self):  # Поделиться проектом
        super().share_project(block=False)

    @allure.feature('Ограничения Профи тариф')
    @allure.title('Ниши')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_alcove(self, close_dialog_upgrade):  # Ниши
        super().constraint_alcove(block=False)

    @allure.feature('Ограничения Профи тариф')
    @allure.title('Экспорт 3D')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_save_3d(self, close_dialog_upgrade):  # Сохранение в 3D
        super().constraint_save_3d(block=False)

    @allure.feature('Ограничения Профи тариф')
    @allure.title('Экспорт PDF')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_save_to_pdf(self, close_dialog_upgrade):  # Сохранение в PDF
        super().constraint_save_to_pdf(block=False)

    @allure.feature('Ограничения Профи тариф')
    @allure.title('Проемы')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_apperture(self, close_dialog_upgrade):  # Проемы
        super().constraint_apperture(block=False)

    @allure.feature('Ограничения Профи тариф')
    @allure.title('Прогулка')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_walk(self, close_dialog_upgrade): # Прогулка
        super().constraint_walk(block=False)

    @allure.feature('Ограничения Профи тариф')
    @allure.title('Изменение высоты мебели')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_hight(self, close_dialog_upgrade):  # Изменение высоты мебели
        super().constraint_change_hight(block=False)

    @allure.feature('Ограничения Профи тариф')
    @allure.title('Изменение текстуры мебели')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_texture(self, close_dialog_upgrade):  # Изменение текстуры мебели
        super().constraint_change_texture(block=False)

    @allure.feature('Ограничения Профи тариф')
    @allure.title('Изменение подконника')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    @pytest.mark.parametrize("id_trackbar", ["sill-height", "sill-radius", "shift_hor", "shift_ver"])
    def test_constraint_change_windowsill(self, id_trackbar, close_dialog_upgrade):  # Изменение подконника
        super().constraint_change_windowsill(id_trackbar, block=False)

    @allure.feature('Ограничения Профи тариф')
    @allure.title('Настройки колонны, поворот на 90')
    @pytest.mark.parametrize("close_dialog_upgrade", [False], indirect=True)
    def test_constraint_change_column(self, close_dialog_upgrade):  # Настройки колонны, поворот на 90
        super().constraint_change_column(block=False)

    @allure.feature('Ограничения Профи тариф')
    @allure.title('Анимация двери')
    @pytest.mark.parametrize("id_animation", ["mirror-width", "mirror-depth", "open-inside"])
    def test_constraint_animation_door(self, id_animation, close_dialog_upgrade):  # Анимация дверей
        super().constraint_animation_door(id_animation)


    

    
    