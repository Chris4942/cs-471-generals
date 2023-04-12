from enum import Enum
from string import ascii_uppercase

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
        col = ascii_uppercase.find(string[0])
        row = int(string[1:])
        return Point(row, col)


class Action:
    def __init__(
                self,
                goal: Goal,
                direction: Direction = None,
                pointString: str = None,
                ):
        self.goal = goal
        self.direction = direction
        self.destination: Point = Point.of(pointString) if pointString is not None else None
    
    def __str__(self) -> str:
        return f"Action ({self.goal}), ({self.direction}), ({self.destination})"


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
