import datetime as dt
import random
import email_sender
import pandas

birth_data = pandas.read_csv('data/birthdays.csv')

today = dt.datetime.now()

for this_tuple in birth_data.itertuples():
    birth_day = this_tuple.day
    birth_month = this_tuple.month
    birth_year = this_tuple.year
    send_to_email = this_tuple.email
    birth_name = this_tuple.name

    birthday = dt.datetime(day=birth_day, month=birth_month, year=birth_year)

    if today.day == birthday.day and today.month == birthday.month:
        with open('data/email.txt', 'r') as file:
            birthdays_data = file.read()
        birthdays_data = birthdays_data.replace('[NAME]', birth_name)
        with open('data/quotes.txt', 'r') as file:
            quotes_data = file.readlines()
        random_quote = random.choice(quotes_data)
        birthdays_data = birthdays_data.replace('[QUOTE]', random_quote)
        email_message = 'Subject: Happy Birthday ' + birth_name + '!!\n\n' + birthdays_data
        email_sender.send_email(email_to_send=email_message, receiver_email=send_to_email)
