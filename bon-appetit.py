#!/bin/python

import sys

def bonAppetit(n, k, b, ar):
    actual = (sum(ar) - ar[k])/
    if actual == b:
        return 'Bon Appetit'
    else:
        return b - actual
        
    

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))

result = bonAppetit(n, k, b, ar)
print(result)
