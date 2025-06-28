from time import sleep as wait

import allure
import pytest

from pages.dashboard_page import DashboardPage
from pages.work_page import WorkPage
from config import settings


@pytest.mark.usefixtures("driver_class")

class TestsCheckButtonBoxAdaptive:
    def test_check_down_block_in_category(self):
        work = WorkPage(self.driver_class)
        work.open_main()

        wait(2)

        work.click_button_video_close()
        work.click_button_models()
        work.click_category_menu_models(4)

        with allure.step("Проверка появления плашки в каталоге"):
            assert work.check_stimulate_panel() == True

    def test_check_work_down_block_in_category(self):
        work = WorkPage(self.driver_class)

        work.click_subcategory(2)

        with allure.step("Проверка появления плашки в подкаталоге"):
            work.click_stimulate_panel_order_button()

    def test_check_true_link_block_in_category(self):
        work = WorkPage(self.driver_class)

        with allure.step("Проверка ссылки на страницу"):
            work.true_url("https://online-dint.ulapr.ru/order.php")