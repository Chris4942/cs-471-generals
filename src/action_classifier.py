from action import Action, Direction, Goal
import numpy as np

def classify_action(text) -> Action:
    return Action(Goal.MOVE, direction=np.random.choice([e.value for e in Direction]))