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
        
class PointString:
    def __init__(self, coord):
        self.string = coord
    
    def __str__(self):
        return f"PointString: {self.string}"

class Action:
    def __init__(
                self,
                goal: Goal,
                direction: Direction = None,
                pointString: PointString = None,
                ):
        self.goal = goal
        self.direction = direction
        self.pointString = pointString
    
    def __str__(self) -> str:
        return f"Action ({self.goal}), ({self.direction}), ({self.pointString})"


class Location:
    def __init__(self, p: PointString, n: int):
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
