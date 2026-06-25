import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from .pages.product_page import ProductPage
import time

# pytest -s -v --tb=line --language=en test_product_page.py


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()  # Проверяем, что на странице товара присутствуют все необходимые элементы
    product_page.should_be_product_name_and_price_match("Coders at Work", "£19.99")  # Проверяем, что название и цена товара на странице совпадают с ожидаемыми значениями
    product_page.add_product_to_basket()  # Добавляем товар в корзину
    product_page.solve_quiz_and_get_code() # Решаем задачку в алерте и получаем код
    product_page.should_be_product_name_match_in_basket("Coders at Work")
    product_page.should_be_basket_total_price_match("£19.99")  # Проверяем, что общая стоимость корзины совпадает с ценой товара
