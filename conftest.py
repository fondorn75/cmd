import pytest
import yaml
import requests

with open("settings.yaml") as f:
    user_set = yaml.safe_load(f)


@pytest.fixture()
def right_word():
    return "колбаса"


@pytest.fixture()
def wrong_word():
    return 'калбаса'


@pytest.fixture()
def login():
    response = requests.post(user_set['url'], data={'username': user_set['username'], 'password': user_set['password']})
    response.encoding = 'utf-8'
    return response.json()['token']


@pytest.fixture()
def search_text():
    return 'Игуана'


@pytest.fixture()
def description():
    return 'New post for pytest in python'
