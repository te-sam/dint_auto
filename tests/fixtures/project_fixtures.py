"""Модуль фикстур для работы с проектами."""

import time
import pytest
import requests

from core.config import settings
from pages.work_page import WorkPage
from utils import get_auth, get_host, get_phpsessid
from loguru import logger


def drop_project(
    driver, project_id: str, phpsessid: str = None, auth: str = None
) -> None:
    """Удаление проекта.

    Args:
        driver (WebDriver): Драйвер браузера.
        project_id (str): ID проекта.
        phpsessid (str, optional): phpsessid cookie. По умолчанию None.
        auth (str, optional): auth cookie. По умолчанию None.

    """
    if not phpsessid:
        phpsessid = get_phpsessid(driver)
    if not auth:
        auth = get_auth(driver)
    host = get_host()

    if phpsessid and auth:
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
    else:
        logger.warning("Пользователь не авторизован")


def drop_all_projects(driver) -> None:
    """Удаление всех проектов.

    Args:
        driver (WebDriver): Драйвер браузера.

    """
    phpsessid = get_phpsessid(driver)
    auth = get_auth(driver)
    host = get_host()

    if auth:
        response = requests.post(
            f"{host}/app/lk/admin/index.php?r=user/getProjects",
            cookies={"PHPSESSID": phpsessid, "auth": auth},
        )
        logger.info(f"Всего проектов: {len(response.json())}")
        for project in response.json():
            drop_project(driver, int(project["id"]), phpsessid, auth)
    else:
        logger.warning("Пользователь не авторизован")


def paste_project(driver) -> None:
    """Вставка проекта.

    Args:
        driver (WebDriver): Драйвер браузера.

    """
    work = WorkPage(driver)
    work.open_main()
    time.sleep(3)
    work.click_start_button()

    if settings.MODE == "TEST":
        project = "projects/test.json"
    else:
        project = "projects/prod.json"

    with open(project, "r") as file:
        json = file.read()
    script = f"core.Import({json});"
    driver.execute_script(script)


@pytest.fixture(scope="class")
def drop_all_project_class(driver_class):
    """Фикстура для удаления всех проектов при работе с классом."""
    drop_all_projects(driver_class)


@pytest.fixture(scope="function")
def drop_all_projects_function(driver):
    """Фикстура для удаления всех проектов при работе с функцией."""
    drop_all_projects(driver)


@pytest.fixture(scope="class")
def paste_project_class(driver_class):
    """Фикстура для вставки проекта для гостя при работе с классом."""
    paste_project(driver_class)


@pytest.fixture(scope="function")
def paste_project_function(driver):
    """Фикстура для вставки проекта для гостя при работе с функцией."""
    paste_project(driver)
