from selenium.common.exceptions import TimeoutException

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_goods(self):
        assert self.is_not_element_present(*BasketPageLocators.TITLE_OF_NOT_EMPTY_BASKET), "Basket is not empty!"

    def should_be_text_about_empty_basket(self):
        assert self.is_any_text(), "There is no text"

    def is_any_text(self):
        is_text = self.is_element_present(*BasketPageLocators.TEXT_IN_BASKET)
        if is_text and self.is_empty():
            text = self.browser.find_element(*BasketPageLocators.TEXT_IN_BASKET).text
            if text != '':
                return True
        return False
    
    def is_empty(self):
        try:
            self.should_not_be_goods()
        except: 
            TimeoutException
            return False
        return True