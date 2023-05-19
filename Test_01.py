from zeep import Client

client = Client("https://speller.yandex.net/services/spellservice?WSDL")
result = client.service.checktext

assert result == 'Vfvf'
