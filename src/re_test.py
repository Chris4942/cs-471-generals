from re import compile
from fuzzywuzzy import process
from my_regex import spaces_regex, group_regex

from word_lists import LEFT_WORDS

# spaces_matcher = compile('(?<= )\d+(?= (?:space|tile|square|spot))')
# group_matcher = compile('(?<= )\d+(?! (?:space|tile|square|spot))')

spaces_matcher = compile(spaces_regex)
group_matcher = compile(group_regex)

test_string = ' move left 7 spaces '


print(spaces_matcher.findall(test_string))
print(group_matcher.findall(test_string))