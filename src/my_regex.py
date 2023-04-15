
coord_regex = '(?<= )[a-z] ?[0-9]+'
spaces_regex = '(?<= )\d+(?= (?:space|tile|square|spot))' # ChatGPT wrote this one
group_regex = '(?<= )\d+(?! (?:space|tile|square|spot))' # ChatGPT also wrote this one...