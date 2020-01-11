import unittest
import sys, os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import ASAP_detector

# from ASAP_detector import count_ASAP

class TestASAPcountig(unittest.TestCase):

    def test_empty_text_contains_no_ASAPs(self):
        self.assertEqual(ASAP_detector.count_ASAP(""), 0, "")

    def test_single_ASAP_is_counted_as_one(self):
        self.assertEqual(ASAP_detector.count_ASAP("ASAP"), 1, "")

if __name__ == '__main__':
    unittest.main()