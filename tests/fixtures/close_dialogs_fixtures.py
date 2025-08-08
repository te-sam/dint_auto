"""Модуль фикстур для закрытия диалогов апгрейда."""

from time import sleep

import pytest

from pages.locators.locators_work import (
    l_3d,
    l_close_dialog_constraint,
    l_dialog_guest_constraint,
    l_dialog_upgrade,
    l_dialog_upgrade_walk,
)
from pages.work_page import WorkPage


@pytest.fixture(scope="function")
def close_dialog_constraint_for_guest(driver_class, request):
    """Фикстура для закрытия диалога ограничений для гостя."""
    yield
    work = WorkPage(driver_class)
    dialog_constraint = driver_class.find_element(
        *l_dialog_guest_constraint
    )
    button_close_dialog_constraint = driver_class.find_element(
        *l_close_dialog_constraint
    )

    # Получаем параметр из request.param
    param_value = request.param if hasattr(request, "param") else None

    if (
        dialog_constraint.is_displayed()
        and button_close_dialog_constraint.is_displayed()
    ):
        button_close_dialog_constraint.click()
    else:
        if param_value:  # Если дилалог должен был появиться, но не появился
            if "active" in element_3d.get_attribute("class"):
                driver_class.refresh()
                element_3d = work.find(l_3d)
                sleep(2)
                work.click_3d()
            else:
                driver_class.refresh()
                sleep(2)


@pytest.fixture(scope="function")
def close_dialog_upgrade(driver_class, request):
    """Фикстура для закрытия диалога ограничений для платного тарифа."""
    yield
    work = WorkPage(driver_class)
    work.await_clickable(l_3d)
    element_3d = work.find(l_3d)
    dialog_upgrade = work.find(l_dialog_upgrade)

    # Получаем параметр из request.param
    param_value = request.param if hasattr(request, "param") else None

    if dialog_upgrade.is_displayed():
        button_close_dialog_upgrade = work.find(
            l_close_dialog_constraint
        )
        button_close_dialog_upgrade.click()
    else:
        if param_value:  # Если дилалог должен был появиться, но не появился
            if "active" in element_3d.get_attribute("class"):
                driver_class.refresh()
                element_3d = work.find(l_3d)
                sleep(2)
                work.click_3d()
            else:
                driver_class.refresh()
                sleep(2)


@pytest.fixture(scope="function")
def close_dialog_upgrade_walk(driver_class, request):
    """Фикстура для закрытия диалога ограничений прогулки."""
    yield
    work = WorkPage(driver_class)
    work.await_clickable(l_3d)
    element_3d = work.find(l_3d)
    dialog_upgrade = work.find(l_dialog_upgrade_walk)
    button_close_dialog_upgrade = work.find(l_close_dialog_constraint)

    # Получаем параметр из request.param
    param_value = request.param if hasattr(request, "param") else None

    if (
        dialog_upgrade.is_displayed()
        and button_close_dialog_upgrade.is_displayed()
    ):
        button_close_dialog_upgrade.click()
    else:
        if param_value:  # Если дилалог должен был появиться, но не появился
            driver_class.refresh()
            sleep(2)
