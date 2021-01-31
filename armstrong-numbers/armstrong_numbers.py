def is_armstrong_number(number):
    str_number = str(number)
    power = len(str_number)
    sum_of_powers = sum([int(no)**power for no in str_number])
    return sum_of_powers == number
