from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.config import settings
from utils import get_host


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_main(self):
        host = get_host(add_credentials=True)

        if not self.true_url(
            f"{host}/app/".replace(f"{settings.USER}:{settings.PASSWORD}@", "")
        ):
            self.driver.get(f"{host}/app/")

        script = 'window.localStorage.setItem("videoShow", true);'
        self.driver.execute_script(script)

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
        wait = WebDriverWait(self.driver, 5, poll_frequency=0.8)
        wait.until(EC.presence_of_element_located(locator))

    def await_clickable(self, element: tuple):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable(element))

    def await_visibility(self, element: tuple):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(element))

    def true_url(self, true_url):
        current_url = self.driver.current_url

        if settings.MODE == "TEST":
            if "@" in current_url:
                parts_url = current_url.split("//")
                current_url = "".join(
                    [parts_url[0], "//", parts_url[1].split("@")[1]]
                )

            if "@" in true_url:
                parts_url = true_url.split("//")
                true_url = "".join(
                    [parts_url[0], "//", parts_url[1].split("@")[1]]
                )

        return current_url == true_url

    def create_screenshot(self, path: str) -> None:
        sleep(1)
        self.driver.save_screenshot(path)

    def create_screenshot_element(
        self, locator: tuple, saving_path: str
    ) -> None:
        element = self.find(locator)
        element.screenshot(saving_path)

    def get_element_by_locator(self, locator: str):
        return self.find(locator)

    def switch_to_tab(self, number: int):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[number - 1])
