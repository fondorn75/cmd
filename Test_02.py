import yaml

with open("settings.yaml") as f:
    user_set = yaml.safe_load(f)

usertoken = "temp.token"