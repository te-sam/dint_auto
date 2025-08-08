"""Модуль с локаторами основной страницы app."""

from selenium.webdriver.common.by import By

l_wall = (By.CSS_SELECTOR, '.item[data-tool="wall"]')
l_canvas = (By.ID, "canvas")
l_canvas_3D = (By.ID, "view3d")
l_2d = (By.CSS_SELECTOR, '[data-view="2D"]')
l_3d = (By.CSS_SELECTOR, '[data-mode="orbit"][data-view="3D"]')
l_walk = (By.CSS_SELECTOR, '[data-mode="firstPerson"][data-view="3D"]')
l_auth_btn = (By.CSS_SELECTOR, ".auth-btn")
l_name = (By.CSS_SELECTOR, "div.logo > span > input")
l_dashboard = (By.CSS_SELECTOR, "div.logo > a")
l_auth_btn = (By.CSS_SELECTOR, ".auth-btn")
l_email_login = (By.ID, "login")
l_password_login = (By.ID, "password")
l_enter_btn = (By.ID, "enterButton")
l_error_login = (By.XPATH, '//*[@id="login_form"]/div[1]/label[2]')
l_error_password = (By.XPATH, '//*[@id="passwordGroup"]/div/label[2]')
l_project_dots = (By.CLASS_NAME, "project_dots")
l_new_project_button = (By.ID, "new_project")
l_dialog_guest_constraint = (By.ID, "reg_modal")
# l_close_dialog_constraint = (By.ID, "close")
l_dialog_upgrade_walk = (By.ID, "fp_upgrade_tarif")
l_close_dialog_constraint = (By.CSS_SELECTOR, '[title="Close (Esc)"]')
l_save_button = (By.ID, "save_project")
l_save_screen_button = (By.ID, "screenshot")
l_save_to_pdf_button = (By.ID, "print")
l_save_3d_button = (By.ID, "export")
l_share_button = (By.ID, "share_project")
l_close_share_button = (By.CSS_SELECTOR, "div.modal-header > button")
l_dialog_share = (By.ID, "modal_share_project")
l_dialog_upgrade = (By.ID, "upgrade_tarif")
l_alcove_button = (By.CSS_SELECTOR, '[data-tool="alcove"]')  # Ниши
l_apperture_button = (
    By.CSS_SELECTOR,
    '[data-tool="apperture"]',
)  # Проемы
l_buttons_catalog_textures = (
    By.CLASS_NAME,
    "img-block",
)  # Каталог текстур
l_catalog_models = (By.ID, "models")

l_edit_height = (By.ID, "model_height")
l_trackbar_height_windowsill = (By.ID, "sill-height")
l_button_expand_settings_windowsill = (By.CSS_SELECTOR, "#open")
l_button_turn_column_90_left = (
    By.CSS_SELECTOR,
    "div.column-info > div.content > div.model-shortcut-panel > div.right-model-shortcut-panel > button:nth-child(2)",
)
l_button_turn_column_90_right = (
    By.CSS_SELECTOR,
    "div.column-info > div.content > div.model-shortcut-panel > div.right-model-shortcut-panel > button:nth-child(3)",
)
l_start_paint_btn = (By.CLASS_NAME, "empty_btn")
l_dialog_count_models = (By.CLASS_NAME, "stimulate-panel")
l_btn_in_dialog_count_models = (By.CLASS_NAME, "order-button")
l_start_video = (By.ID, "start_video")
l_stimulate_dialog_from_above = (
    By.CLASS_NAME,
    "stimulate-plane-content",
)
l_btn_in_dialog_from_above = (
    By.CLASS_NAME,
    "stimulate-plane-content-btn",
)
