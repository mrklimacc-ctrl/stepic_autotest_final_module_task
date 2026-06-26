from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    pass

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    AVELABLE_PRODUCT = (By.CSS_SELECTOR, ".instock.availability .icon-ok")
    REWIEW_PRODUCT = (By.CSS_SELECTOR, "#write_review")
    HEADER_PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert")