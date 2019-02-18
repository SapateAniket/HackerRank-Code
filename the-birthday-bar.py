#!/bin/python

import sys

def getWays(squares, d, m):
    ways = 
    for i in range(len(squares)):
        if sum(squares[i:(i + m)]) == d:
            ways = ways + 
    return ways
       

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d,m = raw_input().strip().split(' ')
d,m = [int(d),int(m)]

print(result)
