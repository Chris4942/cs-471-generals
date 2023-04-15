import os
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
        self.send_attack_to_gm = push_attack
        self.find_all_owned_territoy_coords = find_all_owned_territory_coords
        self.log_file = os.environ['STRATEGIST_FILE']

    
    def execute(self, action: Action):
        """
        Currently operating under the following assumptions:
        No start coord is provided
        Goal is Goal.MOVE
        """
        def find_closest_match(locations, num_to_match):
            return min(locations, key=lambda i: abs(i.n - num_to_match.amount)).p

        owned_coords = self.find_all_owned_territoy_coords()
        start: Point = (action.start if action.start is not None else 
                        find_closest_match(owned_coords, action.group) if action.group is not None else
                        max(owned_coords).p)
        if action.group is not None:
            self.log(f"a group exists on the point. It's at {start}")
        if action.destination is not None:
            current_point = start
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
            
            if current_point.c < action.destination.c:
                for _ in range (action.destination.c - current_point.c):
                    next_point = Point(current_point.r, current_point.c + 1)
                    self.push_attack(current_point, next_point)
                    current_point = next_point
            else:
                for _ in range(current_point.c - action.destination.c):
                    next_point = Point(current_point.r, current_point.c - 1)
                    self.push_attack(current_point, next_point)
                    current_point = next_point

        if action.direction is not None:
            destination = self.compute_destination(start, direction=action.direction)
            self.push_attack(start, destination)
    
    def compute_destination(self, start: Point, direction: Direction) -> Point:
        return Strategist.movement_computers[direction](start)

    def log(self, string):
        with open(self.log_file, 'a') as f:
            print(string, file=f)
    
    def push_attack(self, p1: Point, p2: Point):
        self.log(f"Moving from {p1} to {p2}")
        self.send_attack_to_gm(p1, p2)


class DoNothingStrategist:
    def execute(self, action: Action):
        print(f"executing {action}")
