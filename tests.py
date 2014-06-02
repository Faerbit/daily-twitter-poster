import unittest
from data import data_de
from bot import TwitterBot
from datetime import date, datetime
import os

class DataTests(unittest.TestCase):

    def test_no_duplicates(self):
        data_ = []
        for i in data_de:
            data_.extend(i)
        duplicates = set([x for x in data_ if data_.count(x) > 1])
        self.assertEqual(duplicates, set(), "There is duplicate data.")

class TwitterBotTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if (os.environ["TRAVIS_SECURE_ENV_VARS"] == "true"):
            cls.test_api = True
            API_KEY_TEST=os.environ["API_KEY_TEST"]
            API_SECRET_TEST=os.environ["API_SECRET_TEST"]

            ACCESS_TOKEN_TEST=os.environ["ACCESS_TOKEN_TEST"]
            ACCESS_TOKEN_SECRET_TEST=os.environ["ACCESS_TOKEN_SECRET_TEST"]
            cls.test_string = "Test string: " + datetime.now().isoformat()
            cls.bot_test = TwitterBot("", [[cls.test_string]], API_KEY_TEST, 
                    API_SECRET_TEST, ACCESS_TOKEN_TEST, ACCESS_TOKEN_SECRET_TEST)
        else:
            cls.test_api = False

    def test_split_message_one_message(self):
        test_message = "This is a test string with less than 140 characters."
        self.assertEqual([test_message], TwitterBot.split_message(self, test_message))

    def test_split_message_two_messages(self):
        test_message =  ("This is a test string with more than 140 characters"
            ". Adding useless words to make the string longer. This was not"
            " enough we need even more words. Adding a few more words to make"
            " it more distinct.")
        test_message1 = test_message[:133] + " (1/2)"
        test_message2 = test_message[134:] + " (2/2)"
        self.assertEqual([test_message1, test_message2], 
            TwitterBot.split_message(self, test_message))

    def test_split_message_three_messages(self):
        test_message =  ("This is a test string with more than 280 characters"
                ". Adding useless words to make the string longer. This was "
                "not enough we need even more words. Mary had a little lamb. "
                "His fleece was white as snow. And everywhere that Mary went, "
                "the lamb was sure to go. He followed her to school one day. "
                "Which was against the rule. It made the children laugh and "
                "play, to see a lamb at school.")
        test_message1 = test_message[:133] + " (1/3)"
        test_message2 = test_message[134:267] + " (2/3)"
        test_message3 = test_message[268:] + " (3/3)"
        self.assertEqual([test_message1, test_message2, test_message3], 
            TwitterBot.split_message(self, test_message))
  
    def test_twitter_api(self):
        if not self.test_api:
            raise self.skipTest("API tokens not defined.")
        test_date=date(2000, 1, 1)
        self.bot_test.post(test_date)
        self.assertEqual(self.test_string + "!", self.bot_test.twitter.get_home_timeline()[0]["text"])

if __name__ == "__main__":
    unittest.main()
