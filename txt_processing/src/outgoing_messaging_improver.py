from action import Action

import ASAP_detector


class OutgoingMessageImprover:
    @staticmethod
    def improve(outgoingMessage):
        if ASAP_detector.count_ASAP(outgoingMessage) >= 2:
            msg = "Please, consider using fewer ASAPs, do not give too much pressure to your team"
            return Action("suggest_change", msg)

        return Action("no_suggestion", "")
