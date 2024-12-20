from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from PIL import ImageChops, Image
from pages.base_page import BasePage
from time import sleep

locator_wall = (By.CSS_SELECTOR, '.item[data-tool="wall"]')
locator_canvas = (By.ID, 'canvas')
locator_2d = (By.CSS_SELECTOR, '[data-view="2D"]')
locator_3d = (By.CSS_SELECTOR, '[data-mode="orbit"][data-view="3D"]')
locator_auth_btn = (By.CSS_SELECTOR, '.auth-btn')
locator_name = (By.CSS_SELECTOR, 'div.logo > span > input')
locator_dashboard = (By.CSS_SELECTOR, 'div.logo > a')
locator_auth_btn = (By.CSS_SELECTOR, '.auth-btn')
locator_email_login = (By.ID, 'login')
locator_password_login = (By.ID, 'password')
locator_enter_btn = (By.ID, 'enterButton')
locator_error_login = (By.XPATH, '//*[@id="login_form"]/div[1]/label[2]')
locator_error_password = (By.XPATH, '//*[@id="passwordGroup"]/div/label[2]')

class WorkPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
    

    def click_wall(self) -> None:
        self.wait(locator_wall)
        self.find(locator_wall).click()


    def click_2d(self) -> None:
        self.wait(locator_2d)
        self.find(locator_2d).click()       


    def click_3d(self) -> None:
        self.wait(locator_3d)
        self.find(locator_3d).click()


    def first_click_by_canvas(self, x: int, y: int) -> None:
        canvas =  self.find(locator_canvas)
        ActionChains(self.driver).move_to_element_with_offset(canvas, x, y).click().perform()
        

    def click_by_canvas(self, x: int, y: int) -> None:
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
        input_element = self.find(locator_name)
        input_element.send_keys(Keys.CONTROL, 'a')
        input_element.send_keys(Keys.DELETE)
        input_element.send_keys(new_name)


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