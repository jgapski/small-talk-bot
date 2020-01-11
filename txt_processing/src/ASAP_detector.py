import re

#     asap_match = re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


def count_ASAP(messageText):
    pattern = re.compile(r'asap',re.IGNORECASE) 
    iterator = re.finditer(pattern, messageText)
    count = 0
    for match in iterator:
        count +=1
    return count
