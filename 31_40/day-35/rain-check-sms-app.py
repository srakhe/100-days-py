import requests
from datetime import datetime
from twilio.rest import Client
import os

app_id = os.environ['WEATHER_APP_ID']

weather_url = 'https://api.openweathermap.org/data/2.5/onecall?lat=51.507351&lon=-0.127758&exclude=current,minutely,daily,alerts&appid=' + app_id
account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_AUTH']

response = requests.get(weather_url)
for item in response.json()['hourly']:
    date_time = item['dt']
    weather = item['weather'][0]['id']
    if int(weather) <= 700:
        print('Rain/Storm is predicted!')
        date = datetime.utcfromtimestamp(date_time).date()
        print('Date: ', date)
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=f'It will rain today {date}, bring an umbrella!', from_='{a number}',
                                         to='{a number}')
