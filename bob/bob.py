import re
import unicodedata

re_is_question = re.compile(r'.+\?$')
re_is_yelling_a_question = re.compile(r'\b[A-Z]+\b.*\?$')
re_is_yelling = re.compile(
    r'(\b[A-Z0-9]+\b.*)*(\b[A-Z]+\b.*)+(\b[A-Z0-9]+\b.*)*$')


def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")


def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    hey_bob = remove_control_characters(hey_bob)
    if re_is_question.match(hey_bob):
        if re_is_yelling_a_question.match(hey_bob):
            return "Calm down, I know what I'm doing!"
        return 'Sure.'
    if re_is_yelling.match(hey_bob):
        return 'Whoa, chill out!'
    if len(hey_bob) == 0:
        return 'Fine. Be that way!'
    return 'Whatever.'
