class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = 0
        self.__add__(minute)

    def __repr__(self):
        return '{:02d}:{:02d}'.format(self.hour, self.minute)

    def __eq__(self, other):
        return self.__repr__() == other

    def __add__(self, minutes):
        hours, self.minute = divmod((self.minute + minutes), 60)
        self.hour = divmod((self.hour + hours), 24)[1]
        return self

    def __sub__(self, minutes):
        hours, self.minute = divmod((self.minute - minutes), 60)
        self.hour = divmod((self.hour + hours), 24)[1]
        return self
