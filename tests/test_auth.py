import allure

from pages.login_page import LoginPage


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


@allure.title('Пустое поле email при входе')
def test_failed_login_empty_fields(driver, credentials):
    auth = LoginPage(driver)
    with allure.step('Открыть главную страницу'):
        auth.open_main(credentials)
    with allure.step('Кликнуть по кнопке "Войти в аккаунт"'):
        auth.click_auth_btn()
        assert auth.get_state_label('style') == 'display: none;' 
    with allure.step('Кликнуть по кнопке "Войти"'):
        auth.click_enter_btn()
        assert auth.get_state_label('style') == 'display: inline-block;' and auth.get_text_label() == 'Не указан логин'