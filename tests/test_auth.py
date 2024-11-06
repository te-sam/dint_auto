from pages.login_page import LoginPage
from time import sleep


# def test_successful_login(driver):
#     auth = LoginPage(driver)
#     auth.open_main()
#     auth.click_auth_btn()
#     auth.enter_login_data('art.samohwalov@yandex.ru', '123456')
#     auth.click_enter_btn()

# def test_failed_email(driver):
#     pass

# def test_failed_password(driver):
#     pass

def test_failed_login_empty_fields(driver):
    auth = LoginPage(driver)
    auth.open_main()
    auth.click_auth_btn()
    assert auth.get_state_label_error() == 'display: none;'
    auth.click_enter_btn()
    assert auth.get_state_label_error() == 'display: inline-block;'