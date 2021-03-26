import requests
import datetime


def actualEuroRate():
    url = ('https://api.exchangeratesapi.io/latest?symbols=PLN')
    response = requests.get(url)
    currency = response.text
    cleanValues = currency.replace('{', ' ').replace('}', ' ').replace(':', ','.replace("'", ''))
    exchangeRates = cleanValues.split(',')
    exchangeRatesList = [exchangeRates]
    return print('Aktualny kurs Euro: ' + exchangeRates[2] + 'zł')
    try:
        requests.get('https://api.exchangeratesapi.io/latest?symbols=PLN', timeout=15)
    except requests.exceptions.TimeoutError:
        print('UUUUUU!Trwało to za długo')


def requestResponseTime():
    url = ('https://api.exchangeratesapi.io/latest?symbols=PLN')
    response = requests.get(url)
    responseTime = (response.elapsed.total_seconds() * 1000)
    responseHeadrs = response.headers.get('Date')
    requestsDateTime = responseHeadrs.replace('GMT','')
    return print('Czas wykonania zapytania: ' + str(int(responseTime)) + ' ms' + ' \nData wykonania zapytania: ' + requestsDateTime)


print('--------------------------------------------------------------------------')
actualEuroRate()
requestResponseTime()
print('--------------------------------------------------------------------------')