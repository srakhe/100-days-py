import os
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime, timedelta
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ['ALPHA_API_KEY']
NEWS_API_KEY = os.environ['NEWS_API_KEY']
account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_AUTH']


# STEP 2: Use https://newsapi.org
# TODO Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news(day):
    url = 'https://newsapi.org/v2/everything'
    params = {"q": COMPANY_NAME, "from": day, "apiKey": NEWS_API_KEY, "sortBy": "relevancy", "pageSize": 3}
    response = requests.get(str(url), params=params)
    news_data = response.json()
    articles = news_data['articles']
    news = ''
    for article in articles:
        headline = article['title']
        brief = article['description']
        news += f'Headline: {headline} \n Brief: {brief}\n'
    return news


# STEP 3: Use https://www.twilio.com
# TODO Send a separate message with the percentage change and each article's title and description to your phone number.
def send_message(change, news):
    client = Client(account_sid, auth_token)
    if change > 0:
        body = f'{STOCK}: 🟢 {change}%\n' + news
    else:
        body = f'{STOCK}: 🔴 {change}%\n' + news
    client.messages.create(body=body, to='{a number}')


# STEP 1: Use https://www.alphavantage.co
# TODO When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
ts_obj = TimeSeries(key=STOCK_API_KEY)
trade_data, trade_meta_data = ts_obj.get_daily(STOCK)
day_one = None
day_two = None
if 1 <= (datetime.today().date() - timedelta(days=1)).isoweekday() <= 5:
    day_one = datetime.today().date() - timedelta(days=1)
    # If yesterday was monday then previous day for it should be friday and not sunday
    if day_one.isoweekday() == 1:
        day_two = day_one - timedelta(days=3)
    else:
        day_two = day_one - timedelta(days=1)

day_one_trade_data = trade_data[str(day_one)]
day_two_trade_data = trade_data[str(day_two)]

close_price_day_one = eval(day_one_trade_data['4. close'])
close_price_day_two = eval(day_two_trade_data['4. close'])

perc = ((close_price_day_one - close_price_day_two) / close_price_day_one) * 100

if abs(perc) >= 5:
    news = get_news(str(day_one))
    send_message(change=perc, news=news)
