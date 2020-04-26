import string

def is_pangram(sentence):
    return not set(string.ascii_lowercase) - set(sentence.lower())
