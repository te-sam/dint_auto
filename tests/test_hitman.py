from time import sleep as wait

import allure
import pytest

from pages.dashboard_page import DashboardPage
from pages.work_page import WorkPage
from config import settings


@pytest.mark.usefixtures("driver_class")

class HitmanModelsPage:
    def check_down_block_in_category(self, is_authorized = False):
        work = WorkPage(self.driver_class)
        work.open_main()

        wait(2)

        work.click_button_video_close(is_authorized)

        work.click_button_models()
        work.click_category_menu_models(4)

        with allure.step("Проверка появления плашки в каталоге"):
            assert work.check_stimulate_panel() == True

    def сheck_work_down_block_in_category(self, tarif = 'paid'):
        work = WorkPage(self.driver_class)

        work.click_subcategory(2)

        with allure.step("Проверка появления плашки в подкаталоге"):
            work.click_stimulate_panel_order_button(tarif)

    def check_true_link_block_in_category(self):
        work = WorkPage(self.driver_class)

        with allure.step("Проверка ссылки на страницу"):
            work.true_url("https://online-dint.ulapr.ru/order.php")


@pytest.mark.usefixtures("driver_class")

class HitmanBasesPage:
    def check_door_internals(self, is_authorized = False):
        work = WorkPage(self.driver_class)
        work.open_main()

        wait(2)

        work.click_button_video_close(is_authorized)

        work.click_category_build_selector(4, 1)
        work.click_subcategory_build_selector(1)
        work.click_by_canvas(400, 400)
        wait(1)
        # work.click_subcategory_build_selector(1)

        with allure.step("Проверка появления панели информации о двери"):
            assert work.check_door_info_panel() == True

@pytest.mark.usefixtures("driver_class")

