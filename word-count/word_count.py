import re
from collections import Counter

def count_words(sentence):
    sentence = sentence.lower().replace('_', ' ')
    findings = re.findall(r"(\w+('t)?)", sentence)
    words = Counter(finding[0] for finding in findings)
    return dict(words)
