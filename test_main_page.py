import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage


@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com'
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.see_that_cart_is_empty()
    cart_page.see_cart_empty_message()
