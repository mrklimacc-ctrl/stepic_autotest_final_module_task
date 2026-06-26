from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

class BasePage:
    def __init__(self, browser: WebDriver, url: str, timeout: int = 10):
        self.browser = browser
        self.url = url
        browser.implicitly_wait(timeout)  # Устанавливаем неявное ожидание в timeout секунд

    def open(self):
        self.browser.get(self.url)

    # Метод для проверки наличия элемента на странице
    def is_element_present(self, how: str, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    
    # Метод для проверки, что элемент кликабелен
    def is_element_clickable(self, how: str, what: str) -> bool:
        try:
            self.browser.find_element(how, what).is_enabled()
        except NoSuchElementException:
            return False
        return True
    
    # Метод для получения текста элемента на странице или None, если элемент не найден
    def get_element_text(self, how: str, what: str) -> str | None:
        try:
            element = self.browser.find_element(how, what)
            return element.text
        except NoSuchElementException:
            return None
        
    # Метод для получения СЫРОГО текста элемента на странице или None, если элемент не найден
    def get_raw_element_text(self, how: str, what: str) -> str | None:
        try:
            element = self.browser.find_element(how, what)
            return element.get_attribute("textContent")
        except NoSuchElementException:
            return None

    # Метод проверки, что элекмента НЕТ на странице заданное время
    def is_not_element_present(self, how: str, what: str, timeout : int = 4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        
        return False

    # Метод проверки, что элемент исчезает со страницы
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # Метод для решения математической задачи в алерте и получения кода
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
