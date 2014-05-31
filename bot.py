from twython import Twython
from datetime import date
import os
from data import data

def main():
    API_KEY=os.environ["API_KEY"]
    API_SECRET=os.environ["API_SECRET"]

    ACCESS_TOKEN=os.environ["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET=os.environ["ACCESS_TOKEN_SECRET"]

    twitter = Twython (API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    twitter.verify_credentials()

    today = date.today()

    message = "Heute ist der Tag "

    message = message + data[today.month-1][today.day-1] + "!"

    for status in split_message(message):
        twitter.update_status(status=status)


def split_message(message):
    messages = []
    if len(message) >140:
        message1=message[:135] + "(1/2)"
        messages.append(message1)
        message2=message[136:275] + "(2/2)"
        messages.append(message2)
    else:
        messages.append(message)
    return messages


if __name__ == "__main__":
    main()
