import pytest

from pages.product_page import ProductPage


@pytest.mark.skip
@pytest.mark.parametrize('offer', [
    pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='this bug')
                 ) for i in range(10)
])
def test_add_product_to_cart(browser, offer):
    link = (
        'http://selenium1py.pythonanywhere.com/ru/'
        f'catalogue/coders-at-work_207/?promo=offer{offer}'
    )
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()


@pytest.mark.xfail(reason='it will be fixed sometimes')
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = (
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    )
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = (
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    )
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason='it will be fixed sometimes')
def test_message_disappeared_after_adding_product_to_cart(browser):
    link = (
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    )
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_disappeared_success_message()
