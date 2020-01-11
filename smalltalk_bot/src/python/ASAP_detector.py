import sys
import re

def count_ASAP(messageText):
    pattern = re.compile(r'asap',re.IGNORECASE)
    iterator = re.finditer(pattern, messageText)
    count = 0
    for match in iterator:
        count +=1
    return count

arguments = str(sys.argv)
a_msg = arguments.replace("['src/python/ASAP_detector.py', '", "")
msg = a_msg.replace("']", "")

print(count_ASAP(msg))
