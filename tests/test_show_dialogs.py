import allure
import pytest

from pages.dashboard_page import DashboardPage
from pages.work_page import WorkPage
from utils import get_host


@allure.feature("Отображение диалогов")
@allure.title("Проверка диалога с количествои мебели в каталоге")
@pytest.mark.parametrize("use_auth", [True, False])
def test_show_dialog_count_models(driver, request, use_auth):
    if use_auth:
        request.getfixturevalue("auth_base_function")
    work = WorkPage(driver)
    with allure.step("Открыть главную страницу"):
        work.open_main()
    with allure.step("Перейти в каталог мебели"):
        work.click_button_models()
    with allure.step("Выбрать категорию 'Кухня'"):
        work.click_category_menu_models(3)
    with allure.step("Проверить отсутствие диалога"):
        work.check_dialog_count_models(show_dialog=False)
    with allure.step("Выбрать первую подкатегорию"):
        work.click_subcategory(1)
    with allure.step("Проверить появление диалога"):
        work.check_dialog_count_models(show_dialog=True)
    with allure.step("Кликнуть по кнопке 'Подключить сейчас'"):
        work.click_btn_in_dialog_count_models()
        host = get_host()
        assert work.true_url(f"{host}/order.php")


@allure.feature("Отображение диалогов")
@allure.title("Проверка стимулирующего диалога сверху над сценой")
@pytest.mark.parametrize("use_auth", [True, False])
def test_show_dialog_from_above_2d(driver, request, use_auth):
    if use_auth:
        request.getfixturevalue("auth_base_function")
    work = WorkPage(driver)
    with allure.step("Открыть главную страницу"):
        work.open_main()
    with allure.step(
        "Проверка отображения стимулирующего диалога сверху над сценой"
    ):
        if use_auth:
            work.check_stimulate_dialog_from_above(show_dialog=True)
            with allure.step("Кликнуть по кнопке 'Перейти на PRO'"):
                work.click_btn_in_dialog_from_above()
                host = get_host()
                assert work.true_url(f"{host}/order.php")
        else:
            work.check_stimulate_dialog_from_above(show_dialog=False)


@allure.feature("Отображение диалогов")
@allure.title("Проверка стимулирующего диалога сверху в дашборде")
@pytest.mark.parametrize("use_auth", [True, False])
def test_show_dialog_from_above_dashboard(driver, request, use_auth):
    if use_auth:
        request.getfixturevalue("auth_base_function")
    with allure.step("Перейти на дашборд"):
        dash = DashboardPage(driver)
        dash.open_dashboard()
    with allure.step(
        "Проверка отображения стимулирующего диалога сверху в дашборде"
    ):
        if use_auth:
            dash.check_stimulate_dialog_from_above(show_dialog=True)
            with allure.step("Кликнуть по кнопке 'Перейти на PRO'"):
                dash.click_btn_in_dialog_from_above()
                host = get_host()
                assert dash.true_url(f"{host}/order.php")
        else:
            dash.check_stimulate_dialog_from_above(show_dialog=False)
