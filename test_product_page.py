import pytest

from pages.product_page import ProductPage


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
