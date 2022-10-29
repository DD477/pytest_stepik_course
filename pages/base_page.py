import math
import re

from selenium.common.exceptions import (NoAlertPresentException,
                                        NoSuchElementException,
                                        TimeoutException)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    # login url search regex pattern
    LOGIN_URL_PATTERN = r'.*selenium1py\.pythonanywhere\.com.*\/login\/$'
    # cart url search regex pattern
    CART_URL_PATTERN = r'.*selenium1py\.pythonanywhere\.com.*\/basket\/$'

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(
                self.browser, timeout
            ).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(
                self.browser, timeout, 1, TimeoutException
            ).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        current_url = re.match(
            self.LOGIN_URL_PATTERN, self.browser.current_url
        )
        assert current_url is not None, (
            'current url is not login url'
        )

    def go_to_cart_page(self):
        link = self.browser.find_element(*BasePageLocators.CART_LINK)
        link.click()
        current_url = re.match(
            self.CART_URL_PATTERN, self.browser.current_url
        )
        assert current_url is not None, (
            'current url is not cart url'
        )

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK), 'login link is not visible'

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = re.search(r'\S\d+', alert.text)[0]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            print('Wrong answer')
