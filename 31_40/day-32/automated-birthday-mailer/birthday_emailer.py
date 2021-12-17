import datetime as dt
import random
import email_sender

today = dt.datetime.now()
birth_day = int(input('Enter the birthday date: '))
birth_month = int(input('Enter the birthday month: '))
birth_year = int(input('Enter the birthday year: '))
birthday_date = dt.datetime(day=birth_day, month=birth_month, year=birth_year)
if birthday_date.weekday() == today.weekday():
    with open('data/quotes.txt', 'r') as file:
        data = file.readlines()
    random_quote = random.choice(data)
    email_sender.send_email(email_to_send='Subject: It\'s your birthday day today! \n\n' + random_quote)
