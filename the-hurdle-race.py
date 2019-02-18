#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
height = map(int, raw_input().strip().split(' '))
mx_ht = max(height)
if mx_ht>k:
    print mx_ht - k
else:
    print 
