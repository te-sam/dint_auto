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

class HitmanProjectsPage:
    def check_auto_save_project(self, is_authorized = False):
        work = WorkPage(self.driver_class)
        work.open_main()

        wait(2)

        work.click_button_video_close(is_authorized)

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
        work.give_offset_floor("100")
        work.click_by_canvas(-288, -420)

        work.set_new_model_item(category=4, subcategory=2, num_item=2, x=295, y=500)

        # work.find_and_set_model_item(name="модуль", num_item=3, x=645, y=40)

        work.click_2D()

        work.click_3D()

        # wait(120)

        # work.refresh_tab()

        input('Press Enter to continue...')

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
    @allure.feature('Ограничения Гость')
    @allure.title('Появление панели информации о двери')
    def test_check_door_internals(self):
        super().check_door_internals(is_authorized=False)

class TestsHitmanProjectsPage(HitmanProjectsPage):
    @allure.feature('Ограничения Гость')
    @allure.title('Проверка автоматического сохранения')
    def test_check_auto_save_project(self):
        super().check_auto_save_project(is_authorized=False)