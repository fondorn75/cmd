import yaml
import time
from testpage import OperationsHelper
import logging

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser, answer_code):
    logging.info("Test 1 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(testdata["username"])
    test_page.enter_pass(testdata["password"])
    test_page.click_login_button()
    test_page.click_about_button()
    time.sleep(testdata['sleep_time'])
    field = test_page.get_about_page_font()
    assert field == answer_code


def test_step2(browser, answer_code2):
    logging.info("Test 2 Starting")
    test_page = OperationsHelper(browser)
    assert test_page.get_answer_from_nikto(testdata['cmd'], answer_code2)




