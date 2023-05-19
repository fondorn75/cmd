from zeep import Client, Settings
import yaml

with open('settings.yaml') as f:
    temp = yaml.safe_load(f)

settings = Settings(strict=False)
client = Client(wsdl=temp['wsdl'], settings=settings)


def checkText(word):
    return client.service.checkText(word, lang='ru')[0]['s']


if __name__ == '__main__':
    print(checkText('калбаса'))
