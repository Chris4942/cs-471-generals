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

class Point:
    def __init__(self, r, c):
        self.r = r
        self.c = c


class Location:
    def __init__(self, p: Point, n: int):
        self.p = p
        self.n = n
    
    def __gt__(self, other):
        return self.n > other.n

    def __ge__(self, other):
        return self.n >= other.n
    
    def __lt__(self, other):
        return self.n < other.n

    def __lt__(self, other):
        return self.n <= other.n
