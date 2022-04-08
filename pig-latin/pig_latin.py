VOWELS = 'aeiouAEIOU'


def _rule_one(word):
    return word + 'ay'


def _rule_two(word):
    last_consonant_idx = 0
    for i, char in enumerate(word):
        if char in VOWELS:
            if i > 0 and char == 'u' and word[i - 1] == 'q':
                last_consonant_idx = i + 1
                break
            last_consonant_idx = i
            break
        if i > 0 and char == 'y':
            last_consonant_idx = i
            break
    new_ending = word[0:last_consonant_idx]
    word = word + new_ending
    word = word[last_consonant_idx:] + 'ay'
    return word


def translate(text):
    words = text.split(' ')
    new_words = []
    for word in words:
        if word[0] in VOWELS or word.startswith('xr') or word.startswith('yt'):
            word = _rule_one(word)
        else:
            word = _rule_two(word)
        new_words.append(word)
    return ' '.join(new_words)
