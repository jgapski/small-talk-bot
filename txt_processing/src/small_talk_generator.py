import random
import pyjokes
from strsimpy.levenshtein import Levenshtein

class SmallTalkGenerator:
    @staticmethod
    def init_conversation() -> str:
        return random.choice(SmallTalkAssets.greetings())

    @staticmethod
    def is_init_conversation_phrase(textMessage: str) -> bool:
        levenshtein = Levenshtein()
        for greeting in SmallTalkAssets.greetings():
            distance = levenshtein.distance(textMessage, greeting)
            if distance <= 3:
                return True
        return False


    # @staticmethod
    # def ask_simple_question():
    #     return "How are you?"

    @staticmethod
    def tell_a_joke():
        return pyjokes.get_joke()

class SmallTalkAssets:
    @staticmethod
    def greetings() -> [str]:
        return [
            "Hey",
            "Hi",
            "Hello",
            "Welcome"
        ]