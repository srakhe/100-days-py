from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_AUTH']
client = Client(account_sid, auth_token)

message = client.messages.create(body='Hello World', from_=os.environ['TWILIO_SENDER'],
                                 to=os.environ['TWILIO_RECEIVER'])

print(message.sid)
