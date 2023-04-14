from strategist import Strategist
from action import Action, Goal, Point, Location

def find_all_coords():
    return [Location(Point(1, 2), 12)]

attacks = []
def push_attack(a, b):
    attacks.append((a, b))

strategist = Strategist(find_all_owned_territory_coords=find_all_coords, push_attack=push_attack)
strategist.execute(action=Action(Goal.MOVE, destinationPoint="C3"))

print(attacks)
