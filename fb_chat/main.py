from fbchat import log, Client
from creds import Creds

import requests
import json

class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        # # If you're not the author, echo
        # if author_id != self.uid:
        #     self.send(message_object, thread_id=thread_id, thread_type=thread_type)


        print("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        if author_id == self.uid:
            payload = {
                "from": str(author_id),
                "channel_name": str(thread_id),
                "msg": str(message_object.text)
                }

            url = "http://localhost:8080"
            response = requests.post(url, data=json.dumps(payload))
            json_data = json.loads(response.text)

            print(json_data)
            # suggestions = []
            # for suggestion in suggestions:
            #     thread.send_text(suggestion)

client = EchoBot(Creds.email(), Creds.password())
client.listen()