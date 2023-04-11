from action import Action, Direction, Goal
import numpy as np
from fuzzywuzzy import process
from re import compile

from word_lists import DOWN_WORDS, LEFT_WORDS, RIGHT_WORDS, UP_WORDS

action_dirs = [
    Action(Goal.MOVE, Direction.LEFT),
    Action(Goal.MOVE, Direction.RIGHT),
    Action(Goal.MOVE, Direction.DOWN),
    Action(Goal.MOVE, Direction.UP),
]

coord_matcher = compile('[A-Z][0-9]+')

def classify_action(text) -> Action:
    matches = coord_matcher.match(text)
    print(matches)
    print(type(matches))
    print(dir(matches))
    if matches is not None:
        return Action(Goal.MOVE, pointString = matches.string)
    options = [
        process.extractOne(text, LEFT_WORDS)[1],
        process.extractOne(text, RIGHT_WORDS)[1],
        process.extractOne(text, DOWN_WORDS)[1],
        process.extractOne(text, UP_WORDS)[1],
    ]
    return action_dirs[np.argmax(options)]