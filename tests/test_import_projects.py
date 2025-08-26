from pathlib import Path

import pytest
from selenium.common.exceptions import JavascriptException

from core.logger import logger
from tests.fixtures.project_fixtures import paste_project

project_paths = list(Path("projects/all_projects_for_test").glob("*.json"))
project_files = [str(path) for path in project_paths]


@pytest.mark.parametrize("project_path", project_files)
def test_import_project(driver, project_path: str):
    try:
        # logger.info(f"Загружаю проект: {project_path}")
        paste_project(driver, project_path)
    except JavascriptException as e:
        error_message = getattr(e, "msg", str(e))
        logger.error(
            f"Проект {project_path} не загрузился. Ошибка {error_message}"
        )
        assert False, (
            f"Проект {project_path} не загрузился. Ошибка {error_message}"
        )
