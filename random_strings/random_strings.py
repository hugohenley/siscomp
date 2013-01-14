__author__ = 'hugohenley'
from random import choice

TOTAL_STRINGS = 300
POSSIBLE_STRINGS = ["a", "b", "c"]

f = open('random_strings.txt', 'w')
i = 0
while i <= TOTAL_STRINGS:
    f.write(choice(POSSIBLE_STRINGS))
    i += 1