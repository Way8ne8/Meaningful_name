from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "В url не содержит 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Форма для логина отсутствует"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_LINK), "Форма регистрации отсутствует"

    def register_new_user(self, email, password):
        browser = self.browser
        input_email = browser.find_element_by_css_selector(LoginPageLocators.INPUT_EMAIL)
        input_email.send_keys(email)
        input_psw1 = browser.find_element_by_css_selector(LoginPageLocators.INPUT_PSW1)
        input_psw1.send_keys(password)
        input_psw2 = browser.find_element_by_css_selector(LoginPageLocators.INPUT_PSW2)
        input_psw2.send_keys(password)
        submit_button = browser.find_element_by_css_selector(LoginPageLocators.REG_SUBMIT_BUTTON)
        submit_button.click()