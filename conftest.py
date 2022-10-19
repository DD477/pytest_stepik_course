import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Change page language')
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


def create_custom_webdriver(browser_name, language):
    match browser_name:
        case 'chrome':
            options = Options()
            options.add_experimental_option(
                'prefs', {'intl.accept_languages': language}
            )
            return webdriver.Chrome(options=options)
        case 'firefox':
            options = webdriver.FirefoxOptions()
            options.set_preference('intl.accept_languages', language)
            return webdriver.Firefox(options=options)
        case _:
            raise pytest.UsageError(
                '--browser_name should be chrome or firefox'
            )


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    browser = create_custom_webdriver(browser_name, language)
    yield browser
    browser.quit()
