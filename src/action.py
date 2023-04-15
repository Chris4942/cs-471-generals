from enum import Enum
from string import ascii_lowercase


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

directions = [
    Direction.UP,
    Direction.DOWN,
    Direction.LEFT,
    Direction.RIGHT,
]

class Goal(Enum):
    MOVE = 0
    SPREAD_OUT = 1

class ActionPrimitive:
    def __init__(self, position: tuple[int, int], direction: Direction):
        self.position = position
        self.direction = direction
        
class Point:
    def __init__(self, r, c):
        self.r = r
        self.c = c
    
    def __str__(self) -> str:
        return f"Point: {self.r}, {self.c}"
    
    def __repr__(self) -> str:
        return str(self)
    
    @staticmethod
    def of(string) -> tuple[int, int]:
        col = ascii_lowercase.find(string[0])
        row = int(string[1:])
        return Point(row, col)

class Group:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"group: {self.amount}"
    
    @staticmethod
    def of(string):
        return Group(int(string))

class Action:
    def __init__(
                self,
                goal: Goal = None,
                direction: Direction = None,
                destination_point: str = None,
                starting_point: str = None,
                ):
        self.goal = goal
        self.direction = direction
        self.destination: Point = Point.of(destination_point) if destination_point is not None else None
        self.start: Point = Point.of(starting_point) if starting_point is not None else None
        self.amount = 1
        self.group = None

    
    def __str__(self) -> str:
        return f"Action ({self.goal}), ({self.direction} {self.amount} spaces), ({self.start}/{self.group}) -> ({self.destination})"


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
