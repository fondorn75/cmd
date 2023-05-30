from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_HEADER_LABEL = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_NEW_POST_BTN = (By.ID, "create-btn")
    LOCATOR_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_POST_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_HEADER_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_US = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_YOUR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_YOUR_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_YOUR_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find '{text}' in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_header_text(self):
        header_field = self.find_element(TestSearchLocators.LOCATOR_HEADER_LABEL, time=3)
        text = header_field.text
        logging.info(f"We find '{text}' in error field {TestSearchLocators.LOCATOR_HEADER_LABEL[1]}")
        return text

    def click_new_post_button(self):
        logging.info("Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_BTN).click()

    def enter_title(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_TITLE[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_TITLE)
        login_field.clear()
        login_field.send_keys(word)

    def enter_description(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_DESCRIPTION[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION)
        login_field.clear()
        login_field.send_keys(word)

    def enter_content(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTENT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT)
        login_field.clear()
        login_field.send_keys(word)

    def click_save_post_button(self):
        logging.info("Click save post button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()

    def get_post_header_text(self):
        header_field = self.find_element(TestSearchLocators.LOCATOR_HEADER_FIELD, time=3)
        text = header_field.text
        logging.info(f"We find '{text}' in error field {TestSearchLocators.LOCATOR_HEADER_FIELD[1]}")
        return text

    def click_contact_us_button(self):
        logging.info("Click contact us button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US).click()

    def enter_your_name(self, word):
        logging.info(f"Enter {word} in field {TestSearchLocators.LOCATOR_YOUR_NAME[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME)
        login_field.clear()
        login_field.send_keys(word)

    def enter_your_email(self, word):
        logging.info(f"Enter {word} in field {TestSearchLocators.LOCATOR_YOUR_EMAIL[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL)
        login_field.clear()
        login_field.send_keys(word)

    def enter_your_content(self, word):
        logging.info(f"Enter {word} in field {TestSearchLocators.LOCATOR_YOUR_CONTENT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_CONTENT)
        login_field.clear()
        login_field.send_keys(word)

    def click_send_contact_us_button(self):
        logging.info("Click send contact us button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def get_alert_text(self):
        text = self.driver.switch_to.alert.text
        logging.info(f"We find '{text}' in alert field")
        return text
