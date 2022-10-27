from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #убрать эту хрень
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        assert self.browser.current_url == link, (
            'current url is not login_url'
        )

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), (
            'login form is not presented'
        )

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), (
            'register form is not presented'
        )
