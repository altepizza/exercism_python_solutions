from calendar import monthrange
from collections import deque
from datetime import date

WEEKDAY_IDX = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
    'Sunday': 7
}


def lets_rotate(week, times, day_index):
    dequed_week = deque(week)
    day = 1
    for x in range(times):
        while dequed_week[0] != day_index:
            dequed_week.rotate(-1)
            day += 1
        if x < times - 1:
            dequed_week.rotate(-1)
            day += 1
    return day


def rotate_until_teenth(week, day_index):
    dequed_week = deque(week)
    dequed_week.rotate(-12)
    day = 13
    while day < 20:
        if dequed_week[0] == day_index:
            break
        dequed_week.rotate(-1)
        day += 1
    return day


def find_last_in_month(week, day_index, days_of_month):
    day = week.index(day_index) + 1
    while day + 7 <= days_of_month:
        day += 7
    return day


def create_week_list(start_day):
    if start_day == 1:
        return list(range(1, 8))
    else:
        return list(range(start_day, 8)) + list(range(1, start_day))


def meetup(year, month, week, day_of_week):
    first_day_of_month = date(year, month, 1).weekday() + 1
    first_week = create_week_list(first_day_of_month)
    wanted_day = WEEKDAY_IDX[day_of_week]
    if week == '1st':
        day = lets_rotate(first_week, 1, wanted_day)
    elif week == '2nd':
        day = lets_rotate(first_week, 2, wanted_day)
    elif week == '3rd':
        day = lets_rotate(first_week, 3, wanted_day)
    elif week == '4th':
        day = lets_rotate(first_week, 4, wanted_day)
    elif week == '5th':
        day = lets_rotate(first_week, 5, wanted_day)
    elif week == 'teenth':
        day = rotate_until_teenth(first_week, wanted_day)
    elif week == 'last':
        num_days = monthrange(year, month)[1]
        day = find_last_in_month(first_week, wanted_day, num_days)
    try:
        return date(year, month, day)
    except:
        raise MeetupDayException('Could not find a date matching your request')


class MeetupDayException(Exception):
    pass