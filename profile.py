
import yaml
import requests


with open("settings.yaml") as f:
    user_set = yaml.safe_load(f)


def login():
    response = requests.post(user_set['url'], data={'username': user_set['username'], 'password': user_set['password']})
    response.encoding = 'utf-8'
    return response.json()['token']


def get_user_profile(token):
    response = requests.get(f"{user_set['users']}/616", headers={'X-Auth-Token': token})
    return response.json()['userName']


if __name__ == '__main__':
    print(get_user_profile(login()))