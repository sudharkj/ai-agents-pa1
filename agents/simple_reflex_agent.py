from model.state import State
from model.action import Action


class SimpleReflexAgent:
    """
    Simple Reflex Agent
    """

    def __init__(self):
        print("initialized simple reflex agent")

    def action(self, percept):
        if percept is State.DIRTY:
            return Action.CLEAN
        # if percept is State.HOME:
        #     return Action.STOP
        if percept is State.WALL:
            return Action.RIGHT
        return Action.FORWARD
