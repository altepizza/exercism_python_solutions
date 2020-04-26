import re

def is_valid(isbn):
    result = re.match(r'^(-*[0-9]){9}(-*([0-9]|X)){1}$', isbn)
    if result:
        helper = 10
        sum = 0
        for field in isbn:
            if field.isdigit():
                sum += int(field) * helper
                helper -= 1
            elif field == 'X':
                sum += 10
        return sum % 11 == 0
    return False
