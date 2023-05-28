import yaml
from testpage import OperationsHelper

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser, answer_code):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == answer_code


def test_step2(browser, answer_code2):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["username"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    assert testpage.get_header_text() == answer_code2


def test_step3(browser, answer_code3):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.click_new_post_button()
    testpage.enter_title(testdata["title"])
    testpage.enter_description(testdata["description"])
    testpage.enter_content(testdata["content"])
    testpage.click_save_post_button()
    assert testpage.get_post_header_text() == answer_code3

