import requests


currency = input().lower()
url = f'http://www.floatrates.com/daily/{currency}.json'
response = requests.get(url)
json_obj = response.json()
print(json_obj['usd'])
print(json_obj['eur'])