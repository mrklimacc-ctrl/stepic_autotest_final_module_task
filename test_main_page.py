
from selenium.webdriver.remote.webdriver import WebDriver
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

# pytest -v --tb=line --language=en test_main_page.py

def test_guest_can_go_to_login_page(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    main_page.open()                      # открываем страницу       
    main_page.go_to_login_page() # переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)  # Создаем объект LoginPage с url текущей страницы после перехода по ссылке
    login_page.should_be_login_page()  # проверяем, что оказались на странице логина