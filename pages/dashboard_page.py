from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from config import settings
from pages.base_page import BasePage

locator_project_list = (By.CLASS_NAME, 'project-actions')
locator_project_delete = (By.ID, 'delete')
locator_project_open = (By.ID, 'open')
locator_confirm_delete = (By.CLASS_NAME, 'btn-delete')
locator_projects = (By.CLASS_NAME, 'project')
locator_project_name_list = (By.CLASS_NAME, 'project-name')
locator_new_project_button = (By.CLASS_NAME, 'new_project_text')

class DashboardPage(BasePage):
    def __init__(self, driver):
        self.driver = driver


    def get_dashboard(self) -> None:
        mode = settings.MODE
        
        if mode == 'TEST':
           url = f'https://{settings.USER}:{settings.PASSWORD}@online-dint.ulapr.ru/app/projects.php'
        if mode == 'PROD':
            url = f'https://roomplan.ru/app/projects.php'

        sleep(2)
        self.driver.get(url)


    def drop_first_project(self) -> None:
        project_list = self.find(locator_project_list)
        delete_button = self.find(locator_project_delete)
        confirm_delete_button = self.find(locator_confirm_delete)

        ActionChains(self.driver).move_to_element(project_list).move_to_element(delete_button).click().perform()
        confirm_delete_button.click()


    def drop_last_project(self) -> None:
        self.wait(locator_project_list)

        projects = list(self.finds(locator_project_list))
        delete_buttons = list(self.finds(locator_project_delete))
        confirm_delete_button = self.find(locator_confirm_delete)

        self.scroll_to_element(projects[-1])
        ActionChains(self.driver).move_to_element(projects[-1]).move_to_element(delete_buttons[-1]).click().perform()
        confirm_delete_button.click()
        sleep(1)

    
    def drop_all_projects(self) -> None:
        self.await_visibility(locator_new_project_button)
        try:
            self.wait(locator_project_list)

            count_projects = len(self.finds(locator_project_list))
            confirm_delete_button = self.find(locator_confirm_delete)

            for i in range(count_projects):
                project = self.find(locator_project_list)
                delete_button = self.find(locator_project_delete)
                ActionChains(self.driver).move_to_element(project).move_to_element(delete_button).click().perform()
                confirm_delete_button.click()
                sleep(1)
        except:
            print("Нет созданных проектов")

    
    def is_project_named(self, name_project: str) -> bool:
        try:
            self.wait(locator_project_name_list)
            project_names = list(self.finds(locator_project_name_list))

            for project in project_names:
                print(project.text)
                if project.text == name_project:
                    return True
        except:
            return False


    def get_count_project(self) -> int:
        try:
            self.wait(locator_project_list)
            return len(self.finds(locator_project_list))
        except:
            return 0


    def open_first_project(self):
        # project_list = self.find(locator_project_list)
        # open_button = self.find(locator_project_open)

        # ActionChains(self.driver).move_to_element(project_list).move_to_element(open_button).click().perform()

        self.await_clickable(locator_project_list)
        self.find(locator_project_list).click()

        sleep(2)

        self.await_clickable(locator_project_open)
        self.find(locator_project_open).click()


    def click_new_project(self) -> None:
        self.wait(locator_new_project_button)
        self.find(locator_new_project_button).click()





