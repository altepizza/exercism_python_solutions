def score(word):
    LETTER_SCORE = dict.fromkeys(['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'], 1)
    LETTER_SCORE.update(dict.fromkeys(['d', 'g'], 2))
    LETTER_SCORE.update(dict.fromkeys(['b', 'c', 'm', 'p'], 3))
    LETTER_SCORE.update(dict.fromkeys(['f', 'h', 'v', 'w', 'y'], 4))
    LETTER_SCORE.update(dict.fromkeys(['k'], 5))
    LETTER_SCORE.update(dict.fromkeys(['j', 'x'], 8))
    LETTER_SCORE.update(dict.fromkeys(['q', 'z'], 10))
    return sum(LETTER_SCORE[c] for c in word.lower() if c in LETTER_SCORE)
