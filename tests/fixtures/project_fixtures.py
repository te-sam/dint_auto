import pytest

from pages.dashboard_page import DashboardPage
from pages.work_page import WorkPage
from config import settings


@pytest.fixture(scope="function")
def drop_project(driver):
    yield
    dash = DashboardPage(driver)
    if not dash.true_url("https://online-dint.ulapr.ru/app/projects.php"):
        dash.get_dashboard()
    dash.drop_all_projects()


@pytest.fixture(scope="class")
def drop_all_project(driver_class):
    dash = DashboardPage(driver_class)
    if not dash.true_url("https://online-dint.ulapr.ru/app/projects.php"):
        dash.get_dashboard()
    dash.drop_all_projects()


@pytest.fixture(scope="class")
def paste_project(driver_class):
    work = WorkPage(driver_class)
    work.open_main()

    # Вставить проект
    key = 'autoSave'

    if settings.MODE == "TEST":
        project = 'projects/project_test.txt'
    if settings.MODE == "PROD":
        project = 'projects/project_prod.txt'

    project_number = None
    while project_number is None or project_number == 'None':
        project_number = driver_class.execute_script('return window.localStorage.getItem("openProject");')
        # print(type(project_number))
    key += str(project_number)
    
    # print(key)

    with open(project, 'r', encoding='utf-8') as file:
        value = file.read()
    
    script = f'window.localStorage.setItem("{key}", \'{value}\');'
    driver_class.execute_script(script)
    # driver_class.refresh()