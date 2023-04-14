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

coord_matcher = compile('[a-z] ?[0-9]+')

def preprocess(text: str):
    def replace_word(text, word, replacement):
        text = text.replace(' ' + word, replacement)
        text = text.replace(word + ' ', replacement)
        return text
    text = text.lower()
    text = replace_word(text, 'are', 'R')
    text = replace_word(text, 'zero', '0')
    text = replace_word(text, 'too', '2')
    text = replace_word(text, 'to', '2')
    return text

def classify_action(text) -> Action:
    text = preprocess(text)
    matches = coord_matcher.match(text)
    if matches is not None:
        return Action(Goal.MOVE, pointString = matches.string)
    options = [
        process.extractOne(text, LEFT_WORDS)[1],
        process.extractOne(text, RIGHT_WORDS)[1],
        process.extractOne(text, DOWN_WORDS)[1],
        process.extractOne(text, UP_WORDS)[1],
    ]
    return action_dirs[np.argmax(options)]