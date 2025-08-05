from config import settings
from pages.login_page import LoginPage, get_activation_link


def test_registration(driver, delete_account):
    """Тест регистрации аккаунта, подвтерждение по ссылке"""
    auth = LoginPage(driver)
    auth.open_login()
    auth.click_register_login_btn()
    auth.enter_login(settings.EMAIL_ICMP)
    auth.enter_password(settings.EMAIL_ICMP)
    auth.enter_password2(settings.EMAIL_ICMP)
    auth.click_register_start_btn()

    activation_link = get_activation_link()
    assert activation_link
    auth.driver.get(activation_link)

    if settings.MODE == "TEST":
        link_account = f"https://{settings.USER}:{settings.PASSWORD}@online-dint.ulapr.ru/app/lk/client/index.php?r=clientSettings"
    else:
        link_account = (
            "https://roomplan.ru/app/lk/client/index.php?r=clientSettings"
        )
    auth.driver.get(link_account)
    assert auth.true_url(link_account)
