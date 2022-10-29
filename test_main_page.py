import pytest

from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    LINK = 'http://selenium1py.pythonanywhere.com'

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, self.LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(
        self, browser
    ):
        page = MainPage(browser, self.LINK)
        page.open()
        page.go_to_cart_page()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.see_that_cart_is_empty()
        cart_page.see_cart_empty_message()