class HitmanSaveProjectsPage:
    def create_test_project(self, is_authorized = False):
        work = WorkPage(self.driver_class)
        work.open_main()

        wait(2)

        work.click_button_video_close(is_authorized)

        if is_authorized:
            work.add_new_project("test save project")

            work.click_category_build_selector(2, 1)
            work.click_by_canvas(250, 100)
            work.paint_room(650, 300)

            work.click_category_build_selector(2, 1)
            work.click_by_canvas(0, 300)
            work.paint_room(300, 400)

            work.click_by_canvas(0, -300)

            work.set_new_building_item(category=4, subcategory=1, num_item=2, x=0, y=150)

            work.set_new_building_item(category=4, subcategory=1, num_item=7, x=150, y=300)

            work.set_new_building_item(category=4, subcategory=2, num_item=6, x=650, y=150)

            work.set_new_building_item(category=4, subcategory=2, num_item=10, x=0, y=600)

            work.click_button_models()

            work.set_new_model_item(category=5, subcategory=4, num_item=3, x=40, y=40)

            work.set_new_model_item(category=5, subcategory=2, num_item=6, x=100, y=40)

            work.set_new_model_item(category=5, subcategory=3, num_item=6, x=40, y=250)

            work.set_new_model_item(category=5, subcategory=4, num_item=2, x=40, y=295)
            work.click_by_canvas(40, 288)
            work.give_offset_floor("180")
            work.click_by_canvas(-40, -288)

            work.set_new_model_item(category=3, subcategory=3, num_item=1, x=470, y=295)

            work.set_new_model_item(category=3, subcategory=1, num_item=5, x=585, y=40)

            work.set_new_model_item(category=2, subcategory=1, num_item=2, x=15, y=500)

            work.set_new_model_item(category=2, subcategory=4, num_item=2, x=180, y=500)

            work.set_new_model_item(category=8, subcategory=4, num_item=1, x=295, y=420)
            work.click_by_canvas(288, 420)
            work.give_offset_floor("080")
            work.click_by_canvas(-288, -420)

            work.set_new_model_item(category=4, subcategory=2, num_item=2, x=295, y=500)

        else:
            work.click_category_build_selector(2, 1)
            work.click_by_canvas(600, 150)
            work.paint_room(650, 300)

            work.click_category_build_selector(2, 1)
            work.click_by_canvas(0, 300)
            work.paint_room(300, 400)

            work.click_by_canvas(0, -300)

            work.set_new_building_item(category=4, subcategory=1, num_item=2, x=0, y=150)

            work.set_new_building_item(category=4, subcategory=1, num_item=7, x=150, y=300)

            work.set_new_building_item(category=4, subcategory=2, num_item=6, x=650, y=150)

            work.set_new_building_item(category=4, subcategory=2, num_item=10, x=0, y=600)

            work.click_button_models()

            work.set_new_model_item(category=5, subcategory=4, num_item=3, x=40, y=40)

            work.set_new_model_item(category=5, subcategory=2, num_item=6, x=100, y=40)

            work.set_new_model_item(category=5, subcategory=3, num_item=6, x=40, y=250)

            work.set_new_model_item(category=5, subcategory=4, num_item=2, x=40, y=295)
            work.click_by_canvas(40, 288)
            work.give_offset_floor("180")
            work.click_by_canvas(-40, -288)

            work.set_new_model_item(category=3, subcategory=3, num_item=1, x=470, y=295)

            work.set_new_model_item(category=3, subcategory=1, num_item=5, x=585, y=40)

            work.set_new_model_item(category=2, subcategory=1, num_item=2, x=15, y=500)

            work.set_new_model_item(category=2, subcategory=4, num_item=2, x=180, y=500)

            work.set_new_model_item(category=8, subcategory=4, num_item=1, x=295, y=420)
            work.click_by_canvas(288, 420)
            work.give_offset_floor("080")
            work.click_by_canvas(-288, -420)

            work.set_new_model_item(category=4, subcategory=2, num_item=2, x=295, y=500)

        # work.find_and_set_model_item(name="модуль", num_item=3, x=645, y=40)

    def check_save_3d_2d_mode_switch(self, is_authorized = False):
        work = WorkPage(self.driver_class)
        work.open_main()

        wait(2)

        work.click_3d()

        work.click_2d()

        with allure.step("Проверка стены"):
            assert work.check_alive_building_item("Стена", "wall-info", 5, 200) == True

        with allure.step("Проверка стены"):
            assert work.check_alive_building_item("Стена", "wall-info", 655, 20) == True

        with allure.step("Проверка стены"):
            assert work.check_alive_building_item("Стена", "wall-info", 550, 305) == True

        with allure.step("Проверка стены"):
            assert work.check_alive_building_item("Стена", "wall-info", 285, 305) == True

        with allure.step("Проверка стены"):
            assert work.check_alive_building_item("Стена", "wall-info", 305, 400) == True

        with allure.step("Проверка стены"):
            assert work.check_alive_building_item("Стена", "wall-info", 5, 400) == True

        with allure.step("Проверка стены"):
            assert work.check_alive_building_item("Стена", "wall-info", 20, 705) == True

        with allure.step("Проверка Дверь входная №6"):
            assert work.check_alive_building_item("Дверь входная №6", "door-info", 0, 150) == True

        with allure.step("Проверка Дверь распашная с аркой"):
            assert work.check_alive_building_item("Дверь распашная с аркой", "door-info", 155, 305) == True

        with allure.step("Проверка Окно трехстворчатое с фрамугой №5"):
            assert work.check_alive_building_item("Окно трехстворчатое с фрамугой №5", "window-info", 655,
                                                  155) == True

        with allure.step("Проверка Арочное окно"):
            assert work.check_alive_building_item("Арочное окно", "window-info", 5, 650) == True

        with allure.step("Проверка Вешалка напольная Hook"):
            assert work.check_alive_model_item("Вешалка напольная Hook", 40, 40) == True

        with allure.step("Проверка Шкаф 1 дверный Оскар с стеклом"):
            assert work.check_alive_model_item("Шкаф 1 дверный Оскар с стеклом", 100, 40) == True

        with allure.step("Проверка Зеркало (лофт)"):
            assert work.check_alive_model_item("Зеркало (лофт)", 10, 250) == True

        with allure.step("Проверка Вешалка настенная Торонто"):
            assert work.check_alive_model_item("Вешалка настенная Торонто", 40, 288, offset=180) == True

        with allure.step("Проверка Кухня модульная"):
            assert work.check_alive_model_item("Кухня модульная", 470, 285) == True

        with allure.step("Проверка Модуль напольный 3 дверцы"):
            assert work.check_alive_model_item("Модуль напольный 3 дверцы", 585, 40) == True

        with allure.step("Проверка Диван BOSS.XO"):
            assert work.check_alive_model_item("Диван BOSS.XO", 20, 500) == True

        with allure.step("Проверка Столик круглый (арт деко)"):
            assert work.check_alive_model_item("Столик круглый (арт деко)", 180, 500) == True

        with allure.step("Проверка Монитор"):
            assert work.check_alive_model_item("Монитор", 288, 420, offset=80) == True

        with allure.step("Проверка Столик консольный (классика)"):
            assert work.check_alive_model_item("Столик консольный (классика)", 288, 500) == True

        work.create_screenshot_canvas()

        wait(2)
    
    def check_autosave(self, is_authorized = False):
        work = WorkPage(self.driver_class)
        work.open_main()

        if is_authorized:
            work.open_dashboard()
            wait(8)

            dash = DashboardPage(self.driver_class)
            dash.open_first_project()
            wait(8)

            with allure.step("Проверка стены"):
                assert work.check_alive_building_item("Стена", "wall-info", 5, 200) == True

            with allure.step("Проверка стены"):
                assert work.check_alive_building_item("Стена", "wall-info", 655, 20) == True

            with allure.step("Проверка стены"):
                assert work.check_alive_building_item("Стена", "wall-info", 550, 305) == True

            with allure.step("Проверка стены"):
                assert work.check_alive_building_item("Стена", "wall-info", 285, 305) == True

            with allure.step("Проверка стены"):
                assert work.check_alive_building_item("Стена", "wall-info", 305, 400) == True

            with allure.step("Проверка стены"):
                assert work.check_alive_building_item("Стена", "wall-info", 5, 400) == True

            with allure.step("Проверка стены"):
                assert work.check_alive_building_item("Стена", "wall-info", 20, 705) == True

            with allure.step("Проверка Дверь входная №6"):
                assert work.check_alive_building_item("Дверь входная №6", "door-info", 0, 150) == True

            with allure.step("Проверка Дверь распашная с аркой"):
                assert work.check_alive_building_item("Дверь распашная с аркой", "door-info", 155, 305) == True

            with allure.step("Проверка Окно трехстворчатое с фрамугой №5"):
                assert work.check_alive_building_item("Окно трехстворчатое с фрамугой №5", "window-info", 655, 155) == True

            with allure.step("Проверка Арочное окно"):
                assert work.check_alive_building_item("Арочное окно", "window-info", 5, 650) == True

            with allure.step("Проверка Вешалка напольная Hook"):
                assert work.check_alive_model_item("Вешалка напольная Hook", 40, 40) == True

            with allure.step("Проверка Шкаф 1 дверный Оскар с стеклом"):
                assert work.check_alive_model_item("Шкаф 1 дверный Оскар с стеклом", 100, 40) == True

            with allure.step("Проверка Зеркало (лофт)"):
                assert work.check_alive_model_item("Зеркало (лофт)", 10, 250) == True

            with allure.step("Проверка Вешалка настенная Торонто"):
                assert work.check_alive_model_item("Вешалка настенная Торонто", 40, 288, offset=180) == True

            with allure.step("Проверка Кухня модульная"):
                assert work.check_alive_model_item("Кухня модульная", 470, 285) == True

            with allure.step("Проверка Модуль напольный 3 дверцы"):
                assert work.check_alive_model_item("Модуль напольный 3 дверцы", 585, 40) == True

            with allure.step("Проверка Диван BOSS.XO"):
                assert work.check_alive_model_item("Диван BOSS.XO", 20, 500) == True

            with allure.step("Проверка Столик круглый (арт деко)"):
                assert work.check_alive_model_item("Столик круглый (арт деко)", 180, 500) == True

            with allure.step("Проверка Монитор"):
                assert work.check_alive_model_item("Монитор", 288, 420, offset=80) == True

            with allure.step("Проверка Столик консольный (классика)"):
                assert work.check_alive_model_item("Столик консольный (классика)", 288, 500) == True

        else:
            wait(100)
            work.refresh_tab()
            wait(8)

            with allure.step("Проверка стены"):
                assert work.check_alive_building_item("Стена", "wall-info", 5, 200) == True

            with allure.step("Проверка стены"):
                assert work.check_alive_building_item("Стена", "wall-info", 655, 20) == True

            with allure.step("Проверка стены"):
                assert work.check_alive_building_item("Стена", "wall-info", 550, 305) == True

            with allure.step("Проверка стены"):
                assert work.check_alive_building_item("Стена", "wall-info", 285, 305) == True

            with allure.step("Проверка стены"):
                assert work.check_alive_building_item("Стена", "wall-info", 305, 400) == True

            with allure.step("Проверка стены"):
                assert work.check_alive_building_item("Стена", "wall-info", 5, 400) == True

            with allure.step("Проверка стены"):
                assert work.check_alive_building_item("Стена", "wall-info", 20, 705) == True

            with allure.step("Проверка Дверь входная №6"):
                assert work.check_alive_building_item("Дверь входная №6", "door-info", 0, 150) == True

            with allure.step("Проверка Дверь распашная с аркой"):
                assert work.check_alive_building_item("Дверь распашная с аркой", "door-info", 155, 305) == True

            with allure.step("Проверка Окно трехстворчатое с фрамугой №5"):
                assert work.check_alive_building_item("Окно трехстворчатое с фрамугой №5", "window-info", 655, 155) == True

            with allure.step("Проверка Арочное окно"):
                assert work.check_alive_building_item("Арочное окно", "window-info", 5, 650) == True

            with allure.step("Проверка Вешалка напольная Hook"):
                assert work.check_alive_model_item("Вешалка напольная Hook", 40, 40) == True

            with allure.step("Проверка Шкаф 1 дверный Оскар с стеклом"):
                assert work.check_alive_model_item("Шкаф 1 дверный Оскар с стеклом", 100, 40) == True

            with allure.step("Проверка Зеркало (лофт)"):
                assert work.check_alive_model_item("Зеркало (лофт)", 10, 250) == True

            with allure.step("Проверка Вешалка настенная Торонто"):
                assert work.check_alive_model_item("Вешалка настенная Торонто", 40, 288, offset=180) == True

            with allure.step("Проверка Кухня модульная"):
                assert work.check_alive_model_item("Кухня модульная", 470, 285) == True

            with allure.step("Проверка Модуль напольный 3 дверцы"):
                assert work.check_alive_model_item("Модуль напольный 3 дверцы", 585, 40) == True

            with allure.step("Проверка Диван BOSS.XO"):
                assert work.check_alive_model_item("Диван BOSS.XO", 20, 500) == True

            with allure.step("Проверка Столик круглый (арт деко)"):
                assert work.check_alive_model_item("Столик круглый (арт деко)", 180, 500) == True

            with allure.step("Проверка Монитор"):
                assert work.check_alive_model_item("Монитор", 288, 420, offset=80) == True

            with allure.step("Проверка Столик консольный (классика)"):
                assert work.check_alive_model_item("Столик консольный (классика)", 288, 500) == True

