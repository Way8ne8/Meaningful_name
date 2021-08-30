from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time


link_main_page = "http://selenium1py.pythonanywhere.com/"
link_product_page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link_login_page = "http://selenium1py.pythonanywhere.com/accounts/login/"

@pytest.mark.test_basket_guest
class TestBasketGuest():
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        link = link_product_page
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()

    @pytest.mark.need_review
    def test_guest_can_go_to_basket_from_product_page(self, browser):
        link = link_product_page
        page = BasePage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()

    def test_guest_can_go_to_basket_from_main_page(self, browser):
        link = link_main_page
        page = BasePage(browser, link)
        page.open()
        page.go_to_basket_page()

    @pytest.mark.xfail(reason="так надо")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = link_product_page
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="так надо")
    def test_guest_message_disappeared_after_adding_product_to_basket(self, browser):
        link = link_product_page
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_disappeare_element()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = link_product_page
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = link_product_page
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

@pytest.mark.test_basket_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = link_login_page
        email = str(time.time()) + "@fakemail.org"
        psw = "1qazwsxedc"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, psw)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = link_product_page
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = link_product_page
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
