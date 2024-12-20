import allure

from pages.work_page import WorkPage


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

@allure.feature('Авторизация')
@allure.title('Пустое поле email при входе')
def test_failed_login_empty_email(driver):
    auth = WorkPage(driver)

    with allure.step('Открыть главную страницу'):
        auth.open_main()

    with allure.step('Кликнуть по кнопке "Войти в аккаунт"'):
        auth.click_auth_btn()
        assert auth.get_state_label_email('style') == 'display: none;', "Состояние метки должно быть 'display: none;'"

    with allure.step('Кликнуть по кнопке "Войти"'):
        auth.click_enter_btn()
        assert (auth.get_state_label_email('style') == 'display: inline-block;' and 
                auth.get_text_label_email() == 'Не указан логин'), "Состояние метки должно быть 'display: inline-block;' и текст 'Не указан логин'"


@allure.feature('Авторизация')
@allure.title('Пустое поле пароль при входе')
def test_failed_login_empty_password(driver):
    auth = WorkPage(driver)

    with allure.step('Открыть главную страницу'):
        auth.open_main()


    with allure.step('Кликнуть по кнопке "Войти в аккаунт"'):
        auth.click_auth_btn()

    with allure.step('Ввести email'):
        auth.enter_login('art.samohwalov@yandex.ru')


    with allure.step('Кликнуть по кнопке "Войти"'):
        auth.click_enter_btn()
        assert (auth.get_state_label_password('style') == 'display: inline-block;' and 
                auth.get_text_label_password() == 'Не указан пароль'), "Состояние метки должно быть 'display: inline-block;' и текст 'Не указан логин'"