@pytest.mark.usefixtures("paste_project_for_guest")
class TestsGuestHitmanModelsConstraints(HitmanModelsPage):
    @allure.feature('Ограничения Гость')
    @allure.title('Появление плашки в каталоге')
    def test_check_down_block_in_category(self):
        super().check_down_block_in_category(is_authorized = False)

    @allure.feature('Ограничения Гость')
    @allure.title('Появление плашки в подкаталоге')
    def test_сheck_work_down_block_in_category(self):
        super().сheck_work_down_block_in_category(tarif='guest')

    @allure.feature('Ограничения Гость')
    @allure.title('Ссылка на страницу')
    def test_check_true_link_block_in_category(self):
        super().check_true_link_block_in_category()


@allure.title('Проверка работы функционала на Бесплатном')
@pytest.mark.usefixtures("auth_base",  "drop_all_project", "paste_project")
class TestsFreeHitmanModelsConstraints(HitmanModelsPage):
    @allure.feature('Ограничения Бесплатный тариф')
    @allure.title('Появление плашки в каталоге')
    def test_check_down_block_in_category(self):
        super().check_down_block_in_category(is_authorized = True)

    @allure.feature('Ограничения Бесплатный тариф')
    @allure.title('Появление плашки в подкаталоге')
    def test_сheck_work_down_block_in_category(self):
        super().сheck_work_down_block_in_category(tarif = 'free')

    @allure.feature('Ограничения Бесплатный тариф')
    @allure.title('Ссылка на страницу')
    def test_check_true_link_block_in_category(self):
        super().check_true_link_block_in_category()


