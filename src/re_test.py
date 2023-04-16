from re import compile
from fuzzywuzzy import process
from my_regex import spaces_regex, group_regex

from action_classifier import classify_action
from word_lists import LEFT_WORDS

# spaces_matcher = compile('(?<= )\d+(?= (?:space|tile|square|spot))')

# group_matcher = compile('(?<= )\d+(?! (?:space|tile|square|spot))')
action = classify_action("move the 112 up to spaces")
print(action)