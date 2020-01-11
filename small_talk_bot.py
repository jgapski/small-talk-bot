import requests
from slack import RTMClient

URL = "http://localhost:8080"
BOT_TOKEN = ""


@RTMClient.run_on(event="message")
def say_hello(**payload):
    data = payload['data']
    print("Received event: " + str(data))
    web_client = payload['web_client']

    if 'text' in data:
        channel_id = data['channel']
        user = data['user']

        params = {"from": user, "channel_name": channel_id, "msg": data['text']}
        response = "We tried to get suggestion, but there was \n an error connecting to server"
        try:
            r = requests.post(url=URL, json=params)
            if r.status_code == 200:
                response = '\n'.join(r.json()['suggestions'])
        except requests.exceptions.RequestException as e:
            print(e)

        web_client.chat_postEphemeral(user=user, channel=channel_id, text=response)


rtm_client = RTMClient(token=BOT_TOKEN)
rtm_client.start()
