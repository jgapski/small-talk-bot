from incomming_messaging_interpreter import IncomingMessageInterpreter
from outgoing_messaging_improver import OutgoingMessageImprover

incoming_msgs = [
    "Hi",
    "Hii",
    "How are you?",
    "Whats up",
    "Where are my keys?"
    ]

print("\nIncomming\n")

for msg in incoming_msgs:
    print(msg, (IncomingMessageInterpreter.interpete(msg).toJSON()))

outgoing_msgs = [
    "We need it ASAP, and no later than asap",
    "We need it ASAP"
    ]

print("\nOutgoing\n")

for msg in outgoing_msgs:
    print(msg, (OutgoingMessageImprover.improve(msg).toJSON()))
