import unittest
from data import data

class DataTests(unittest.TestCase):

    def test_no_duplicates(self):
        data_ = []
        for i in data:
            data_.extend(i)
        duplicates = set([x for x in data_ if data_.count(x) > 1])
        self.assertEqual(duplicates, {}, "There is duplicate data.")


if __name__ == "__main__":
    unittest.main()
