from config_handler import ConfigHandler
import smtplib


class EmailNotifier:

    def __init__(self):
        self.config_data = ConfigHandler()
        self.gmail_smtp_server = None
        self.gmail_smtp_port = None
        self.sender_email = None
        self.sender_email_pass = None
        self.gmail_smtp_server, self.gmail_smtp_port, self.sender_email, self.sender_email_pass = self.config_data.get_email_data()

    def send_emails(self, name, receiver, from_city, to_city, deal_price, deal_date):
        """
        Function:
        Send an email notification.
        Params:
        receiver: str
            Receiver's email address
        """
        with smtplib.SMTP(str(self.gmail_smtp_server), int(self.gmail_smtp_port)) as connection:
            connection.starttls()
            connection.login(user=self.sender_email, password=self.sender_email_pass)
            connection.sendmail(from_addr=self.sender_email,
                                to_addrs=receiver,
                                msg=f'Subject: Deal found! {from_city} to {to_city}!\n\nHi {name}! The deal price is, INR {deal_price} only and it is available on {deal_date}')
