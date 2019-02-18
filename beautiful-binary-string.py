#!/bin/python

import sys

def minSteps(n, B):
    cnt = B.count('010')
    return cnt

n = int(raw_input().strip())
B = raw_input().strip()
result = minSteps(n, B)
print(result)
