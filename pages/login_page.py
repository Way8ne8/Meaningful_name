from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL don't have word login"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Net formy logina"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_LINK), "Net formy registracii"

    def register_new_user(self, email, password):
        browser = self.browser
        input_email = browser.find_element_by_css_selector('#id_registration-email')
        input_email.send_keys(email)
        input_psw1 = browser.find_element_by_css_selector('#id_registration-password1')
        input_psw1.send_keys(password)
        input_psw2 = browser.find_element_by_css_selector('#id_registration-password2')
        input_psw2.send_keys(password)
        submit_button = browser.find_element_by_css_selector('#register_form > button')
        submit_button.click()