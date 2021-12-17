import configparser
import smtplib


def send_email(message_from_config=False, email_to_send='', receiver_email=''):
    """
    Function:
    Send an email
    Params:
    message_from_config: Bool
        Read data from config file if True
    email_to_send: str
        Data to send as email (Prefix with 'Subject:')
    """
    # Read data from config file
    config = configparser.ConfigParser()
    config.read('data/config.ini')
    # Get required data
    gmail_server = config['Gmail Server Data']
    gmail_data = config['Gmail Data']
    gmail_smtp_server = gmail_server.get('smtp_address')
    gmail_server_port = gmail_server.get('smtp_port')
    sender_email = gmail_data.get('sender')
    sender_pass = gmail_data.get('sender_pass')

    if message_from_config:
        email_content_data = config['Email Content']
        email_subject = email_content_data.get('subject')
        email_content = email_content_data.get('content')
        email_to_send = 'Subject: ' + str(email_subject) + '\n\n' + str(email_content)
        receiver_email = gmail_data.get('receiver')

    with smtplib.SMTP(str(gmail_smtp_server), int(gmail_server_port)) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_pass)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=receiver_email,
                            msg=email_to_send)
    print('Email has been sent!')
