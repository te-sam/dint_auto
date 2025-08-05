import email
import imaplib
import time
from email import policy

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from core.config import settings
from pages.base_page import BasePage

locator_auth_btn = (By.CSS_SELECTOR, '.auth-btn')
locator_register_btn = (By.ID, 'registerLink')
locator_email_login = (By.ID, 'login')
locator_password_login = (By.ID, 'password')
locator_password2_login = (By.ID, 'password2')
locator_enter_btn = (By.ID, 'enterButton')
locator_register_start_btn = (By.ID, 'registerStartButton')

locator_error_login = (By.XPATH, '//*[@id="login_form"]/div[1]/label[2]')

class LoginPage(BasePage):
    def click_auth_btn(self):
        self.wait(locator_auth_btn)
        self.find(locator_auth_btn).click()

    def enter_login_data(self, email, password):
        self.find(locator_email_login).send_keys(email)
        self.find(locator_password_login).send_keys(password)
    
    def enter_login(self, email: str) -> None:
        element = self.find(locator_email_login)
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.DELETE)
        element.send_keys(email)
    
    def enter_password(self, password: str) -> None:
        element = self.find(locator_password_login)
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.DELETE)
        element.send_keys(password)

    def enter_password2(self, password: str) -> None:
        element = self.find(locator_password2_login)
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.DELETE)
        element.send_keys(password)

    def click_enter_btn(self):
        self.wait(locator_enter_btn)
        self.find(locator_enter_btn).click()

    def get_state_label(self, attribute):
        return self.find(locator_error_login).get_attribute(attribute)
    
    def get_text_label(self):
        return self.find(locator_error_login).text

    def open_login(self):
        """Открытие страницы входа"""
        mode = settings.MODE
        print(mode)

        if mode == 'TEST':
            self.driver.get(f'https://{settings.USER}:{settings.PASSWORD}@online-dint.ulapr.ru/app/lk/client/index.php?r=loginClient')
        if mode == 'PROD':
            self.driver.get(f'https://roomplan.ru/app/lk/client/index.php?r=loginClient')
    
    def click_register_login_btn(self):
        """Клик по кнопке "Зарегистрироваться" сверху на странице входа"""
        self.wait(locator_register_btn)
        self.find(locator_register_btn).click()

    def click_register_start_btn(self):
        """Клик по кнопке "Зарегистрироваться" после ввода данных"""
        self.wait(locator_register_start_btn)
        self.find(locator_register_start_btn).click()



def get_activation_link() -> str:
    """Извлекает ссылку активации из письма"""
    try:
        mail = imaplib.IMAP4_SSL('imap.yandex.ru', 993)
        mail.login(settings.EMAIL_ICMP, settings.PASSWORD_ICMP)

        for _ in range(5):
            mail.select('inbox')
            status, messages = mail.search(None, '(UNSEEN FROM "RoomPlan")')
            if status != 'OK':
                raise Exception("Ошибка поиска письма")

            if not messages[0]:
                print("Нет непрочитанных писем от RoomPlan")
                time.sleep(2)
                continue
            else:
                break

        if not messages[0]:
            raise Exception("Нет непрочитанных писем от RoomPlan")

        latest_email_id = messages[0].split()[-1]
        status, msg_data = mail.fetch(latest_email_id, '(RFC822)')
        if status != 'OK':
            raise Exception("Ошибка загрузки письма")

        msg = email.message_from_bytes(msg_data[0][1], policy=policy.default)

        # Сохранение HTML-части
        html_content = None
        for part in msg.walk():
            if part.get_content_type() == 'text/html':
                charset = part.get_content_charset() or 'utf-8'
                html_content = part.get_content()
                break

        if html_content:
            soup = BeautifulSoup(html_content, 'html.parser')
            link_texts = []
            
            for a_tag in soup.find_all('a', href=True):
                link_text = a_tag.get_text(strip=True)
                link_texts.append(link_text)
            
            if settings.MODE == "TEST":
                host = "online-dint.ulapr.ru"
                return link_texts[1].replace(host, f"{settings.USER}:{settings.PASSWORD}@{host}")
            else:
                return link_texts[1]
        else:
            raise Exception("HTML-часть письма не найдена")
    except Exception as e:
        print(f"Ошибка: {str(e)}")
    finally:
        if 'mail' in locals():
            mail.logout()