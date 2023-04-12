from typing import Callable
from action import Action, Direction, Location, Point

class Strategist:
    movement_computers: dict[Direction, Callable[[Location], Location]] = {
        Direction.UP: lambda s: Point(s.r - 1, s.c),
        Direction.DOWN: lambda s: Point(s.r + 1, s.c),
        Direction.RIGHT: lambda s: Point(s.r, s.c + 1),
        Direction.LEFT: lambda s: Point(s.r, s.c - 1),
    }

    def __init__(self, push_attack, find_all_owned_territory_coords):
        self.push_attack = push_attack
        self.find_all_owned_territoy_coords = find_all_owned_territory_coords

    
    def execute(self, action: Action):
        """
        Currently operating under the following assumptions:
        No start coord is provided
        Goal is Goal.MOVE
        """
        owned_points = self.find_all_owned_territoy_coords()
        start: Point = max(owned_points).p
        if action.destination is not None:
            current_point = start
            print(f"action destination c: {action.destination.c}")
            if current_point.r < action.destination.r:
                for _ in range(action.destination.r - current_point.r):
                    next_point = Point(current_point.r + 1, current_point.c)
                    self.push_attack(current_point, next_point)
                    current_point = next_point
            else:
                for _ in range(current_point.r - action.destination.r):
                    next_point = Point(current_point.r - 1, current_point.c)
                    self.push_attack(current_point, next_point)
                    current_point = next_point
            
            print(f"current_point.c: {current_point.c}")
            print(f"action.destination.c: {action.destination.c}")
            if current_point.c < action.destination.c:
                for _ in range (action.destination.c - current_point.c):
                    print("up")
                    next_point = Point(current_point.r, current_point.c + 1)
                    self.push_attack(current_point, next_point)
                    current_point = next_point
            else:
                for _ in range(current_point.c - action.destination.c):
                    print("down")
                    next_point = Point(current_point.r, current_point.c - 1)
                    self.push_attack(current_point, next_point)
                    current_point = next_point

        if action.direction is not None:
            destination = self.compute_destination(start, direction=action.direction)
            self.push_attack(start, destination)
    
    def compute_destination(self, start: Point, direction: Direction) -> Point:
        print(Strategist.movement_computers)
        return Strategist.movement_computers[direction](start)

class DoNothingStrategist:
    def execute(self, action: Action):
        print(f"executing {action}")
