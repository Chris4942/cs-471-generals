from action import Action, Direction, Goal
import numpy as np

pos = 0
actions = [
    Direction.UP,
    Direction.UP,
    Direction.LEFT,
    Direction.LEFT,
    Direction.DOWN,
    Direction.DOWN,
    Direction.RIGHT,
    Direction.RIGHT,
]

def classify_action(text) -> Action:
    global pos, actions
    action = Action(Goal.MOVE, direction=actions[pos])
    pos += 1
    return action