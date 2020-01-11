import json

class Action:
    def __init__(self, type, metadata):
        self.type = type
        self.metadata = metadata

    def toJSON(self):
        jsonObj = {
            "type": self.type,
            "metadata": self.metadata
        }
        return json.dumps(jsonObj)
