#!/usr/bin/python

# frequency.py
# given word list, find top n words by frequency

words = 'cat, cat, dog, do, rr, rr, rr, apple, peach, pear, cat, pear, cat'
freq = {}

words = [each.strip() for each in words.split(',')]

for each in words:
    freq[each] = freq.get(each, 0) + 1

pairs = [(each,freq[each]) for each in freq]

print pairs

n = 3

finalpairs = []


for i in range(0, n):
    newmax = max(each[1] for each in pairs)

    # terrible
    for each in pairs:
        if each[1] == newmax:
            pairs.remove(each)
            finalpairs.append(each)
            break

print finalpairs
