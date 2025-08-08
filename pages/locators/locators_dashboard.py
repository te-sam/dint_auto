"""Модуль с локаторами страницы дашборда."""

from selenium.webdriver.common.by import By

l_project_list = (By.CLASS_NAME, "project-actions")
l_project_delete = (By.ID, "delete")
l_confirm_delete = (By.CLASS_NAME, "btn-delete")
l_projects = (By.CLASS_NAME, "project")
l_project_name_list = (By.CLASS_NAME, "project-name")
l_new_project_button = (By.CLASS_NAME, "new_project_text")
