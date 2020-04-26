import re

def abbreviate(words):
    words_splitted = re.split("[^a-zA-Z']", words.upper())
    return ''.join([word[0]
                    for word
                    in words_splitted
                    if word and word[0].isalpha()])
