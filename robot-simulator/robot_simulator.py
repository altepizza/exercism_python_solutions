import operator
from collections import deque

EAST = 'EAST'
NORTH = 'NORTH'
WEST = 'WEST'
SOUTH = 'SOUTH'


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.compass = deque([NORTH, EAST, SOUTH, WEST])
        while self.compass[0] != direction:
            self.compass.rotate(1)
        self.direction = self.compass[0]
        self.coordinates = (x, y)

    def move(self, commands=''):
        for cmd in commands:
            if cmd is 'L':
                self.compass.rotate(1)
                self.direction = self.compass[0]
            if cmd is 'R':
                self.compass.rotate(-1)
                self.direction = self.compass[0]
            if cmd is 'A':
                if self.direction is EAST:
                    self.coordinates = tuple(
                        map(operator.add, self.coordinates, (1, 0)))
                if self.direction is NORTH:
                    self.coordinates = tuple(
                        map(operator.add, self.coordinates, (0, 1)))
                if self.direction is SOUTH:
                    self.coordinates = tuple(
                        map(operator.add, self.coordinates, (0, -1)))
                if self.direction is WEST:
                    self.coordinates = tuple(
                        map(operator.add, self.coordinates, (-1, 0)))
