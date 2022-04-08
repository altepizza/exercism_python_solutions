VOWELS = 'aeiouAEIOU'


def _starts_with_vowel_action(word):
    return word + 'ay'


def _starts_with_consonant_action(word):
    last_consonant_idx = 0
    for idx, char in enumerate(word):
        last_consonant_idx = idx
        if char in VOWELS:
            if idx > 0 and char == 'u' and word[idx - 1] == 'q':
                last_consonant_idx += 1
                break
            break
        if idx > 0 and char == 'y':
            break
    new_extracted_ending = word[0:last_consonant_idx]
    word = word + new_extracted_ending
    return word[last_consonant_idx:] + 'ay'


def pigify(word):
    if word[0] in VOWELS or word.startswith('xr') or word.startswith('yt'):
        return _starts_with_vowel_action(word)
    else:
        return _starts_with_consonant_action(word)


def translate(text):
    new_words = [pigify(word) for word in text.split(' ')]
    return ' '.join(new_words)
