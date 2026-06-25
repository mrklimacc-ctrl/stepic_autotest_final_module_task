from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from typing import Literal

# Ограничиваем тип только теми строками, которые есть в By
ByLocatorStrategy = Literal["css selector", "xpath", "id", "name", "link text", "partial link text", "tag name", "class name"]

class BasePage:
    def __init__(self, browser: WebDriver, url: str, timeout: int = 10):
        self.browser = browser
        self.url = url
        browser.implicitly_wait(timeout)  # Устанавливаем неявное ожидание в timeout секунд

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how: ByLocatorStrategy, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
