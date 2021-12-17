import requests
import json

INR_response = requests.get('https://api.coinbase.com/v2/prices/spot?currency=INR')
print(json.loads(INR_response.text))

currencies = requests.get('https://api.coinbase.com/v2/currencies')
print(json.loads(currencies.text))

exchange_rates = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=INR')
print(json.loads(exchange_rates.text))

buy_price = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy')
print(json.loads(buy_price.text))

sell_price = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell')
print(json.loads(sell_price.text))
