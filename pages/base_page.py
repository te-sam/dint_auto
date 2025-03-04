from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import settings


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def open_main(self):
        mode = settings.MODE
        print(mode)

        if mode == 'TEST':
            self.driver.get(f'https://{settings.USER}:{settings.PASSWORD}@online-dint.ulapr.ru/app/')
        if mode == 'PROD':
            self.driver.get(f'https://roomplan.ru/app/')


    def find(self, args):
        return self.driver.find_element(*args)
    

    def finds(self, args):
        return self.driver.find_elements(*args)
    

    def switch_new_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])


    def scroll_to_element(self, element):
        ActionChains(self.driver).scroll_to_element(element).perform()


    def wait(self, locator):
        wait = WebDriverWait(self.driver, 5, poll_frequency=.8)
        wait.until(EC.presence_of_element_located(locator))

    
    def await_clickable(self, element: tuple):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable(element))

    
    def await_visibility(self, element: tuple):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(element))


    def true_url(self, true_url):
        print(true_url)
        print(self.driver.current_url)
        parts_url = self.driver.current_url.split('//')
        # удаление логина и пароля из url
        current_url = "".join([parts_url[0], "//", parts_url[1].split('@')[1]])
        return current_url == true_url
    
    
    def create_screenshot(self, path: str) -> None:
        sleep(1)
        self.driver.save_screenshot(path)

    
    def create_screenshot_element(self, locator: tuple, saving_path: str) -> None:
        element = self.find(locator)
        element.screenshot(saving_path)


    def get_element_by_locator(self, locator: str):
        return self.find(locator)


    def switch_to_tab(self, number: int):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[number-1])
