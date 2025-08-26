import allure
import requests

from core.logger import logger
from pages.dashboard_page import DashboardPage
from pages.work_page import WorkPage
from utils import get_auth, get_host, get_phpsessid


def test_duble_project(
    driver,
    auth_profi_function,
    drop_all_projects_function,
    paste_project_function,
):
    """Тестирование дублирования проекта в дашборде."""
    dash = DashboardPage(driver)

    with allure.step("Открыть дашборд"):
        dash.open_dashboard()
    with allure.step("Дублировать первый проект"):
        dash.copy_first_project()

    with allure.step("Проверить наличие копии проекта"):
        phpsessid = get_phpsessid(driver)
        auth = get_auth(driver)
        host = get_host()

        if auth:
            response = requests.post(
                f"{host}/app/lk/admin/index.php?r=user/getProjects",
                cookies={"PHPSESSID": phpsessid, "auth": auth},
            )

            projects = response.json()
            logger.debug(response.json())
            assert len(projects) == 2, "В списке должно быть два проекта"
            assert any(
                "копия" in project.get("name", "") for project in projects
            ), 'В списке нет проекта в названии которого есть слово "копия"'
        else:
            logger.warning("Пользователь не авторизован")


# def test_walk_not_empty(driver, auth_profi_function, paste_project_function):
#     """Проверка, что прогулка не пустая"""
#     work = WorkPage(driver)

#     with allure.step("Открыть главную страницу"):
#         work.open_main()

#     with allure.step("Перейти в режим прогулки"):
#         work.click_walk()

# with allure.step("Проверить, что прогулка не пустая"):
# work.create_screenshot_element(locator=(l_canvas_3D), saving_path="walk.png")
# allure.attach(
#     driver.get_screenshot_as_png(),
#     name="Скриншот по окончании теста",
#     attachment_type=allure.attachment_type.PNG
# )
# assert work.is_walk_not_empty(), "Прогулка пустая"
