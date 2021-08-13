import math


def square(number):
    if number < 1 or number > 64:
        raise ValueError('number must be positive and not exceed 64')
    return math.pow(2, number - 1)


def total():
    # This won't never change, why waste resources
    return 18446744073709551615
