from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        # self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

