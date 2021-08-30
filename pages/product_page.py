from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_LINK), "Нет кнопки Добавить в корзину"
        self.browser.find_element(*ProductPageLocators.ADD_LINK).click()
        self.check_messages()

    def check_messages(self):
        assert self.is_element_present(*ProductPageLocators.ADD_SUCC_MESSAGE), "Нет сообщения об успешном добавлении"
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MESSAGE), "Нет сообщения о стоимости в корзине"
        assert self.browser.find_element(*ProductPageLocators.NAME_IN_BASKET).text == self.browser.find_element(
            *ProductPageLocators.NAME_PRODUCT).text, \
            "Название на странице и в корзине не совпадают"
        assert self.browser.find_element(*ProductPageLocators.VALUE_IN_MESSAGE).text == self.browser.find_element(
            *ProductPageLocators.VALUE_ON_PAGE).text, \
            "Неверная цена в сообщении"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_SUCC_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeare_element(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_SUCC_MESSAGE), \
            "Success message is presented, but should not be"
