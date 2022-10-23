from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')


class ProductPageLocators:
    CARD = (By.XPATH, '//div[contains(@class,"basket")]')
    ADD_TO_CARD = (By.XPATH, '//button[@value="Добавить в корзину"]')
    SUCCESS_MESSAGE = (
        By.XPATH, '//div[contains(@class, "alert-success")][1]'
    )
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div[class$="product_main"] h1')
    PRODUCT_PRICE = (
        By.CSS_SELECTOR, 'div[class$="product_main"] p[class^="price"]'
    )
