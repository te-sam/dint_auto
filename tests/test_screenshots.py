import allure
import json

from pages.work_page import WorkPage

from time import sleep

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
        key = "autoSavenull"
        data = {
            'data': "18.11.24 18:00:43",
            'id': "not-save",
            'isAutoSave': True,
            'name': "Новый проект 2024",
            'preview': "data:image/png;base64,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",
            'project': {"connectors":[],"segments":[],"areas":[],"elements":[],"project_version":"1.1.1"}
        }
        # Преобразование словаря в JSON-строку
        json_string = json.dumps(data, ensure_ascii=False)

        # Экранирование кавычек для передачи в JavaScript
        escaped_json_string = json_string.replace("'", "\\'").replace('"', '\\"')

        # Сохранение в Local Storage
        driver.execute_script(f"window.localStorage.setItem('{key}', '{escaped_json_string}');")
        driver.refresh()
        sleep(60)
    with allure.step('Сделать скриншот 2D сцены'):
        work.create_screenshot('img/current_screen_2d.png')
        with open('img/current_screen_2d.png', 'rb') as f:
            allure.attach(f.read(), name="Скриншот 2D сцены", attachment_type=allure.attachment_type.PNG)
        # assert work.compare_img('img/current_screen_2d.png', 'img/screen_2d.png'), "Скриншоты не совпадают"
    with allure.step('Перейти на 3D сцену'):
        work.click_3d()
    with allure.step('Сделать скриншот 3D сцены'):
        work.create_screenshot('img/current_screen_3d.png')
        with open('img/current_screen_3d.png', 'rb') as f:
            allure.attach(f.read(), name="Скриншот 3D сцены", attachment_type=allure.attachment_type.PNG)
        # assert work.compare_img('img/current_screen_3d.png', 'img/screen_3d.png'), "Скриншоты не совпадают"

def test_one(driver, auth):
    work = WorkPage(driver)
    work.open_main()   
    work.rename_project("гавно")
    work.open_dashboard()
    local_storage_data = driver.execute_script("return JSON.stringify(window.localStorage);")
    print(local_storage_data)
    # sleep(5)