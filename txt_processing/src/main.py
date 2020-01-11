from incomming_messaging_interpreter import IncomingMessageInterpreter

msgs = [
    "Hi",
    "Hii",
    "How are you?",
    "Whats up",
    "We need it ASAP, and no later than asap",
    "Where are my keys?"
    ]

for msg in msgs:
    print(msg, (IncomingMessageInterpreter.interpete(msg).toJSON()))
