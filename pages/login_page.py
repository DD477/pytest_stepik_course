import re

from .base_page import BasePage
from .locators import BasePageLocators, LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = re.match(
            self.LOGIN_URL_PATTERN, self.browser.current_url
        )
        assert current_url is not None, (
            'current url is not login url'
        )

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), (
            'login form is not presented'
        )

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), (
            'register form is not presented'
        )

    def register_new_user(self, email, password):
        self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_EMAIL
        ).send_keys(email)

        self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_PASSWORD
        ).send_keys(password)

        self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_PASSWORD_REPEAT
        ).send_keys(password)

        self.browser.find_element(
            *LoginPageLocators.REGISTER_SUBMIT
        ).click()

        assert self.is_element_present(*BasePageLocators.USER_ICON), (
            'dont see user icon, perhaps registration not work'
        )
