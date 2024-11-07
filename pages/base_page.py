from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_main(self, credentials):
        username, password = credentials
        self.driver.get(f'https://{username}:{password}@online-dint.ulapr.ru/app/')

    def find(self, args):
        return self.driver.find_element(*args)
    
    def finds(self, args):
        return self.driver.find_elements(*args)
    
    def switch_new_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])

    def scroll_to_element(self, locator):
        self.wait((By.CSS_SELECTOR,  locator))
        element = self.driver.find_element(By.CSS_SELECTOR, locator)
        ActionChains(self.driver).scroll_to_element(element).perform()

    def wait(self, locator):
        wait = WebDriverWait(self.driver, 5, poll_frequency=.8)
        wait.until(EC.presence_of_element_located(locator))

    def true_url(self, true_url):
        return self.driver.current_url == true_url
    
    def create_screenshot(self, path: str) -> None:
        self.driver.save_screenshot(path)
