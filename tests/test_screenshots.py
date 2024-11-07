import allure

from pages.work_page import WorkPage

@allure.title('Проверка отображения на 2D и 3D сценах')
def test_screenshots(driver, credentials):
    work = WorkPage(driver)
    with allure.step('Открыть главную страницу'):
        work.open_main(credentials)
    with allure.step('Кликнуть "Рисовать стены"'):
        work.click_wall()
    with allure.step('Нарисовать комнату'):
        work.first_click_by_canvas(0, 0)
        work.click_by_canvas(0, 300)
        work.click_by_canvas(400, 0)
        work.click_by_canvas(0, -300)
        work.click_by_canvas(-400, 0)
    with allure.step('Сделать скриншот 2D сцены'):
        work.create_screenshot('img/current_screen_2d.png')
        assert work.compare_img('img/current_screen_2d.png', 'img/screen_2d.png'), "Скриншоты не совпадают"
    with allure.step('Перейти на 3D сцену'):
        work.click_3d()
    with allure.step('Сделать скриншот 3D сцены'):
        work.create_screenshot('img/current_screen_3d.png')
        assert work.compare_img('img/current_screen_3d.png', 'img/screen_3d.png'), "Скриншоты не совпадают"