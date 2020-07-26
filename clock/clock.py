class Clock:
    def __init__(self, hour, minute):
        diff_hours, self.minute = divmod(minute, 60)
        self.hour = divmod((hour + diff_hours), 24)[1]

    def __repr__(self):
        return '{:02d}:{:02d}'.format(self.hour, self.minute)

    def __eq__(self, other):
        return self.__repr__() == other

    def __add__(self, minutes):
        diff_hour, new_minute = divmod((self.minute + minutes), 60)
        new_hour = divmod((self.hour + diff_hour), 24)[1]
        return Clock(new_hour, new_minute)

    def __sub__(self, minutes):
        diff_hour, new_minute = divmod((self.minute - minutes), 60)
        new_hour = divmod((self.hour + diff_hour), 24)[1]
        return Clock(new_hour, new_minute)
