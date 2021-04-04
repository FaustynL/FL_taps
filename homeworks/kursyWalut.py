import requests
import time
import json

url = 'https://api.ratesapi.io/api/latest?base=EUR&symbols=PLN'


def currency():
    try:
        r = requests.get(url)
        data = r.text
        parse = json.loads(data)
        print('Kurs Euro: ' + str(parse['rates']['PLN']))
    except requests.exceptions.Timeout:
        print('Serwis chwilowo niedostępny')


def wrapper():
    response = requests.get(url)
    req_time = response.headers.get('Date')
    responseTime = (response.elapsed.total_seconds() * 1000)

    print('Data i godzina: ' + str(req_time))
    print('Czas wykonania zapytania: ' + str(round(responseTime)) + ' ms')
    print('----------------------')


while True:
    currency()
    wrapper()
    time.sleep(15)