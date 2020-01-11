import random
import pyjokes

from strsimpy.levenshtein import Levenshtein
from small_talk_assets import SmallTalkAssets

class SmallTalkGenerator:
    @staticmethod
    def make_init_conversation_phrase() -> str:
        return random.choice(SmallTalkAssets.greetings())

    @staticmethod
    def is_init_conversation_phrase(textMessage: str) -> bool:
        levenshtein = Levenshtein()
        for greeting in SmallTalkAssets.greetings():
            distance = levenshtein.distance(textMessage, greeting)
            if distance <= 3:
                return True
        return False

    @staticmethod
    def tell_a_joke():
        return pyjokes.get_joke()
