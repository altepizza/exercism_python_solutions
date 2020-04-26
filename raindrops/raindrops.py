def convert(number):
    FACTOR_WORD = ((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))
    result = [word for factor, word in FACTOR_WORD if number % factor == 0]
    return ''.join(result) or str(number)
