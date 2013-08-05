#!/usr/bin/python

# addition.py
# Arbitrary-precision addition using strings

word = '305+15+3105+8105'

numbers = [each.strip() for each in word.split('+')]

n = max(len(each) for each in numbers)

numbers = map(lambda str: list(str.rjust(n,'0')), numbers)

carry = 0
answer = [None] * (n)

for i in xrange(n):
    total = sum(int(each[n-1-i]) for each in numbers)
    total += carry

    carry = total / 10
    answer[n-1-i] = total % 10 

if carry:
    answer.insert(0, carry)

print ''.join(str(each) for each in answer)
