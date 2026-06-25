
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage

# pytest -v --tb=line --language=en test_main_page.py

def test_guest_can_go_to_login_page(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    page.should_be_login_link()      # проверяем, что есть ссылка на логин