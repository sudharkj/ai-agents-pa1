from enum import Enum


class State(Enum):
    WALL = 0
    DIRTY = 1
    CLEAN = 2
    HOME = 3

    def __str__(self):
        return '%5s' % str(self.name)
