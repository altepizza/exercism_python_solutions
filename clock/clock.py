from datetime import datetime
from datetime import timedelta


class Clock:
    def __init__(self, hour, minute):
        self.my_clock = datetime.strptime('00', '%H')
        self.my_clock += timedelta(minutes=minute)
        self.my_clock += timedelta(hours=hour)

    def __repr__(self):
        return self.my_clock.strftime('%H:%M')

    def __eq__(self, other):
        return self.__repr__() == other

    def __add__(self, minutes):
        self.my_clock += timedelta(minutes=minutes)
        return self

    def __sub__(self, minutes):
        self.my_clock -= timedelta(minutes=minutes)
        return self
