import pytest
from faker import Faker

from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

FALLING_REASON = 'it will be fixed sometimes'
PRODUCT_LINK = (
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
)

@pytest.mark.need_review
@pytest.mark.parametrize('offer', [
    pytest.param(i, marks=pytest.mark.xfail(i == 7, reason=FALLING_REASON)
                 ) for i in range(10)
])
def test_guest_can_add_product_to_basket(browser, offer):
    link = (
        'http://selenium1py.pythonanywhere.com/ru/'
        f'catalogue/coders-at-work_207/?promo=offer{offer}'
    )
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart(is_got_quiz=True)


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.see_cart_empty_message()


@pytest.mark.guest_add_to_cart
class TestGuestAddToCartFromProductPage:
    @pytest.mark.xfail(reason=FALLING_REASON)
    def test_guest_cant_see_success_message_after_adding_product_to_cart(
        self, browser
    ):
        page = ProductPage(browser, PRODUCT_LINK)
        page.open()
        page.add_product_to_cart()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, PRODUCT_LINK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason=FALLING_REASON)
    def test_success_message_disappeared_after_adding_product_to_cart(
        self, browser
    ):
        page = ProductPage(browser, PRODUCT_LINK)
        page.open()
        page.add_product_to_cart()
        page.should_disappeared_success_message()


@pytest.mark.user_add_to_cart
class TestUserAddToCartFromProductPage:
    LOGIN_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'

    # this fixture only for a training, it's a bad praxis
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, self.LOGIN_LINK)
        login_page.open()
        # library for data generation
        f = Faker()
        login_page.register_new_user(f.email(), f.password())

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, PRODUCT_LINK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT_LINK)
        page.open()
        page.add_product_to_cart()
