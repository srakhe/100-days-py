import datetime as dt
import random
import email_sender

today = dt.datetime.now()
if today.weekday() == 0:
    print('It\'s monday! Time for some motivation.')
    with open('data/quotes.txt', 'r') as file:
        data = file.readlines()
    random_quote = random.choice(data)
    email_sender.send_email(email_to_send='Subject: It\'s your birthday day today! \n\n' + random_quote)