@pytest.mark.usefixtures("paste_project_for_guest")
class TestsHitmanBaseConstraints(HitmanBasesPage):
    @allure.feature('Свойства Гость')
    @allure.title('Появление панели информации о двери')
    def test_check_door_internals(self):
        super().check_door_internals(is_authorized=False)

class TestsHitmanSaveProjectsPage(HitmanSaveProjectsPage):
    @allure.feature('Сохранения Гость')
    @allure.title('Создание проеката на тарифе Гость')
    def test_create_test_project(self):
        super().create_test_project(is_authorized=False)

    @allure.feature("Сохранения Гость")
    @allure.title('Сохранение предметов после изменений пространства на тарифе Гость')
    def test_check_save_3d_2d_mode_switch(self):
        super().check_save_3d_2d_mode_switch(is_authorized=False)

    @allure.feature("Сохранения Гость")
    @allure.title('Автосохранение предметов на тарифе Гость')
    def test_check_autosave(self):
        super().check_autosave(is_authorized=False)

@allure.title('Проверка работы функционала на Бесплатном')
@pytest.mark.usefixtures("auth_base",  "drop_all_project", "paste_project")
class TestsFreeHitmanSaveProjectsPage(HitmanSaveProjectsPage):
    @allure.feature('Сохранения Бесплатный тариф')
    @allure.title('Создание проеката на Бесплатном тарифе')
    def test_create_test_project(self):
        super().create_test_project(is_authorized=True)

    @allure.feature('Сохранения Бесплатный тариф')
    @allure.title('Сохранение предметов после изменений пространства на Бесплатном тарифе')
    def test_check_save_3d_2d_mode_switch(self):
        super().check_save_3d_2d_mode_switch(is_authorized=True)

    @allure.feature('Сохранения Бесплатный тариф')
    @allure.title('Автосохранение предметов на Бесплатном тарифе')
    def test_check_autosave(self):
        super().check_autosave(is_authorized=True)