import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser: WebDriver):
        main_page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        main_page.open()                      # открываем страницу       
        main_page.go_to_login_page() # переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)  # Создаем объект LoginPage с url текущей страницы после перехода по ссылке
        login_page.should_be_login_page()  # проверяем, что оказались на странице логина


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_goods()
    basket_page.should_be_text_about_empty_basket()


