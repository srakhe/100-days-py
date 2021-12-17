from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, sid, auth):
        self.account_sid = sid
        self.auth_token = auth

    def notify_sms(self, country, price, seats):
        """
        Send a sms notification.
        """
        message = f'Alert for {country}! We have a ticket for INR{price}\nSeats left:{seats}, hurry!'
        client = Client(self.account_sid, self.auth_token)
        client.messages.create(body=message, to='{a number}')
