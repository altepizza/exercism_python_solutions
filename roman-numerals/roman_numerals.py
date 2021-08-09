INT_TO_ROMAN = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
}


def roman(number):
    roman_chars = []
    for _int in INT_TO_ROMAN:
        counts = int(number / _int)
        roman_chars.append(INT_TO_ROMAN[_int] * counts)
        number -= _int * counts
    return ''.join(roman_chars)
