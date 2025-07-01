from time import sleep as wait

import allure
import pytest

from pages.dashboard_page import DashboardPage
from pages.work_page import WorkPage
from config import settings


@pytest.mark.usefixtures("driver_class")

class HitmanModelsConstraints:
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

class HitmanBaseConstraints:
    def check_door_internals(self, is_authorized = False):
        work = WorkPage(self.driver_class)
        work.open_main()

        wait(2)

        work.click_button_video_close(is_authorized)

        work.click_category_build_selector(4, 1)
        work.click_subcategory_build_selector(1)
        work.click_by_canvas(100, 100)

        with allure.step("Проверка появления панели информации о двери"):
            assert work.check_door_info_panel() == True


@pytest.mark.usefixtures("paste_project_for_guest")
class TestsGuestHitmanModelsConstraints(HitmanModelsConstraints):
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
class TestsFreeHitmanModelsConstraints(HitmanModelsConstraints):
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
class TestsHitmanBaseConstraints(HitmanBaseConstraints):
    @allure.feature('Ограничения Гость')
    @allure.title('Появление панели информации о двери')
    def test_check_door_internals(self):
        super().check_door_internals(is_authorized=False)