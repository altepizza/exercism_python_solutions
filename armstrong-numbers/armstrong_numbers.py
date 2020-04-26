def is_armstrong_number(number):
    numberparts = list(str(number))
    POWER = len(numberparts)
    result = 0
    for number in numberparts:
        result += int(number) ** POWER
    return number == result
