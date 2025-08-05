from selenium.webdriver.common.by import By

from pages.base_page import BasePage

l_settings_btn = (By.CSS_SELECTOR, "li:nth-child(3)")
l_delete_account_btn = (By.ID, "buttonDeleteAccount")
l_confirm_deletion_btn = (By.ID, "deleteAccount")


class LKPage(BasePage):
    """Методы для работы с личным кабинетом"""

    def open_lk(self):
        pass

    def click_settings(self):
        self.await_clickable(l_settings_btn)
        self.find(l_settings_btn).click()

    def click_delete_account(self):
        self.await_clickable(l_delete_account_btn)
        self.find(l_delete_account_btn).click()

    def click_confirm_deletion_account(self):
        self.await_clickable(l_confirm_deletion_btn)
        self.find(l_confirm_deletion_btn).click()
