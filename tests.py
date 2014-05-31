import unittest
from data import data
from bot import split_message

class DataTests(unittest.TestCase):

    def test_no_duplicates(self):
        data_ = []
        for i in data:
            data_.extend(i)
        duplicates = set([x for x in data_ if data_.count(x) > 1])
        self.assertEqual(duplicates, {}, "There is duplicate data.")

class SplitMessageTests(unittest.TestCase):

    def test_one_message(self):
        test_message = "This is a test string with less than 140 characters."
        self.assertEqual([test_message], split_message(test_message))

    def test_two_messages(self):
        test_message =  ("This is a test string with more than 140 characters"
            ". Adding useless words to make the string longer. This was not"
            " enough we need even more words. Adding a few more words to make"
            " it more distinct.")
        test_message1 = test_message[:133] + " (1/2)"
        test_message2 = test_message[134:] + " (2/2)"
        self.assertEqual([test_message1, test_message2], split_message(test_message))

    def test_three_messages(self):
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
        self.assertEqual([test_message1, test_message2, test_message3], split_message(test_message))

if __name__ == "__main__":
    unittest.main()
