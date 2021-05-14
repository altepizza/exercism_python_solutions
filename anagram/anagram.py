from collections import Counter

def is_anagaram(word, candidate):
    lower_word = word.lower()
    lower_candidate = candidate.lower()
    if lower_word == lower_candidate:
        return False
    word_letters = Counter(lower_word)
    candidate_letters = Counter(lower_candidate)
    return not word_letters - candidate_letters and not candidate_letters - word_letters

def find_anagrams(word, candidates):
    return [canditate for canditate in candidates if is_anagaram(word, canditate)]
