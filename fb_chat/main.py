from fbchat import Client, Message
from creds import Creds

import requests
import json


class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        print("{} from {} in {}".format(
            message_object, thread_id, thread_type.name))

        marker = "#SUGGESTION"

        if author_id == self.uid and not message_object.text.startswith(marker):
            payload = {
                "from": str(author_id),
                "channel_name": str(thread_id),
                "msg": str(message_object.text)
            }

            url = "http://localhost:8080"
            response = requests.post(url, data=json.dumps(payload))
            json_data = json.loads(response.text)

            suggestions = json_data['suggestions']
            print(suggestions)
            for suggestion in suggestions:
                text = marker + " " + suggestion
                msg = Message(text=text)
                self.send(msg, thread_id=thread_id, thread_type=thread_type)


client = EchoBot(Creds.email(), Creds.password())
client.listen()
