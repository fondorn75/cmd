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
    test_page.enter_login("test")
    test_page.enter_pass("test")
    test_page.click_login_button()
    assert test_page.get_error_text() == answer_code


def test_step2(browser, answer_code2):
    logging.info("Test 2 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(testdata["username"])
    test_page.enter_pass(testdata["password"])
    test_page.click_login_button()
    assert test_page.get_header_text() == answer_code2


def test_step3(browser, answer_code3):
    logging.info("Test 3 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.click_new_post_button()
    test_page.enter_title(testdata["title"])
    test_page.enter_description(testdata["description"])
    test_page.enter_content(testdata["content"])
    test_page.click_save_post_button()
    time.sleep(testdata['sleep_time'])
    assert test_page.get_post_header_text() == answer_code3

# Добавить в проект тест по проверке механики работы формы Contact Us на главной странице личного кабинета
# (https://test-stand.gb.ru/).
# Должно проверятся открытие формы, ввод данных в поля, клик по кнопке и появление всплывающего alert.
# Совет: переключиться на alert можно командой alert = self.driver.switch_to.alert
# Вывести текст alert.text
# Формат сдачи:
# В качестве решения принимается написанный нами ранее проект с добавлением шага по проверке
# Contact Us и правками всех необходимых вспомогательных файлов.


def test_step4(browser, answer_code4):
    logging.info("Test 4 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.click_contact_us_button()
    test_page.enter_your_name(testdata['your_name'])
    test_page.enter_your_email(testdata['your_email'])
    test_page.enter_your_content(testdata['your_content'])
    test_page.click_send_contact_us_button()
    time.sleep(testdata['sleep_time'])
    assert test_page.get_alert_text() == answer_code4
