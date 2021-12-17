import smtplib
import os


def send_email(receiver='', product_name='', deal_price=None, url=''):
    gmail_smtp_server = os.environ['GMAIL_SMTP_SERVER']
    gmail_smtp_port = os.environ['GMAIL_SMTP_PORT']
    gmail_pass = os.environ['GMAIL_PASSWORD']

    with smtplib.SMTP(str(gmail_smtp_server), int(gmail_smtp_port)) as connection:
        connection.starttls()
        connection.login(user='sender@gmail.com', password=gmail_pass)
        connection.sendmail(from_addr='sender@gmail.com',
                            to_addrs=receiver,
                            msg=f'Subject: Deal found for {product_name}! \n\n{deal_price} \nCheck it out now! {url}')
