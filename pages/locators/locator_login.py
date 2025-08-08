from selenium.webdriver.common.by import By

locator_auth_btn = (By.CSS_SELECTOR, ".auth-btn")
locator_register_btn = (By.ID, "registerLink")
locator_email_login = (By.ID, "login")
locator_password_login = (By.ID, "password")
locator_password2_login = (By.ID, "password2")
locator_enter_btn = (By.ID, "enterButton")
locator_register_start_btn = (By.ID, "registerStartButton")

locator_error_login = (By.XPATH, '//*[@id="login_form"]/div[1]/label[2]')
