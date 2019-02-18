#!/bin/python

import sys

def saveThePrisoner(n, m, s):
    return (m+s-1)%n

t = int(raw_input().strip())
for a0 in xrange(t):
    n, m, s = raw_input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)

