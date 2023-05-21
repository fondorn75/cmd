import yaml
import requests

with open("settings.yaml") as f:
    user_set = yaml.safe_load(f)

response = requests.post(user_set['url'])
print(response.status_code)
response.encoding = 'utf-8'
print(response.json())

# usertoken = "temp.token"