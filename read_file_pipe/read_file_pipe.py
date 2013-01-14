__author__ = 'hugohenley'

file = open('random_strings.txt', 'r')
string = file.read()
print string.count('cba')