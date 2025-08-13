import allure
import requests

from core.logger import logger
from pages.dashboard_page import DashboardPage
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
