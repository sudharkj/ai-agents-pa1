import random

from model.action import Action
from model.state import State


class Environment:
    """
    Class definition for environment.
    """

    def __init__(self, dimensions, start_location, start_direction):
        # define grid
        self.start_grid_state = []
        self.start_grid_state.append([State.WALL] * (dimensions[1] + 2))
        for r in range(dimensions[0]):
            column = [State.WALL]
            column.extend(random.choices([State.CLEAN, State.DIRTY], k=dimensions[0]))
            column.extend([State.WALL])
            self.start_grid_state.append(column)
        self.start_grid_state.append([State.WALL] * (dimensions[1] + 2))

        self._dirty_cells = 0
        self.count_dirty_cells()

        # define start location
        self.start_location = start_location
        self.start_direction = start_direction

        # reset states
        self.grid_state = None
        self.location = None
        self.direction = None
        self.reset()

    def count_dirty_cells(self):
        dirty_cells = 0
        for r in self.start_grid_state:
            for c in r:
                if c is State.DIRTY:
                    dirty_cells = dirty_cells + 1
        self._dirty_cells = dirty_cells
        print('clean', dirty_cells)

    @property
    def dirty_cells(self):
        return self._dirty_cells

    def reset(self):
        self.grid_state = [[c for c in r] for r in self.start_grid_state]
        self.location = (self.start_location[0], self.start_location[1])
        self.direction = self.start_direction

    def percept(self):
        if self.grid_state[self.location[0]][self.location[1]] is State.DIRTY:
            return State.DIRTY

        new_location = tuple([self.location[i] + self.direction.value[i] for i in range(len(self.location))])
        if self.grid_state[new_location[0]][new_location[1]] is State.WALL:
            return State.WALL

        if self.location == self.start_location:
            return State.HOME

        return State.CLEAN

    def act(self, action):
        if action is Action.CLEAN:
            self.grid_state[self.location[0]][self.location[1]] = State.CLEAN
        if action is Action.LEFT:
            self.direction = self.direction.previous()
        if action is Action.RIGHT:
            self.direction = self.direction.next()
        if action is Action.FORWARD:
            self.location = tuple([self.location[i] + self.direction.value[i] for i in range(len(self.location))])

    def __str__(self):
        return str('\n'.join(['   '.join([str(c) for c in r]) for r in self.grid_state]))


if __name__ == '__main__':
    dimension = (10, 10)
    location = (0, 0)
    from model.direction import Direction
    direction = Direction.LEFT
    environment = Environment(dimension, location, direction)
    print('Environment Info:')
    print(environment)
    print(environment.percept())
    environment.act(Action.RIGHT)
