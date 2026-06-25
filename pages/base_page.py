from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, browser: WebDriver, url: str, timeout: int = 10):
        self.browser = browser
        self.url = url
        browser.implicitly_wait(timeout)  # Устанавливаем неявное ожидание в timeout секунд

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how: str, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
