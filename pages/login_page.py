from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # убрать эту хрень
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
