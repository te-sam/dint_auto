"""Модуль вспомогательных функций."""

from core.config import settings


def get_phpsessid(driver) -> str | None:
    """Получение phpsessid из cookies.
    
    Args:
        driver (WebDriver): Драйвер браузера.
        
    Returns:
        str: phpsessid cookie.

    """
    cookies = driver.get_cookies()
    phpsessid = next(
        (
            cookie["value"]
            for cookie in cookies
            if cookie["name"] == "PHPSESSID"
        ),
        None,
    )
    return phpsessid


def get_auth(driver) -> str | None:
    """Получение auth из cookies.
    
    Args:
        driver (WebDriver): Драйвер браузера.
        
    Returns:
        str: auth cookie.
    """
    cookies = driver.get_cookies()
    auth = next(
        (cookie["value"] for cookie in cookies if cookie["name"] == "auth"),
        None,
    )
    return auth


def get_host(add_credentials: bool = False) -> str:
    """Получение host.

    Args:
        add_credentials (bool, optional): Добавлять ли логин и пароль для аутентификации.

    Returns:
        str: тестовый или релизный хост.
    """
    if settings.MODE == "TEST":
        if add_credentials:
            return f"https://{settings.USER}:{settings.PASSWORD}@online-dint.ulapr.ru"
        else:
            return "https://online-dint.ulapr.ru"
    else:
        return "https://roomplan.ru"
