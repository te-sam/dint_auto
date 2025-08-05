import allure
import pytest
import requests

from config import settings


@pytest.mark.parametrize(
    "url",
    [
        "https://roomplan.ru/app/projects.php",
        "https://roomplan.ru/app",
        "https://roomplan.ru/",
        "https://roomplan.ru/app/lk/client/index.php?r=loginClient",
        "https://roomplan.ru/order.php",
        "https://roomplan.ru/help.php",
        "https://roomplan.ru/blog.php",
        "https://roomplan.ru/support.php",
        "https://roomplan.ru/litsenzionnoye-soglasheniye.php",
        "https://roomplan.ru/privacy-policy.php",
        "https://roomplan.ru/app/lk/client/index.php?r=loginClient/register",
        f"https://{settings.USER}:{settings.PASSWORD}@online-dint.ulapr.ru/app/projects.php",
        f"https://{settings.USER}:{settings.PASSWORD}@online-dint.ulapr.ru/app",
        f"https://{settings.USER}:{settings.PASSWORD}@online-dint.ulapr.ru/",
        f"https://{settings.USER}:{settings.PASSWORD}@online-dint.ulapr.ru/app/lk/client/index.php?r=loginClient",
        f"https://{settings.USER}:{settings.PASSWORD}@online-dint.ulapr.ru/order.php",
        f"https://{settings.USER}:{settings.PASSWORD}@online-dint.ulapr.ru/help.php",
        f"https://{settings.USER}:{settings.PASSWORD}@online-dint.ulapr.ru/blog.php",
        f"https://{settings.USER}:{settings.PASSWORD}@online-dint.ulapr.ru/support.php",
        f"https://{settings.USER}:{settings.PASSWORD}@online-dint.ulapr.ru/litsenzionnoye-soglasheniye.php",
        f"https://{settings.USER}:{settings.PASSWORD}@online-dint.ulapr.ru/app/lk/client/index.php?r=loginClient/register",
    ],
)
@allure.feature("Наличие метрики")
def test_metrika(url):
    metrika = "(function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};"
    response = requests.get(url)
    html = response.text
    if "https://roomplan.ru/" in url:
        assert metrika in html
    else:
        assert metrika not in html
