#!/usr/bin/python

words = ['cat', 'tac', 'god', 'dog', 'something']
mydict = {}

for each in words:
    s = ''.join(sorted(each))
    mydict.setdefault(s, []).append(each)

print mydict
