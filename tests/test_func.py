from time import sleep
import allure
import pytest

from pages.dashboard_page import DashboardPage
from pages.work_page import WorkPage



class TestsWithAuth:
    @pytest.mark.usefixtures("auth")
    @allure.feature('Работа с проектом')
    @allure.title('Переименование проекта')
    def test_rename_project(self, driver, drop_project):
        name_project = "Сарай"
        work = WorkPage(driver)
        dash = DashboardPage(driver)

        with allure.step('Открыть главную страницу'):
            work.open_main()   

        with allure.step('Ввести новое название'):    
            work.rename_project(name_project)
        
        with allure.step('Открыть дашборд'):   
            work.open_dashboard()
        assert dash.is_project_named(name_project), 'Проект не переименовался'


@allure.feature('Работа с проектом')
@allure.title('Проверка отображения на 2D и 3D сценах')
def test_screenshots(driver):
    work = WorkPage(driver)
    
    with allure.step('Открыть главную страницу'):
        work.open_main()

    with allure.step('Кликнуть "Рисовать стены"'):
        sleep(3)
        work.click_wall()

    with allure.step('Нарисовать комнату'):
        work.first_click_by_canvas(0, 0)
        work.click_by_canvas(0, 300)
        work.click_by_canvas(400, 0)
        work.click_by_canvas(0, -300)
        work.click_by_canvas(-400, 0)

    # work.create_screenshot('img/screen_2d.png')
    # work.click_3d()
    # work.create_screenshot('img/screen_3d.png')

    with allure.step('Сделать скриншот 2D сцены'):
        work.create_screenshot('img/current_screen_2d.png')
        with open('img/screen_2d.png', 'rb') as f:
            allure.attach(f.read(), name="Ожидаемый скриншот 2D сцены", attachment_type=allure.attachment_type.PNG)
        with open('img/current_screen_2d.png', 'rb') as f:
            allure.attach(f.read(), name="Текущий скриншот 2D сцены", attachment_type=allure.attachment_type.PNG)
        assert work.compare_img('img/current_screen_2d.png', 'img/screen_2d.png'), "Скриншоты 2D не совпадают"
    
    with allure.step('Перейти на 3D сцену'):
        work.click_3d()

    with allure.step('Сделать скриншот 3D сцены'):
        work.create_screenshot('img/current_screen_3d.png')
        with open('img/screen_3d.png', 'rb') as f:
            allure.attach(f.read(), name="Ожидаемый скриншот 3D сцены", attachment_type=allure.attachment_type.PNG)
        with open('img/current_screen_3d.png', 'rb') as f:
            allure.attach(f.read(), name="Текущий скриншот 3D сцены", attachment_type=allure.attachment_type.PNG)
        assert work.compare_img('img/current_screen_3d.png', 'img/screen_3d.png'), "Скриншоты 3D не совпадают"
