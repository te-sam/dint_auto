"""Модуль с локаторами страницы авторизации/регистрации."""

from selenium.webdriver.common.by import By

l_auth_btn = (By.CSS_SELECTOR, ".auth-btn")
l_register_btn = (By.ID, "registerLink")
l_email_login = (By.ID, "login")
l_password_login = (By.ID, "password")
l_password2_login = (By.ID, "password2")
l_enter_btn = (By.ID, "enterButton")
l_register_start_btn = (By.ID, "registerStartButton")

l_error_login = (By.XPATH, '//*[@id="login_form"]/div[1]/label[2]')
