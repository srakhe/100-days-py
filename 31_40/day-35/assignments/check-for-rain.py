import requests
from datetime import datetime
import os

app_id = os.environ['WEATHER_APP_ID']

weather_url = 'https://api.openweathermap.org/data/2.5/onecall?lat=51.507351&lon=-0.127758&exclude=current,minutely,daily,alerts&appid=' + app_id

response = requests.get(weather_url)
for item in response.json()['hourly']:
    date_time = item['dt']
    weather = item['weather'][0]['description']
    if not str(weather).lower().find('rain') == -1 or not str(weather).lower().find('snow') == -1:
        print(weather)
        print('Rain is predicted!')
        print('For time: ', datetime.utcfromtimestamp(date_time))
