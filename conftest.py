import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose language")

@pytest.fixture
def browser():
    print("\nstart Chrome")
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    yield browser
    print("\nend Chrome")
    browser.quit()


@pytest.fixture
def language(request):
    language = request.config.getoption("language")
    return language