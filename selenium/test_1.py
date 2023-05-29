import yaml
import time
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
    time.sleep(testdata['sleep_time'])
    assert testpage.get_post_header_text() == answer_code3

# Добавить в проект тест по проверке механики работы формы Contact Us на главной странице личного кабинета
# (https://test-stand.gb.ru/).
# Должно проверятся открытие формы, ввод данных в поля, клик по кнопке и появление всплывающего alert.
# Совет: переключиться на alert можно командой alert = self.driver.switch_to.alert
# Вывести текст alert.text
# Формат сдачи:
# В качестве решения принимается написанный нами ранее проект с добавлением шага по проверке
# Contact Us и правками всех необходимых вспомогательных файлов.


def test_step4(browser, answer_code4):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.click_contact_us_button()
    testpage.enter_your_name(testdata['your_name'])
    testpage.enter_your_email(testdata['your_email'])
    testpage.enter_your_content(testdata['your_content'])
    testpage.click_send_contact_us_button()
    time.sleep(testdata['sleep_time'])
    assert testpage.get_alert_text == answer_code4
