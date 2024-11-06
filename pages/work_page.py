from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PIL import ImageChops, Image
from pages.base_page import BasePage

locator_wall = (By.CSS_SELECTOR, '[data-tool="wall"]')
locator_canvas = (By.ID, 'canvas')
locator_2d = (By.CSS_SELECTOR, '[data-view="2D"]')
locator_3d = (By.CSS_SELECTOR, '[data-mode="orbit"][data-view="3D"]')
locator_auth_btn = (By.CSS_SELECTOR, '.auth-btn')

class WorkPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
    
    def click_wall(self):
        self.wait(locator_wall)
        self.find(locator_wall).click()

    def click_2d(self):
        self.wait(locator_2d)
        self.find(locator_2d).click()       

    def click_3d(self):
        self.wait(locator_3d)
        self.find(locator_3d).click()

    def first_click_by_canvas(self, x, y):
        canvas =  self.find(locator_canvas)
        ActionChains(self.driver).move_to_element_with_offset(canvas, x, y).click().perform()
        
    def click_by_canvas(self, x, y):
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


    