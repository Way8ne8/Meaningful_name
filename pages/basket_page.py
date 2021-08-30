from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_in_url()
        # проверки пустоты корзины
        self.should_be_empty_basket()
        self.should_be_text_empty_basket()

    def should_be_basket_in_url(self):
        assert "basket" in self.browser.current_url, "URL don't have word basket"

    # проверки пустоты корзины
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket doesn't empty"

    def should_be_text_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "Basket empty text don't present"

