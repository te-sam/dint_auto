from selenium.webdriver.common.by import By

locator_wall = (By.CSS_SELECTOR, '.item[data-tool="wall"]')
locator_canvas = (By.ID, "canvas")
locator_canvas_3D = (By.ID, "view3d")
locator_2d = (By.CSS_SELECTOR, '[data-view="2D"]')
locator_3d = (By.CSS_SELECTOR, '[data-mode="orbit"][data-view="3D"]')
locator_walk = (By.CSS_SELECTOR, '[data-mode="firstPerson"][data-view="3D"]')
locator_auth_btn = (By.CSS_SELECTOR, ".auth-btn")
locator_name = (By.CSS_SELECTOR, "div.logo > span > input")
locator_dashboard = (By.CSS_SELECTOR, "div.logo > a")
locator_auth_btn = (By.CSS_SELECTOR, ".auth-btn")
locator_email_login = (By.ID, "login")
locator_password_login = (By.ID, "password")
locator_enter_btn = (By.ID, "enterButton")
locator_error_login = (By.XPATH, '//*[@id="login_form"]/div[1]/label[2]')
locator_error_password = (By.XPATH, '//*[@id="passwordGroup"]/div/label[2]')
locator_project_dots = (By.CLASS_NAME, "project_dots")
locator_new_project_button = (By.ID, "new_project")
locator_dialog_guest_constraint = (By.ID, "reg_modal")
# locator_close_dialog_constraint = (By.ID, "close")
locator_dialog_upgrade_walk = (By.ID, "fp_upgrade_tarif")
locator_close_dialog_constraint = (By.CSS_SELECTOR, '[title="Close (Esc)"]')
locator_save_button = (By.ID, "save_project")
locator_save_screen_button = (By.ID, "screenshot")
locator_save_to_pdf_button = (By.ID, "print")
locator_save_3d_button = (By.ID, "export")
locator_share_button = (By.ID, "share_project")
locator_close_share_button = (By.CSS_SELECTOR, "div.modal-header > button")
locator_dialog_share = (By.ID, "modal_share_project")
locator_dialog_upgrade = (By.ID, "upgrade_tarif")
locator_alcove_button = (By.CSS_SELECTOR, '[data-tool="alcove"]')  # Ниши
locator_apperture_button = (
    By.CSS_SELECTOR,
    '[data-tool="apperture"]',
)  # Проемы
locator_buttons_catalog_textures = (
    By.CLASS_NAME,
    "img-block",
)  # Каталог текстур
locator_catalog_models = (By.ID, "models")

locator_edit_height = (By.ID, "model_height")
locator_trackbar_height_windowsill = (By.ID, "sill-height")
locator_button_expand_settings_windowsill = (By.CSS_SELECTOR, "#open")
locator_button_turn_column_90_left = (
    By.CSS_SELECTOR,
    "div.column-info > div.content > div.model-shortcut-panel > div.right-model-shortcut-panel > button:nth-child(2)",
)
locator_button_turn_column_90_right = (
    By.CSS_SELECTOR,
    "div.column-info > div.content > div.model-shortcut-panel > div.right-model-shortcut-panel > button:nth-child(3)",
)
locator_start_paint_btn = (By.CLASS_NAME, "empty_btn")
locator_dialog_count_models = (By.CLASS_NAME, "stimulate-panel")
locator_btn_in_dialog_count_models = (By.CLASS_NAME, "order-button")
locator_start_video = (By.ID, "start_video")
locator_stimulate_dialog_from_above = (
    By.CLASS_NAME,
    "stimulate-plane-content",
)
locator_btn_in_dialog_from_above = (
    By.CLASS_NAME,
    "stimulate-plane-content-btn",
)
