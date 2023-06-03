from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml
import requests

with open("locators.yaml") as f:
    locators = yaml.safe_load(f)

with open("testdata.yaml") as f2:
    user_set = yaml.safe_load(f2)


class TestSearchLocators:
    ids = dict()
    for i in locators['xpath'].keys():
        ids[i] = (By.XPATH, locators['xpath'][i])
    for i in locators['css'].keys():
        ids[i] = (By.CSS_SELECTOR, locators['css'][i])


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.debug(f"Send {word} to element {TestSearchLocators.ids['LOCATOR_LOGIN_FIELD']}")
        login_field = self.find_element(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'])
        if login_field:
            login_field.clear()
            login_field.send_keys(word)
        else:
            logging.error('Field Login not found')

    def enter_pass(self, word):
        logging.debug(f"Send {word} to element {TestSearchLocators.ids['LOCATOR_PASS_FIELD']}")
        password_field = self.find_element(TestSearchLocators.ids['LOCATOR_PASS_FIELD'])
        if password_field:
            password_field.clear()
            password_field.send_keys(word)
        else:
            logging.error('Field Password not found')

    def click_login_button(self):
        logging.debug("Click login button")
        btn = self.find_element(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'])
        if btn:
            btn.click()
        else:
            logging.error('Button Login not found')

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'], time=3)
        if error_field:
            text = error_field.text
            logging.debug(f"We find '{text}' in error field {TestSearchLocators.ids['LOCATOR_ERROR_FIELD']}")
            return text
        else:
            logging.error('Error text not found')
            return None

    def get_header_text(self):
        header_field = self.find_element(TestSearchLocators.ids['LOCATOR_HEADER_LABEL'], time=3)
        if header_field:
            text = header_field.text
            logging.debug(f"We find '{text}' in error field {TestSearchLocators.ids['LOCATOR_HEADER_LABEL']}")
            return text
        else:
            logging.error('Error Header not found')
            return None

    def click_new_post_button(self):
        logging.debug("Click new post button")
        btn = self.find_element(TestSearchLocators.ids['LOCATOR_NEW_POST_BTN'])
        if btn:
            btn.click()
        else:
            logging.error('Error click new post button')

    def enter_title(self, word):
        logging.debug(f"Send {word} to element {TestSearchLocators.ids['LOCATOR_TITLE']}")
        title_field = self.find_element(TestSearchLocators.ids['LOCATOR_TITLE'])
        if title_field:
            title_field.clear()
            title_field.send_keys(word)
        else:
            logging.error('Field Title not found')

    def enter_description(self, word):
        logging.debug(f"Send {word} to element {TestSearchLocators.ids['LOCATOR_DESCRIPTION']}")
        description_field = self.find_element(TestSearchLocators.ids['LOCATOR_DESCRIPTION'])
        if description_field:
            description_field.clear()
            description_field.send_keys(word)
        else:
            logging.error('Field Description not found')

    def enter_content(self, word):
        logging.debug(f"Send {word} to element {TestSearchLocators.ids['LOCATOR_CONTENT']}")
        content_field = self.find_element(TestSearchLocators.ids['LOCATOR_CONTENT'])
        if content_field:
            content_field.clear()
            content_field.send_keys(word)
        else:
            logging.error('Field Content not found')

    def click_save_post_button(self):
        logging.debug("Click save post button")
        btn = self.find_element(TestSearchLocators.ids['LOCATOR_SAVE_POST_BTN'])
        if btn:
            btn.click()
        else:
            logging.error('Error click save post button')

    def get_post_header_text(self):
        header_field = self.find_element(TestSearchLocators.ids['LOCATOR_HEADER_FIELD'], time=3)
        if header_field:
            text = header_field.text
            logging.debug(f"We find '{text}' in error field {TestSearchLocators.ids['LOCATOR_HEADER_FIELD']}")
            return text
        else:
            logging.error('Error Post header not found')
            return None

    def click_contact_us_button(self):
        logging.debug("Click contact us button")
        btn = self.find_element(TestSearchLocators.ids['LOCATOR_CONTACT_US'])
        if btn:
            btn.click()
        else:
            logging.error('Error. Button Contact Us not found')

    def enter_your_name(self, word):
        logging.debug(f"Enter {word} in field {TestSearchLocators.ids['LOCATOR_YOUR_NAME']}")
        your_name_field = self.find_element(TestSearchLocators.ids['LOCATOR_YOUR_NAME'])
        if your_name_field:
            your_name_field.clear()
            your_name_field.send_keys(word)
        else:
            logging.error('Field Your Name not found')

    def enter_your_email(self, word):
        logging.debug(f"Enter {word} in field {TestSearchLocators.ids['LOCATOR_YOUR_EMAIL']}")
        your_email_field = self.find_element(TestSearchLocators.ids['LOCATOR_YOUR_EMAIL'])
        if your_email_field:
            your_email_field.clear()
            your_email_field.send_keys(word)
        else:
            logging.error('Field Your Email not found')

    def enter_your_content(self, word):
        logging.debug(f"Enter {word} in field {TestSearchLocators.ids['LOCATOR_YOUR_CONTENT']}")
        your_content_field = self.find_element(TestSearchLocators.ids['LOCATOR_YOUR_CONTENT'])
        if your_content_field:
            your_content_field.clear()
            your_content_field.send_keys(word)
        else:
            logging.error('Field Your Content not found')

    def click_send_contact_us_button(self):
        logging.debug("Click send contact us button")
        btn = self.find_element(TestSearchLocators.ids['LOCATOR_CONTACT_US_BTN'])
        if btn:
            btn.click()
        else:
            logging.error('Button Send contact us not found')

    def get_alert_text(self):
        try:
            text = self.driver.switch_to.alert.text
            logging.debug(f"We find '{text}' in alert field")
            return text
        except:
            logging.error('Error. Text Alert not found')
            return None

    def get_not_me_posts(self, token):
        try:
            response = requests.get(user_set['posts'], headers={'X-Auth-Token': token}, params={'owner': 'notMe', 'page': 1})
            listTitle = []
            for i in response.json()['data']:
                listTitle.append(i['title'])
            return listTitle
        except:
            logging.error('Dont get list not me posts')
            return None

    def create_new_post(self, token):
        try:
            response = requests.post(user_set['posts'], headers={'X-Auth-Token': token},
                                     params={'title': user_set['title'],
                                             'description': user_set['description'],
                                             'content': user_set['content']})
            response.encoding = 'utf-8'
            return response.json()
        except:
            logging.error('Error. Dont create new post')
            return None

    def get_my_posts(self, token):
        try:
            response = requests.get(user_set['posts'], headers={'X-Auth-Token': token})
            listDescription = []
            for i in response.json()['data']:
                listDescription.append(i['description'])
            return listDescription
        except:
            logging.error('Error. Dont get list my posts')
            return None
