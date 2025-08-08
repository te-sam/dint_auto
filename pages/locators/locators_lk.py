"""Модуль с локаторами страницы личного кабинета."""

from selenium.webdriver.common.by import By

l_settings_btn = (By.CSS_SELECTOR, "li:nth-child(3)")
l_delete_account_btn = (By.ID, "buttonDeleteAccount")
l_confirm_deletion_btn = (By.ID, "deleteAccount")
