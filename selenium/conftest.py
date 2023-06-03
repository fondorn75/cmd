import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import requests

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

browser = testdata["browser"]


@pytest.fixture()
def answer_code():
    return "401"


@pytest.fixture()
def answer_code2():
    return f'Hello, {testdata["username"]}'


@pytest.fixture()
def answer_code3():
    return "Hello World"


@pytest.fixture()
def answer_code4():
    return "Form successfully submitted"


@pytest.fixture(scope="session")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def search_text():
    return 'test_test_test_test_test_test_test_test_'


@pytest.fixture()
def description():
    return 'New post for pytest in python'


@pytest.fixture()
def login():
    response = requests.post(testdata['url'], data={'username': testdata['username'], 'password': testdata['password']})
    response.encoding = 'utf-8'
    return response.json()['token']
