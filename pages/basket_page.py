from .base_page import BasePage
from .locators import BasketPageLocators
from selenium import webdriver


class BasketPage(BasePage):
    def should_be_login_page(self):
        self.should_be_basket_in_url()
        self.should_be_empty_basket()
        self.should_be_text_empty_basket()

    def should_be_basket_in_url(self):
        assert "basket" in self.browser.current_url, "URL don't have word basket"

    def should_be_empty_basket(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket doesn't empty"

    def should_be_text_empty_basket(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "Basket empty text don't present"

