from enum import Enum


class Direction(Enum):
    LEFT = (0, -1)
    TOP = (-1, 0)
    RIGHT = (0, 1)
    BOTTOM = (1, 0)

    def previous(self):
        prev = Direction.BOTTOM
        for dir in Direction:
            if dir is self:
                return prev
            prev = dir

    def next(self):
        prev = Direction.BOTTOM
        for dir in Direction:
            if prev is self:
                return dir
            prev = dir

    def __str__(self):
        return '%5s' % str(self.name)
