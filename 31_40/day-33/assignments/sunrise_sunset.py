import requests

response = requests.get('https://api.sunrise-sunset.org/json?lat=18.5204&lng=73.8567&formatted=1')
print(response.json())
