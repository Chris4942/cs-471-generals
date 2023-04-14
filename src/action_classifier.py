import os
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
    text = text.replace('use your', 'u0')
    text = text.replace('and', 'n')
    text = text.replace('one', '1')
    text = letter_o_matcher.sub('o', text)
    text = ignore_matcher.sub('', text)
    text = a_fix_matcher.sub('a', text)
    log(f"post_preprocessed_text:\"{text}\"")
    return text

def classify_action(text) -> Action:
    def help(text):
        text = preprocess(text)
        matches = coord_matcher.findall(text)
        if len(matches) > 1:
            return Action(Goal.MOVE, starting_point=matches[0], destination_point=matches[1])
        if len(matches) == 1:
            return Action(Goal.MOVE, destination_point = matches[0])
        options = [
            process.extractOne(text, LEFT_WORDS)[1],
            process.extractOne(text, RIGHT_WORDS)[1],
            process.extractOne(text, DOWN_WORDS)[1],
            process.extractOne(text, UP_WORDS)[1],
        ]
        return action_dirs[np.argmax(options)]
    output = help(text)
    log(f"action classified as:{output}")
    return output

def log(text):
    with open(action_classifier_log_file, 'a') as f:
        print(text, file=f)