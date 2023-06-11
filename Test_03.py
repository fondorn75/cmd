# Добавить в задание с REST API ещё один тест, в котором создаётся новый пост,
# а потом проверяется его наличие на сервере по полю «описание».
# Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/gateway/posts
# с передачей параметров title, description, content.

import yaml
import requests

with open("settings.yaml") as f:
    user_set = yaml.safe_load(f)


def new_post(token):
    response = requests.post(user_set['posts'], headers={'X-Auth-Token': token},
                             params={'title': user_set['title'],
                                     'description': user_set['description'],
                                     'content': user_set['content']})
    response.encoding = 'utf-8'
    return response.json()


def my_posts(token):
    response = requests.get(user_set['posts'], headers={'X-Auth-Token': token})
    listDescription = []
    for i in response.json()['data']:
        listDescription.append(i['description'])
    return listDescription


def test_step3(login, description):
    new_post(login)
    assert description in my_posts(login)



