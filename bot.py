from twython import Twython
from datetime import date
import os
import data

API_KEY=os.environ["API_KEY"]
API_SECRET=os.environ["API_SECRET"]

ACCESS_TOKEN=os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET=os.environ["ACCESS_TOKEN_SECRET"]

twitter = Twython (API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitter.verify_credentials()

today = date.today()

message = "Heute ist der Tag "

message = message + data.data[today.month-1][today.day-1] + "!"

if len(message) >140:
    message1=message[:135] + "(1/2)"
    twitter.update_status(status=message1)
    message2=message[136:275] + "(2/2)"
    twitter.update_status(status=message2)
else:
    twitter.update_status(status=message)
