import os
from action import Action, Direction, Goal, Group, Point
import numpy as np
from fuzzywuzzy import process
from re import compile

from word_lists import DOWN_WORDS, LEFT_WORDS, RIGHT_WORDS, SPREAD_OUT_WORDS, UP_WORDS

action_dirs = [
    Direction.LEFT,
    Direction.RIGHT,
    Direction.DOWN,
    Direction.UP,
]

coord_matcher = compile('(?<= )[a-z] ?[0-9]+')
group_matcher = compile('(?<! \w) \d+(?= )')

letter_o_matcher = compile('(^| )0(?=\d)')
ignore_matcher = compile('[-]')
a_fix_matcher = compile('8(?=\d\d?)')

action_classifier_log_file = os.environ['ACTION_CLASSIFIER_LOG_FILE']

def preprocess(text: str):
    log(f"prepreprocessed text:\"{text}\"")
    def replace_word(text, word, replacement):
        text = text.replace(' ' + word, replacement)
        text = text.replace(word + ' ', replacement)
        return text
    text = text.lower()
    text = replace_word(text, 'are', 'R')
    text = replace_word(text, 'zero', '0')
    text = replace_word(text, 'too', '2')
    text = replace_word(text, 'easier', 'e0')
    text = replace_word(text, 'ask', 's')
    text = replace_word(text, 'for', '4')
    text = replace_word(text, 'spell', 'L')
    text = text.replace('use your', 'u0')
    text = text.replace('and', 'n')
    text = text.replace('one', '1')
    text = text.replace('two', '2')
    text = text.replace('three', '3')
    text = text.replace('four', '4')
    text = text.replace('five', '5')
    text = text.replace('six', '6')
    text = text.replace('sex', '6')
    text = text.replace('seven', '7')
    text = text.replace('eight', '8')
    text = text.replace('nine', '9')
    text = letter_o_matcher.sub(' o', text)
    text = ignore_matcher.sub('', text)
    text = a_fix_matcher.sub('a', text)
    log(f"post_preprocessed_text:\"{text}\"")
    return ' ' + text + ' '

def classify_action(text) -> Action:
    def help(text):
        action = Action()
        if process.extractOne(text, SPREAD_OUT_WORDS)[1] > 80:
            action.goal = Goal.SPREAD_OUT
        else:
            action.goal = Goal.MOVE
        text = preprocess(text)
        coord_matches = coord_matcher.findall(text)
        group_matches = group_matcher.findall(text)
        if len(group_matches) > 0:
            action.group = Group.of(group_matches[0])
        if len(coord_matches) > 1:
            action.destination = Point.of(coord_matches[1])
            action.start = Point.of(coord_matches[0])
        if len(coord_matches) == 1:
            action.destination = Point.of(coord_matches[0])
        if action.destination is None:
            options = [
                process.extractOne(text, LEFT_WORDS)[1],
                process.extractOne(text, RIGHT_WORDS)[1],
                process.extractOne(text, DOWN_WORDS)[1],
                process.extractOne(text, UP_WORDS)[1],
            ]
            action.direction = action_dirs[np.argmax(options)]
        return action
    output = help(text)
    log(f"action classified as:{output}")
    return output

def log(text):
    with open(action_classifier_log_file, 'a') as f:
        print(text, file=f)