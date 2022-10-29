from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    CART_LINK = (By.CSS_SELECTOR, 'div[class*="basket"] a[href*="basket"]')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class MainPageLocators:
    ...


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')
    REGISTER_FORM_EMAIL = (By.XPATH, '//input[@name="registration-email"]')
    REGISTER_FORM_PASSWORD = (
        By.XPATH, '//input[@name="registration-password1"]'
    )
    REGISTER_FORM_PASSWORD_REPEAT = (
        By.XPATH, '//input[@name="registration-password2"]'
    )
    REGISTER_SUBMIT = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators:
    CARD = (By.XPATH, '//div[contains(@class,"basket")]')
    ADD_TO_CARD = (By.XPATH, '//button[contains(@class,"add-to-basket")]')
    SUCCESS_MESSAGE = (
        By.XPATH, '//div[contains(@class, "alert-success")][1]//strong'
    )
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div[class$="product_main"] h1')
    PRODUCT_PRICE = (
        By.CSS_SELECTOR, 'div[class$="product_main"] p[class^="price"]'
    )


class CartPageLocators:
    CART_CONTENT = (By.CSS_SELECTOR, '#content_inner p')
