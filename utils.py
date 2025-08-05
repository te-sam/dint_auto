from core.config import settings


def get_phpsessid(driver) -> str | None:
    """Получение phpsessid из cookies."""
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
    """Получение auth из cookies."""
    cookies = driver.get_cookies()
    auth = next(
        (cookie["value"] for cookie in cookies if cookie["name"] == "auth"),
        None,
    )
    return auth


def get_host(add_credentials: bool = False) -> str:
    """Получение host.

    Returns:
        str: тестовый или релизный хост.
    """
    if settings.MODE == "TEST":
        if add_credentials:
            host = f"https://{settings.USER}:{settings.PASSWORD}@online-dint.ulapr.ru"
        else:
            host = "https://online-dint.ulapr.ru"
    else:
        host = "https://roomplan.ru"
    return host
