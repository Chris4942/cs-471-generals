from re import compile

m = compile('(?<! \w) \d+(?= )')

print(m.findall(' the 200 '))
print(m.findall(' the 35 '))
print(m.findall(' all 200 '))