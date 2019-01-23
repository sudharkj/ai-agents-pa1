import random

from model.state import State
from model.action import Action


class RandomizedReflexAgent:
    """
    Simple Reflex Agent
    """

    def __init__(self):
        print("initialized simple reflex agent")

    def action(self, percept):
        if percept is State.DIRTY:
            return Action.CLEAN
        # if percept is State.HOME:
        #     return random.choice([Action.FORWARD, Action.STOP])
        if percept is State.WALL:
            return random.choice([Action.LEFT, Action.RIGHT])
        return Action.FORWARD
