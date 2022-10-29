from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
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

    def get_alert(self):
        return self.browser.switch_to.alert

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        # убрать эту хрень
        correct_link = ('http://selenium1py.pythonanywhere.com/'
                        'en-gb/accounts/login/')
        assert self.browser.current_url == correct_link, (
            'current url is not login_url'
        )

    def go_to_cart(self):
        link = self.browser.find_element(*BasePageLocators.CART_LINK)
        link.click()

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK), 'login link is not presented'
