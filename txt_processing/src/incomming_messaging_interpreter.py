from small_talk_generator import SmallTalkGenerator
from small_talk_assets import SmallTalkAssets
from strsimpy.levenshtein import Levenshtein
from action import Action


class IncomingMessageInterpreter:
    @staticmethod
    def interpete(incomingMessage):
        if IncomingMessageInterpreter.__is_init_conversation_phrase(incomingMessage):
            return Action("suggest_reply", SmallTalkGenerator.make_init_conversation_phrase())
        if IncomingMessageInterpreter.__is_init_feeling_question(incomingMessage):
            return Action("suggest_reply", SmallTalkGenerator.make_feeling_answer_phrase())
        return Action("no_suggestion", "")

    @staticmethod
    def __is_init_conversation_phrase(textMessage: str) -> bool:
        return IncomingMessageInterpreter.__is_phrase(textMessage, 3, SmallTalkAssets.greetings())

    @staticmethod
    def __is_init_feeling_question(textMessage: str) -> bool:
        return IncomingMessageInterpreter.__is_phrase(textMessage, 5, SmallTalkAssets.feeling_questions())

    @staticmethod
    def __is_phrase(textMessage: str, maxDistance: int, assets: [str]) -> bool:
        levenshtein = Levenshtein()
        for phrase in assets:
            distance = levenshtein.distance(textMessage, phrase)
            if distance <= maxDistance:
                return True
        return False
