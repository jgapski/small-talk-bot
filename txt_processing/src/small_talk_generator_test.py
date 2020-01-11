import unittest

from small_talk_generator import SmallTalkGenerator
from small_talk_assets import SmallTalkAssets


class TestGreetings(unittest.TestCase):

    def test_1(self):
        self.assertIn(SmallTalkGenerator.make_init_conversation_phrase(),
                      SmallTalkAssets.greetings(), "")


if __name__ == '__main__':
    unittest.main()
