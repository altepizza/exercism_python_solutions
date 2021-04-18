from collections import deque
import string

def _find_replacement(char, lower_map, upper_map):
    if char.lower() not in string.ascii_lowercase:
        return char
    if char.islower():
        return lower_map[string.ascii_lowercase.find(char)]
    else:
        return upper_map[string.ascii_uppercase.find(char)]

def rotate(text, key):
    lower = deque(string.ascii_lowercase)
    higher = deque(string.ascii_uppercase)
    lower.rotate(-key)
    higher.rotate(-key)

    return ''.join([_find_replacement(c, lower, higher) for c in text])