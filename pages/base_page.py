from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, browser: WebDriver, url: str):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)