from typing import Callable
from action import Action, Direction, Location, PointString

class Strategist:
    movement_computers: dict[Direction, Callable[[Location], Location]] = {
        Direction.UP: lambda s: PointString(s.r - 1, s.c),
        Direction.DOWN: lambda s: PointString(s.r + 1, s.c),
        Direction.RIGHT: lambda s: PointString(s.r, s.c + 1),
        Direction.LEFT: lambda s: PointString(s.r, s.c - 1),
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
        print(f"I would be executing {action.direction}")
        owned_points = self.find_all_owned_territoy_coords()
        start: PointString = max(owned_points).p
        destination = self.compute_destination(start, direction=action.direction)
        self.push_attack(start, destination)
    
    def compute_destination(self, start: PointString, direction: Direction) -> PointString:
        print(Strategist.movement_computers)
        return Strategist.movement_computers[direction](start)

class DoNothingStrategist:
    def execute(self, action: Action):
        print(f"executing {action}")
