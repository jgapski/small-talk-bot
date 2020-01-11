from src.small_talk_generator import SmallTalkGenerator
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestGreetings(unittest.TestCase):

    def test_1(self):
        self.assertIn(SmallTalkGenerator.init_conversation(),
                      SmallTalkAssets.greetings(), "")


if __name__ == '__main__':
    unittest.main()
