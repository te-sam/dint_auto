import allure

from pages.work_page import WorkPage

@allure.title('Проверка отображения на 2D и 3D сценах')
def test_screenshots(driver):
    work = WorkPage(driver)
    with allure.step('Открыть главную страницу'):
        work.open_main()
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
        with open('img/current_screen_2d.png', 'rb') as f:
            allure.attach(f.read(), name="Скриншот 2D сцены", attachment_type=allure.attachment_type.PNG)
        assert work.compare_img('img/current_screen_2d.png', 'img/screen_2d.png'), "Скриншоты 2D не совпадают"
    with allure.step('Перейти на 3D сцену'):
        work.click_3d()
    with allure.step('Сделать скриншот 3D сцены'):
        work.create_screenshot('img/current_screen_3d.png')
        with open('img/current_screen_3d.png', 'rb') as f:
            allure.attach(f.read(), name="Скриншот 3D сцены", attachment_type=allure.attachment_type.PNG)
        assert work.compare_img('img/current_screen_3d.png', 'img/screen_3d.png'), "Скриншоты 3D не совпадают"