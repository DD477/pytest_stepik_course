from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # if page have a quiz use is_got_quiz=True
    def add_product_to_cart(self, is_got_quiz=False):
        add_to_cart_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_CARD
        )
        add_to_cart_button.click()
        if is_got_quiz:
            self.solve_quiz_and_get_code()
        self.check_succes_message()

    def check_succes_message(self):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), 'success message not found'
        title_from_message = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE
        ).text
        product_title = self.browser.find_element(
            *ProductPageLocators.PRODUCT_TITLE
        ).text
        assert title_from_message == product_title, (
            'product title and title from success message not equal'
        )

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), 'success message is presented, but should not be'

    def should_disappeared_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), 'success message is not disappeared, but should be'
