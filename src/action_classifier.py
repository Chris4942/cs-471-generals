from action import Action, Direction, Goal
import numpy as np
from fuzzywuzzy import process

from word_lists import DOWN_WORDS, LEFT_WORDS, RIGHT_WORDS, UP_WORDS

action_dirs = [
    Action(Goal.MOVE, Direction.LEFT),
    Action(Goal.MOVE, Direction.RIGHT),
    Action(Goal.MOVE, Direction.DOWN),
    Action(Goal.MOVE, Direction.UP),
]

def classify_action(text) -> Action:
    options = [
        process.extractOne(text, LEFT_WORDS)[1],
        process.extractOne(text, RIGHT_WORDS)[1],
        process.extractOne(text, DOWN_WORDS)[1],
        process.extractOne(text, UP_WORDS)[1],
    ]
    return action_dirs[np.argmax(options)]