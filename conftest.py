import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# pytest -s -v --language=ru --browser_name=chrome test_items.py
def pytest_addoption(parser):
    # Добавляем опцию для выбора браузера
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    # Добавляем опцию для выбора языка
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru, en, fr, etc.")


@pytest.fixture(scope="function")
def browser(request):
    # Получаем язык из командной строки pytest (например: pytest --language=ru)
    user_language = request.config.getoption("language")
    
    # Получаем имя браузера из командной строки pytest (например: pytest --browser_name=chrome)
    browser_name = request.config.getoption("browser_name")
    
    browser = None
    
    # Открываем браузер в зависимости от выбранного имени браузера и устанавливаем язык
    # Chrome
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    # Firefox
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    
    # Закрываем браузер после завершения тестов
    print("\nquit browser..")
    browser.quit()
