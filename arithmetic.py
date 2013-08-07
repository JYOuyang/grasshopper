#!/usr/bin/python

# arithmetic.py
# evaluate arithmetic expressions

import re

sumexpr = '1+2+3+4'

print sum([int(each) for each in sumexpr.split('+')])

subexpr = '1+2-3-2'

addgrps = subexpr.split('+')

def intsub(grp):
    try:
        grp = int(grp.strip())

    except:
        grp = [int(elem) for elem in grp.split('-')]

        grp = grp[0] - sum(grp[1:])

    return grp

out = map(intsub, addgrps)

print sum(out)

subexpr = re.sub('([+-])', '.\g<0>', subexpr)
addgrps = [int(each) for each in subexpr.split('.')]

print sum(addgrps)
