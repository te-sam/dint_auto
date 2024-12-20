from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

locator_project_list = (By.CLASS_NAME, 'project-actions')
locator_project_delete = (By.ID, 'delete')
locator_confirm_delete = (By.CLASS_NAME, 'btn-delete')
locator_projects = (By.CLASS_NAME, 'project')
locator_project_name_list = (By.CLASS_NAME, 'project-name')

class DashboardPage(BasePage):
    def __init__(self, driver):
        self.driver = driver


    def get_dashboard(self) -> None:
        self.driver.get('https://online-dint.ulapr.ru/app/projects.php')
        self.wait(locator_project_list)


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
        self.wait(locator_project_list)

        count_projects = len(self.finds(locator_project_list))
        confirm_delete_button = self.find(locator_confirm_delete)

        for i in range(count_projects):
            project = self.find(locator_project_list)
            delete_button = self.find(locator_project_delete)
            ActionChains(self.driver).move_to_element(project).move_to_element(delete_button).click().perform()
            confirm_delete_button.click()
            sleep(1)

    
    def is_project_named(self, name_project: str) -> bool:
        self.wait(locator_project_name_list)
        project_names = list(self.finds(locator_project_name_list))

        for project in project_names:
            if project.text == name_project:
                return True
        
        return False





