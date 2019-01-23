from enum import Enum


class Action(Enum):
    CLEAN = 2
    LEFT = 3
    RIGHT = 4
    FORWARD = 5
    STOP = 6

    def __str__(self):
        return '%5s' % str(self.name)
