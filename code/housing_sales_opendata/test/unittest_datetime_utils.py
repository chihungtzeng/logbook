import unittest
from datetime_utils import roc_date_to_datetime


class DatetimeUtilsTest(unittest.TestCase):
    def test_a(self):
        _dt = roc_date_to_datetime("1070402")
        self.assertEqual(2018, _dt.year)
        self.assertEqual(4, _dt.month)
        self.assertEqual(2, _dt.day)


if __name__ == "__main__":
    unittest.main()
