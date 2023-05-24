import yaml
from module import Site
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


def test_step1(x_selector1, x_selector2, btn_selector, x_selector3, answer_code):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn = site.find_element("css", btn_selector)
    btn.click()
    err_label = site.find_element("xpath", x_selector3)
    assert err_label.text == answer_code


def test_step2(x_selector1, x_selector2, btn_selector, x_selector4, answer_code2):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata["username"])
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata["password"])
    btn = site.find_element("css", btn_selector)
    btn.click()
    header_label = site.find_element("xpath", x_selector4)
    assert header_label.text == answer_code2


def test_step3(x_selector5, title, description, content, btn_save, x_selector6, answer_code3):
    time.sleep(testdata["sleep_time"])
    btn2 = site.find_element("id", x_selector5)
    btn2.click()
    time.sleep(testdata["sleep_time"])
    input1 = site.find_element("xpath", title)
    input1.send_keys(testdata["title"])
    input2 = site.find_element("xpath", description)
    input2.send_keys(testdata["description"])
    input3 = site.find_element("xpath", content)
    input3.send_keys(testdata["content"])
    time.sleep(testdata["sleep_time"])
    btn = site.find_element("xpath", btn_save)
    btn.click()
    time.sleep(testdata["sleep_time"])
    header_label = site.find_element("xpath", x_selector6)
    assert header_label.text == answer_code3
    site.close()

