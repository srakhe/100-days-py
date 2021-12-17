import requests

quote = requests.get('https://api.kanye.rest/')
print(quote.json())
