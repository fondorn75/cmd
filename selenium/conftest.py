import pytest
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def btn_selector():
    return "button"


@pytest.fixture()
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def answer_code():
    return "401"


@pytest.fixture()
def x_selector4():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def answer_code2():
    return f'Hello, {testdata["username"]}'


@pytest.fixture()
def x_selector5():
    return "create-btn"


@pytest.fixture()
def title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def description():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def btn_save():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""


@pytest.fixture()
def x_selector6():
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture()
def answer_code3():
    return "Hello World"

