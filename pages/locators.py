from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    pass

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#register_form input[type='email']")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTRATION_DOUBLE_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    AVELABLE_PRODUCT = (By.CSS_SELECTOR, ".instock.availability .icon-ok")
    REWIEW_PRODUCT = (By.CSS_SELECTOR, "#write_review")
    HEADER_PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert")

class BasketPageLocators():
    TITLE_OF_NOT_EMPTY_BASKET = (By.CSS_SELECTOR, "body .page .basket-title")
    COLUMN_OF_NOT_EMPTY_BASKET = (By.CSS_SELECTOR, "body .page #content_inner p.col-sm-3")
    TEXT_IN_BASKET = (By.CSS_SELECTOR, "body .page #content_inner p")