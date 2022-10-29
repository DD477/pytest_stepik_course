from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def see_that_cart_is_empty(self):
        content = self.browser.find_elements(*CartPageLocators.CART_CONTENT)
        assert len(content) <= 1, 'cart is not empty'

    def see_cart_empty_message(self):
        empty_cart_message = self.browser.find_element(
            *CartPageLocators.CART_CONTENT
        ).text
        CORRECT_EMPTY_CART_MESSAGE = 'Your basket is empty. Continue shopping'
        assert (
            empty_cart_message == CORRECT_EMPTY_CART_MESSAGE
        ), 'cart empty message is not correct'
