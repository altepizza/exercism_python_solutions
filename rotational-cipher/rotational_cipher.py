from collections import deque
import string

def _find_replacement(char, cipher_map):        
    if char.islower():
        return cipher_map[string.ascii_lowercase.find(char)]
    elif char.isupper():
        return cipher_map[string.ascii_uppercase.find(char)].upper()
    return char

def rotate(text, key):
    cipher_map = deque(string.ascii_lowercase)
    cipher_map.rotate(-key)
    return ''.join([_find_replacement(c, cipher_map) for c in text])