from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, '#basket_formset')
    BASKET_EMPTY_TEXT = (By.XPATH, "//*[text()[contains(.,'Your basket is empty.')]]")


class LoginPageLocators():
    REG_LINK = (By.CSS_SELECTOR, "#register_form")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_form")
    INPUT_EMAIL = "#id_registration-email"
    INPUT_PSW1 = "#id_registration-password1"
    INPUT_PSW2 = "#id_registration-password2"
    REG_SUBMIT_BUTTON = "#register_form > button"


class ProductPageLocators():
    ADD_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADD_SUCC_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    BASKET_PRICE_MESSAGE = (By.XPATH, "//*[@id='messages']/div[3]/div")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    NAME_IN_BASKET = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    VALUE_ON_PAGE = (By.CSS_SELECTOR, "p.price_color")
    VALUE_IN_MESSAGE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
