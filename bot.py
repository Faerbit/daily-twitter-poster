from twython import Twython
from datetime import date
import os
from data import data_de

class TwitterBot:

    def __init__(self, message_prefix, data, api_key, api_secret, 
            access_token, access_token_secret):
        self.message_prefix = message_prefix
        self.data = data
        self.twitter = Twython(api_key, api_secret, access_token,
                access_token_secret)
        self.twitter.verify_credentials()

    def post(self, date):
        message = (self.message_prefix + 
            self.data[date.month- 1][date.day-1] + "!")
        for status in self.split_message(message):
            self.twitter.update_status(status=status)


    def split_message(self, message):
        messages = []
        if len(message) > 140:
            last = 0
            # Don't cut the last message
            for i in range(134, len(message)+134, 134):
                start = last
                # Don't cut the last word of the last message out
                if ((len(message) - i) > 0):
                    last = message[:i].rfind(" ")
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


def main():
    API_KEY_DE=os.environ["API_KEY"]
    API_SECRET_DE=os.environ["API_SECRET"]

    ACCESS_TOKEN_DE=os.environ["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET_DE=os.environ["ACCESS_TOKEN_SECRET"]

    de_bot = TwitterBot("Heute ist der Tag ", data_de, API_KEY_DE,
            API_SECRET_DE, ACCESS_TOKEN_DE, ACCESS_TOKEN_SECRET_DE)
    de_bot.post(date.today())

if __name__ == "__main__":
    main()
