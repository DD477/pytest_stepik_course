import re

from utills import send_answer_to_stepik, solve_quiz_and_get_code

from .base_page import BasePage
from .locators import ProductPageLocators

LESSON_URL = 'https://stepik.org/lesson/201964/step/2?unit=176022'
CURRENCY = {'Pound': '£'}


class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_to_cart_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_CARD
        )
        add_to_cart_button.click()
        solve_quiz_and_get_code(self.browser)
        self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
        # send_answer_to_stepik(LESSON_URL, self.browser, True)
        self.check_succes_message()

    def check_succes_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
        message = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE
        )
        title_from_message = re.split('\n| был', message.text)[1]
        product_title = self.browser.find_element(
            *ProductPageLocators.PRODUCT_TITLE
        ).text
        assert (
            title_from_message == product_title,
            'Product title and title from success message not equal'
        )
