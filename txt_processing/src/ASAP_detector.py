import re

def count_ASAP(messageText):
    return len(re.findall("ASAP", messageText))
