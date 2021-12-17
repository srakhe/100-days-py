from alpha_vantage.foreignexchange import ForeignExchange
import os

fx_obj = ForeignExchange(key=os.environ['ALPHA_API_KEY'])
data = fx_obj.get_currency_exchange_rate(from_currency='CAD', to_currency='INR')
exchange_rate = data[0]['5. Exchange Rate']
from_currency = data[0]['2. From_Currency Name']
to_currency = data[0]['4. To_Currency Name']
print(f'The price of 1 {from_currency} is {exchange_rate} in {to_currency}')
