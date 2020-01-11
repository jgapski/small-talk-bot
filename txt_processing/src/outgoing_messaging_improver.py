from small_talk_assets import SmallTalkAssets
from action import Action

import ASAP_detector


class OutgoingMessageImprover:
    @staticmethod
    def improve(outgoingMessage):
        if ASAP_detector.count_ASAP(outgoingMessage) >= 2:
            msg = "Please, consider using fewer ASAPs, do not give too much pressure to your team"
            return Action("suggest_change", msg)
        if OutgoingMessageImprover.__make_more_polite_question(outgoingMessage):
            msg = "Consider starting the question with Could you please tell me, ..."
            return Action("suggest_change", msg)
        return Action("no_suggestion", "")

    @staticmethod
    def __make_more_polite_question(textMessage):
        for question_word in SmallTalkAssets.question_starting_words():
            if textMessage.startswith(question_word):
                return True
        return False

