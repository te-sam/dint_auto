"""Модуль с локаторами страницы дашборда."""

from selenium.webdriver.common.by import By

locator_project_list = (By.CLASS_NAME, "project-actions")
locator_project_delete = (By.ID, "delete")
locator_confirm_delete = (By.CLASS_NAME, "btn-delete")
locator_projects = (By.CLASS_NAME, "project")
locator_project_name_list = (By.CLASS_NAME, "project-name")
locator_new_project_button = (By.CLASS_NAME, "new_project_text")
