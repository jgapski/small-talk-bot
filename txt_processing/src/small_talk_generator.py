import random
import pyjokes

from small_talk_assets import SmallTalkAssets

class SmallTalkGenerator:
    @staticmethod
    def make_init_conversation_phrase() -> str:
        return random.choice(SmallTalkAssets.greetings())

    @staticmethod
    def make_feeling_answer_phrase() -> str:
        return random.choice(SmallTalkAssets.feeling_answer())

    @staticmethod
    def tell_a_joke():
        return pyjokes.get_joke()


class OutgoingMessageImprover:
    @staticmethod
    def interpete(outgoingMessage: str) -> str:
        pass
