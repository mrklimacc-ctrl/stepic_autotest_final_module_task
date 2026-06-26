from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    # Метод для добавления товара в корзину
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    # Проверяем, что на странице товара присутствуют все необходимые элементы
    def should_be_product_page(self):
        self.should_be_add_to_basket_button()
        self.should_be_clickable_add_to_basket_button()
        self.should_be_product_price()
        self.should_be_rewiew_button()
        self.should_be_header_product_name()

    # Проверяем, что название и цена товара на странице совпадают с ожидаемыми значениями
    def should_be_product_name_and_price_match(self, product_name: str, product_price: str):
        page_product_name = self.get_product_name()
        page_product_price = self.get_product_price()
        assert page_product_name == product_name, f"Product name on the page '{page_product_name}' does not match the expected name '{product_name}'"
        assert page_product_price == product_price, f"Product price on the page '{page_product_price}' does not match the expected price '{product_price}'"
    
    def should_be_basket_total_price_match(self, expected_price: str):
        basket_total_price = self.get_basket_total_price()
        assert basket_total_price == expected_price, f"Basket total price '{basket_total_price}' does not match the expected price '{expected_price}'"

    # Проверяем, что кнопка "Добавить в корзину" присутствует на странице
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
    
    # Проверяем, что кнопка "Добавить в корзину" кликабельна, если товар доступен
    def should_be_clickable_add_to_basket_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        if self.is_product_available():
            assert add_button.is_enabled(), "Add to basket button is not clickable"
        # Если товар недоступен, проверяем, что кнопка "Добавить в корзину" не кликабельна
        else:
            assert not add_button.is_enabled(), "Add to basket button is clickable, but product is not available"

    # Проверяем, что на странице товара есть цена
    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), "Product price is not presented"

    # Проверяем, что товар доступен (наличие иконки "в наличии")
    def is_product_available(self):
        return self.is_element_present(*ProductPageLocators.AVELABLE_PRODUCT)
    
    # Проверяем, что на странице товара есть кнопка "Написать отзыв" и на нее можно нажать
    def should_be_rewiew_button(self):
        assert self.is_element_present(*ProductPageLocators.REWIEW_PRODUCT), "Review button is not presented"
        assert self.is_element_clickable(*ProductPageLocators.REWIEW_PRODUCT), "Review button is not clickable"

    # Проверяем, что на странице товара есть заголовок с названием товара
    def should_be_header_product_name(self):
        assert self.is_element_present(*ProductPageLocators.HEADER_PRODUCT_NAME), "Header product name is not presented"

    # Получаем название товара со страницы
    def get_product_name(self) -> str | None:
        return self.get_element_text(*ProductPageLocators.HEADER_PRODUCT_NAME)
    
    # Получаем цену товара со страницы
    def get_product_price(self) -> str | None:
        return self.get_element_text(*ProductPageLocators.PRICE_PRODUCT)
    
    # Получаем общую стоимость корзины со страницы
    def get_basket_total_price(self) -> str | None:
        text = self.get_element_text(*ProductPageLocators.BASKET_TOTAL_PRICE).split(':')[1] # Разделяем текст по символу ":" и берем вторую часть, которая содержит цену корзины
        lines = [line.strip() for line in text.splitlines() if line.strip() != ''] # Разделяем текст на строки, удаляем пустые строки и пробелы в начале и конце каждой строки
        price = lines[0] # Берем первую строку, которая содержит цену корзины
        return price
    
    def should_be_product_name_match_in_basket(self, product_name: str):
        name = self.get_element_text(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        assert product_name == name, f"Expected product name '{product_name}' does not match name in basket '{name}'"

    # Проверка отсутствия на странице сообщения об успешной покупке
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    # Проверка исчезновения со страницы сообщения об успешной покупке в течение заданного времени
    def should_disappear(self, timeout : int = 5):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE, timeout), "Success message didn't disappered"

