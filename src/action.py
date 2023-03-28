from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Goal(Enum):
    MOVE = 0

class ActionPrimitive:
    def __init__(self, position: tuple[int, int], direction: Direction):
        self.position = position
        self.direction = direction

class Action:
    def __init__(self, goal: Goal, direction: Direction):
        self.goal = goal
        self.direction = direction
