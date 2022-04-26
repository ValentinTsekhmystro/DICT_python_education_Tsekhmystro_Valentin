import requests


cache = dict()

currency_from = input().lower()
url = f'http://www.floatrates.com/daily/{currency_from}.json'
response = requests.get(url)
json_obj = response.json()

if currency_from != 'usd':
    cache['usd'] = json_obj['usd']['rate']
if currency_from != 'eur':
    cache['eur'] = json_obj['eur']['rate']

while True:
    currency_to = input().lower()
    if currency_to == '':
        break
    amount = float(input())
    print('Checking the cache...')
    if currency_to in cache.keys():
        print('Oh! It is in the cache!')
    else:
        print('Sorry, but it is not in the cache!')
        cache[currency_to] = json_obj[currency_to]['rate']
    print(f'You received {round(amount * cache[currency_to], 2)} {currency_to.upper()}.')