class Clock:
    def __init__(self, hour, minute):
        diff_hours, self.minute = divmod(minute, 60)
        _, self.hour = divmod((hour + diff_hours), 24)

    def __repr__(self):
        return '{:02d}:{:02d}'.format(self.hour, self.minute)

    def __eq__(self, other):
        return self.__repr__() == other

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
