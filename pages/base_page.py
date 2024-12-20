import os
from dotenv import load_dotenv

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def open_main(self):
        load_dotenv()
        username = os.getenv("USER")
        password = os.getenv("PASSWORD")
        self.driver.get(f'https://{username}:{password}@online-dint.ulapr.ru/app/')


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
        wait = WebDriverWait(self.driver, 10, poll_frequency=1.5)
        wait.until(EC.presence_of_element_located(locator))


    def true_url(self, true_url):
        parts_url = self.driver.current_url.split('//')
        # удаление логина и пароля из url
        current_url = "".join([parts_url[0], "//", parts_url[1].split('@')[1]])
        return current_url == true_url
    
    
    def create_screenshot(self, path: str) -> None:
        sleep(1)
        self.driver.save_screenshot(path)