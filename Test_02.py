import yaml
import requests

with open("settings.yaml") as f:
    user_set = yaml.safe_load(f)


def posts(token):
    response = requests.get(user_set['posts'], headers={'X-Auth-Token': token}, params={'owner': 'notMe', 'page': 1})
    listTitle = []
    for i in response.json()['data']:
        listTitle.append(i['title'])
    return listTitle


def test_step2(login, search_text):
    assert search_text in posts(login)

