LEFT_WORDS = [
    'left',
    'west',
]

RIGHT_WORDS = [
    'right',
    'east',
]

DOWN_WORDS = [
    'down',
    'south',
]

UP_WORDS = [
    'up',
    'north',
]

DIRECTION_WORDS = [
    *LEFT_WORDS,
    *RIGHT_WORDS,
    *DOWN_WORDS,
    *UP_WORDS,
]

SPREAD_OUT_WORDS = [
    'spread out'
]

INSTRUCTIONS = '''
    Example commands:
    - "Move up 5 (spaces)" -- It will default to the largest group of units if none is provided
    - "Move the (group of) 32 down"
    - "Move E10 to G12" -- Note: there is no path finding around obstacles
    - "Move the group of 90 to E10"
    - "Spread out" -- Moves all units in a random direction
'''