
tile_words = "(?:space|tile|square|spot)"
coord_regex = '(?<= )[a-z] ?[0-9]+'
spaces_regex = f"(?<= )\d+(?= {tile_words})" # ChatGPT wrote this one
group_regex = f"(?<= )\d+(?! {tile_words})" # ChatGPT also wrote this one...