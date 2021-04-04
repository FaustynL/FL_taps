import requests
import time
import json

url = ('https://api.ratesapi.io/api/latest?base=EUR&symbols=PLN')

def actualEuroRate():
    try:
        response = requests.get(url)
        currency = response.text
        parse = json.loads(currency)
        print('Aktualny kurs Euro: ' + str(parse['rates']['PLN']))
    except requests.exceptions.Timeout:
        print('UUUUUU!Trwało to za długo')


def requestResponseTime():
    response_2 = requests.get(url)
    responseTime = (response_2.elapsed.total_seconds() * 1000)
    responseHeadrs = response_2.headers.get('Date')

    print('Data i godzina: ' + str(responseHeadrs))
    print('Czas wykonania zapytania: ' + str(round(responseTime)) + ' ms')
    print('--------------------------------------')


while True:
    actualEuroRate()
    requestResponseTime()
    time.sleep(15)