from selenium.webdriver.common.by import By
from pages.base_page import BasePage

locator_auth_btn = (By.CSS_SELECTOR, '.auth-btn')
locator_email_login = (By.ID, 'login')
locator_password_login = (By.ID, 'password')
locator_enter_btn = (By.ID, 'enterButton')

locator_error_login = (By.XPATH, '//*[@id="login_form"]/div[1]/label[2]')

class LoginPage(BasePage):
    def click_auth_btn(self):
        self.wait(locator_auth_btn)
        self.find(locator_auth_btn).click()

    def enter_login_data(self, email, password):
        self.find(locator_email_login).send_keys(email)
        self.find(locator_password_login).send_keys(password)
    
    def click_enter_btn(self):
        self.find(locator_enter_btn).click()
    
    def get_state_label(self, attribute):
        return self.find(locator_error_login).get_attribute(attribute)
    
    def get_text_label(self):
        return self.find(locator_error_login).text