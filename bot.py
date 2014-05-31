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
    if len(message) > 140:
        last = 0
        i = 0
        while (i*134 < len(message)):
            i += 1
            start = last
            # Don't cut the last word of the last message out
            if ((len(message) - i*134) > 0):
                last = message[:(i*134)].rfind(" ")
            else:
                last = len(message)
            messages.append(message[start:last])
            # Skip space
            last += 1
        for (i, string) in enumerate(messages):
            messages[i] += " (" + str(i+1) + "/" + str(len(messages)) + ")"
    else:
        messages.append(message)
    return messages


if __name__ == "__main__":
    main()
