from time import sleep
from typing import Literal

from PIL import Image, ImageChops
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage

locator_wall = (By.CSS_SELECTOR, '.item[data-tool="wall"]')
locator_canvas = (By.ID, 'canvas')
locator_canvas_3D = (By.ID, 'view3d')
locator_2d = (By.CSS_SELECTOR, '[data-view="2D"]')
locator_3d = (By.CSS_SELECTOR, '[data-mode="orbit"][data-view="3D"]')
locator_walk = (By.CSS_SELECTOR, '[data-mode="firstPerson"][data-view="3D"]')
locator_auth_btn = (By.CSS_SELECTOR, '.auth-btn')
locator_name = (By.CSS_SELECTOR, 'div.logo > span > input')
locator_dashboard = (By.CSS_SELECTOR, 'div.logo > a')
locator_auth_btn = (By.CSS_SELECTOR, '.auth-btn')
locator_email_login = (By.ID, 'login')
locator_password_login = (By.ID, 'password')
locator_enter_btn = (By.ID, 'enterButton')
locator_error_login = (By.XPATH, '//*[@id="login_form"]/div[1]/label[2]')
locator_error_password = (By.XPATH, '//*[@id="passwordGroup"]/div/label[2]')
locator_project_dots = (By.CLASS_NAME, 'project_dots')
locator_new_project_button = (By.ID, 'new_project')
locator_dialog_guest_constraint = (By.ID, 'reg_modal')
locator_close_dialog_constraint = (By.ID, 'close')
locator_save_button = (By.ID, 'save_project')
locator_save_screen_button = (By.ID, 'screenshot')
locator_save_to_pdf_button = (By.ID, 'print')
locator_save_3d_button = (By.ID, 'export')
locator_share_button = (By.ID, 'share_project')
locator_close_share_button = (By.CSS_SELECTOR, "div.modal-header > button")
locator_dialog_share = (By.ID, 'modal_share_project')
locator_dialog_upgrade = (By.ID, 'upgrade_tarif')
locator_alcove_button = (By.CSS_SELECTOR, '[data-tool="alcove"]')  # Ниши
locator_apperture_button = (By.CSS_SELECTOR, '[data-tool="apperture"]')  # Проемы
locator_buttons_catalog_textures = (By.CLASS_NAME, 'img-block')  # Каталог текстур
locator_catalog_models = (By.ID, 'models')
locator_button_video_close = (By.CLASS_NAME, 'video-close') # Закрыть видео в начале

locator_edit_height = (By.ID, 'model_height')
locator_trackbar_height_windowsill = (By.ID, 'sill-height')
locator_button_expand_settings_windowsill = (By.CSS_SELECTOR, '#open')
locator_button_turn_column_90_left = (By.CSS_SELECTOR, 'div.column-info > div > div.info-progress-bar > div.rotate-bnts > button:nth-child(1)')


class WorkPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
    

    def click_wall(self) -> None:
        self.await_clickable(locator_wall)
        self.find(locator_wall).click()


    def click_2d(self) -> None:
        self.await_clickable(locator_2d)
        self.find(locator_2d).click()       


    def click_3d(self) -> None:
        self.await_clickable(locator_3d)
        self.await_visibility(locator_3d)
        self.find(locator_3d).click()

    
    def click_walk(self) -> None:
        self.await_clickable(locator_walk)
        self.find(locator_walk).click()


    def first_click_by_canvas(self, view: Literal['2d', '3d'], x: int, y: int) -> None:
        if view == '2d':
            self.await_visibility(locator_canvas)
            canvas =  self.find(locator_canvas)
        if view == '3d':
            self.await_visibility(locator_canvas_3D)
            canvas = self.find(locator_canvas_3D)
        ActionChains(self.driver).move_to_element_with_offset(canvas, x, y).click().perform()
        

    def click_by_canvas(self, x: int, y: int) -> None:
        ActionChains(self.driver).move_by_offset(0, 0).perform()
        ActionChains(self.driver).move_by_offset(x, y).click().perform()


    def compare_img(self, base_image_path: str, actual_image_path: str) -> bool:
        base_image = Image.open(base_image_path)
        actual_image = Image.open(actual_image_path)
        diff = ImageChops.difference(base_image, actual_image)
        
        if diff.getbbox() is None:
            print("Изображения совпадают")
            return True
        else:
            print("Изображения различаются")
            return False


    def rename_project(self, new_name: str) -> None:
        self.wait(locator_name)
        self.await_clickable(locator_3d)
        input_element = self.find(locator_name)
        input_element.send_keys(Keys.CONTROL, 'a')
        input_element.send_keys(Keys.DELETE)
        input_element.send_keys(new_name)
        input_element.send_keys(Keys.ENTER)


    def open_dashboard(self) -> None:
        self.wait(locator_dashboard)
        self.find(locator_dashboard).click()

    
    def click_auth_btn(self) -> None:
        self.wait(locator_auth_btn)
        self.find(locator_auth_btn).click()


    def enter_login(self, email: str) -> None:
        self.find(locator_email_login).send_keys(email)
        
    
    def enter_password(self, password: str) -> None:
        self.find(locator_password_login).send_keys(password)
    

    def click_enter_btn(self) -> None:
        self.wait(locator_enter_btn)
        self.find(locator_enter_btn).click()
    

    def get_state_label_email(self, attribute: str) -> str:
        return self.find(locator_error_login).get_attribute(attribute)
    
    
    def get_text_label_email(self) -> str:
        return self.find(locator_error_login).text
    

    def get_state_label_password(self, attribute: str) -> str:
        return self.find(locator_error_password).get_attribute(attribute)
    
    
    def get_text_label_password(self) -> str:
        return self.find(locator_error_password).text
    

    def create_screenshot_canvas(self) -> None:
        # self.create_screenshot_element(locator_auth_btn, "img/screen_canvas.png")
         # Получить содержимое canvas как изображение в формате Base64
        canvas = self.find(locator_canvas)
        canvas_data = self.driver.execute_script(
            "return arguments[0].toDataURL('image/png');", canvas
        )

        # Удалить префикс "data:image/png;base64," и сохранить изображение
        base64_data = canvas_data.split(',')[1]

        with open("img/canvas_image.png", "wb") as file:
            import base64
            file.write(base64.b64decode(base64_data))
    
        print("Содержимое canvas сохранено в файл canvas_image.png.")


    def add_new_project(self, name: str) -> None:
        self.wait(locator_project_dots)
        self.rename_project(name)
        project_dots = self.find(locator_project_dots)
        new_project_button = self.find(locator_new_project_button)
        ActionChains(self.driver).move_to_element(project_dots).move_to_element(new_project_button).click().perform()
        sleep(1)
    

    def send_enter(self):
        self.find(locator_name).send_keys(Keys.ENTER)

    
    def check_dialog_constraint(self, block: bool, tarif = 'paid'):
        if tarif == 'guest':
            self.wait(locator_dialog_guest_constraint)
            dialog_constraint = self.find(locator_dialog_guest_constraint)
        else:
            self.wait(locator_dialog_upgrade)
            dialog_constraint = self.find(locator_dialog_upgrade)
        sleep(0.5)
        if block:
            assert dialog_constraint.is_displayed(), "Диалог ограничений не появился"
        else:
            print("Не блок")
            assert not dialog_constraint.is_displayed(), "Диалог ограничений появился"

    def check_dialog_share(self):
        dialog_share = self.find(locator_dialog_share)
        assert dialog_share.is_displayed(), "Окно Поделиться проектом не появилось"
        self.find(locator_close_share_button).click()


    def click_save(self, locator_button: str):
        self.await_clickable(locator_save_button)
        save_button = self.find(locator_save_button)
        save_something_button = self.find(locator_button)
        ActionChains(self.driver).move_to_element(save_button).move_to_element(save_something_button).click().perform()    

    
    def click_save_screen(self):
        self.click_save(locator_save_screen_button)


    def click_save_to_pdf(self):
        self.click_save(locator_save_to_pdf_button)


    def click_save_3d(self):
        self.click_save(locator_save_3d_button)


    def click_share(self):  #поделиться
        self.await_clickable(locator_share_button)
        self.find(locator_share_button).click()

    
    def click_alcove(self):  # ниши
        self.await_clickable(locator_alcove_button)
        self.find(locator_alcove_button).click()

    
    def click_apperture(self):  # проемы
        self.await_clickable(locator_apperture_button)
        self.find(locator_apperture_button).click()

    
    def change_height(self, height: int) -> None:
        self.find(locator_edit_height).send_keys(height)

    
    def click_texture_for_furniture(self, num_texture: int) -> None:
        locator = (By.CSS_SELECTOR, f'#ui > div.model-info > div > div.textures_block > div.textures-info > div:nth-child({num_texture})')
        self.find(locator).click()

    
    def click_texture_from_catalog(self):
        # buttons = self.finds(locator_buttons_catalog_textures)
        # print(f"Количество текстур: {len(buttons)}")

        # # Клик по первой видимой кнопке
        # for button in buttons:
        #     print(button)
        #     if button.is_displayed():
        #         button.click()
        #         return True
        locator = (By.CSS_SELECTOR, '.img-block.active')
        self.await_clickable(locator)
        self.find(locator).click()



    def expand_settings_windowsill(self):
        locator_windowsill_ranges = (By.CLASS_NAME, "windowsill-ranges")
        if self.find(locator_windowsill_ranges).get_attribute("style") != "display: block;":
            self.find(locator_button_expand_settings_windowsill).click()

    
    def change_windowsill(self, id_trackbar: str):
        trackbar = self.find((By.ID, id_trackbar))
        actions = ActionChains(self.driver)
        actions.click_and_hold(trackbar).move_by_offset(55, 0).release().perform()

    
    def turn_column_90_left(self):
        self.await_clickable(locator_button_turn_column_90_left)
        self.find(locator_button_turn_column_90_left).click()

    
    def click_animation_door(self, id_animation: str):
        locator_animation = (By.ID, id_animation)
        # self.await_clickable(locator_animation)
        self.find(locator_animation).click()

    
    def click_button_models(self):
        self.await_clickable(locator_catalog_models)
        self.find(locator_catalog_models).click()


    def click_category_menu_models(self, category: int):
        locator_category = (By.CSS_SELECTOR,f"#main_menu_block > button:nth-child({category})")
        self.await_clickable(locator_category)
        self.find(locator_category).click()
    
    def click_subcategory(self, subcategory: int):
        locator_subcategory = (By.CSS_SELECTOR, f"#ui > div.left-menu-block > div:nth-child(2) > div:nth-child(5) > div:nth-child({subcategory})")
        self.await_clickable(locator_subcategory)
        self.find(locator_subcategory).click()

    
    def add_in_favorite_from_catalog(self):
        locator = (By.ID, "set_like")
        self.await_clickable(locator)
        self.find(locator).click()


    def click_button_video_close(self):
        self.await_clickable(locator_button_video_close)
        self.find(locator_button_video_close).click()


    def check_stimulate_panel(self):
        locator = (By.CLASS_NAME, "stimulate-panel")
        self.find(locator)


    def click_stimulate_panel_order_button(self):
        locator = (By.CLASS_NAME, "order-button")
        self.await_clickable(locator)
        self.find(locator).click()