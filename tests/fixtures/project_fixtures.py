import time
import pytest
import requests

from core.config import settings
from pages.dashboard_page import DashboardPage
from pages.work_page import WorkPage
from utils import get_auth, get_host, get_phpsessid
from loguru import logger


def drop_project(
    driver, project_id: str, phpsessid: str = None, auth: str = None
):
    if not phpsessid:
        phpsessid = get_phpsessid(driver)
    if not auth:
        auth = get_auth(driver)
    host = get_host()

    response = requests.post(
        f"{host}/app/lk/admin/index.php?r=user/deleteProject",
        cookies={"PHPSESSID": phpsessid, "auth": auth},
        json={"id": project_id},
    )

    if response.json()["success"]:
        logger.success(f"Проект {project_id} удален")
    else:
        logger.error(
            f"Проект {project_id} не удален. Ответ сервера: {response.json()}"
        )


def drop_all_projects(driver):
    phpsessid = get_phpsessid(driver)
    auth = get_auth(driver)
    host = get_host()

    if phpsessid:
        response = requests.post(
            f"{host}/app/lk/admin/index.php?r=user/getProjects",
            cookies={"PHPSESSID": phpsessid, "auth": auth},
        )

    logger.info(f"Всего проектов: {len(response.json())}")
    for project in response.json():
        drop_project(driver, int(project["id"]), phpsessid, auth)


@pytest.fixture(scope="class")
def drop_all_project_class(driver_class):
    yield
    drop_all_projects(driver_class)


@pytest.fixture(scope="function")
def drop_all_projects_function(driver):
    yield
    drop_all_projects(driver)


@pytest.fixture(scope="class")
def paste_project(driver_class):
    work = WorkPage(driver_class)
    work.open_main()

    # Вставить проект
    key = "autoSave"

    if settings.MODE == "TEST":
        project = "projects/project_test.txt"
    if settings.MODE == "PROD":
        project = "projects/project_prod.txt"

    project_number = None
    while project_number is None or project_number == "None":
        project_number = driver_class.execute_script(
            'return window.localStorage.getItem("openProject");'
        )
        logger.info(type(project_number))
    key += str(project_number)

    logger.info(key)

    with open(project, "r", encoding="utf-8") as file:
        value = file.read()

    script = f"window.localStorage.setItem(\"{key}\", '{value}');"
    driver_class.execute_script(script)
    driver_class.refresh()


@pytest.fixture(scope="class")
def paste_project_class(driver_class):
    """Фикстура для вставки проекта для гостя."""
    paste_project(driver_class)


@pytest.fixture(scope="function")
def paste_project_function(driver):
    """Фикстура для вставки проекта для гостя."""
    yield
    paste_project(driver)
    

def paste_project(driver):
    work = WorkPage(driver)
    work.open_main()
    work.click_start_button()
    
    if settings.MODE == "TEST":
        project = "projects/test.json"
    else:
        project = "projects/prod.json"

    with open(project, "r") as file:
        json = file.read(
    )
    script = f"core.Import({json});"
    driver.execute_script(script)


