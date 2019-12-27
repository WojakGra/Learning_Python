import requests
import json

payload = {'format':'json'}

def Convert(currency):
    response = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/'+str(currency), params=payload)
    if response:
        response_json = json.loads(response.text)

        country = response_json['currency']
        code = response_json['code']
        value = str(response_json['rates'][0]['mid'])

        print('1 ' + code + ' (' + country + ') to ' + value + 'zł')
    else:
        print('An error has occurred.')

def Menu():
        answer = input('Podaj jaką walutę chciałbyś się dowiedzieć (np. USD, EUR, GBP) > ')
        Convert(answer)

Menu()