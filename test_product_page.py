import pytest
import time

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

# pytest -v --tb=line --language=en -m need_review test_product_page.py

@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "Password"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    # Проверяем, что нет сообщения об успехе без добавления в карзину
    @pytest.mark.new
    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        product_page = ProductPage(browser, link)
        product_page.open()
        
        product_page.should_not_be_success_message()

    @pytest.mark.new
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        product_page = ProductPage(browser, link)
        product_page.open()
        
        product_page.should_be_product_page()  # Проверяем, что на странице товара присутствуют все необходимые элементы
        product_page.should_be_product_name_and_price_match("Coders at Work", "£19.99")  # Проверяем, что название и цена товара на странице совпадают с ожидаемыми значениями
        product_page.add_product_to_basket()  # Добавляем товар в корзину
        # product_page.solve_quiz_and_get_code() # Решаем задачку в алерте и получаем код
        product_page.should_be_product_name_match_in_basket("Coders at Work")
        product_page.should_be_basket_total_price_match("£19.99")  # Проверяем, что общая стоимость корзины совпадает с ценой товара

def test_guest_cant_see_success_message(browser, link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()  # Проверяем, что на странице товара присутствуют все необходимые элементы
    product_page.should_be_product_name_and_price_match("Coders at Work", "£19.99")  # Проверяем, что название и цена товара на странице совпадают с ожидаемыми значениями
    product_page.add_product_to_basket()  # Добавляем товар в корзину
    # product_page.solve_quiz_and_get_code() # Решаем задачку в алерте и получаем код
    product_page.should_be_product_name_match_in_basket("Coders at Work")
    product_page.should_be_basket_total_price_match("£19.99")  # Проверяем, что общая стоимость корзины совпадает с ценой товара

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
    product_page = ProductPage(browser, link)
    product_page.open()
    # product_page.add_product_to_basket()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_goods()
    basket_page.should_be_text_about_empty_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()



# Проверяем, что нет сообщения об успехе после добавления в карзину
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
@pytest.mark.xfail(reason="It's correct")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()

# Проверяем, что сообщение об успехе исчезает
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
@pytest.mark.xfail(reason="It's correct")
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_disappear()

