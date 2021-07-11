import string

ALPHABET = string.ascii_lowercase

ENCODER = {a: z for a, z in zip(ALPHABET, ALPHABET[::-1])}
DECODER = {z: a for a, z in zip(ALPHABET, ALPHABET[::-1])}


def _decide_to_add_space(char, char_index):
    if char_index and char_index % 5 == 0:
        return f' {char}'
    return char


def _clean_plain_text(plain_text):
    cleaned_text = plain_text.replace(' ', '').lower()
    punctuations = str.maketrans(dict.fromkeys(string.punctuation))
    return cleaned_text.translate(punctuations)


def encode(plain_text):
    cleaned_text = _clean_plain_text(plain_text)
    ciphered_chars = [ENCODER.get(char, char) for char in cleaned_text]
    return ''.join([_decide_to_add_space(
        char, index) for index, char in enumerate(ciphered_chars)])


def decode(ciphered_text):
    cleaned_text = ciphered_text.replace(' ', '')
    return ''.join([DECODER.get(char, char) for char in cleaned_text])
