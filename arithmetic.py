#!/usr/bin/python

sumexpr = '1+2+3+4'

print sum([int(each) for each in sumexpr.split('+')])
