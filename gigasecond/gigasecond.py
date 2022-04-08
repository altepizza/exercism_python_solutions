from datetime import timedelta

GIGASECOND = 1000000000


def add(moment):
    return moment + timedelta(seconds=GIGASECOND)
