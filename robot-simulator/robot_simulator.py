import operator
from collections import deque

EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.compass = deque([NORTH, EAST, SOUTH, WEST])
        while self.compass[0] != direction:
            self.compass.rotate(1)
        self.direction = self.compass[0]
        self.coordinates = (x, y)

    def _turn(self, cmd):
        turn_to_value = {'L': 1, 'R': -1}
        self.compass.rotate(turn_to_value[cmd])
        self.direction = self.compass[0]

    def _walk(self):
        self.coordinates = tuple(
            map(operator.add, self.coordinates, self.compass[0]))

    def move(self, commands=''):
        for cmd in commands:
            if cmd in 'LR':
                self._turn(cmd)
            elif cmd is 'A':
                self._walk()
