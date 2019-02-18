#!/bin/python

import sys

def getRecord(s):
    high_cnt, low_cnt = 0, 
    mx,mn = s[0],s[0]
    for i in range(1,len(s)):
        if s[i] > mx:
            mx = s[i]
            high_cnt = high_cnt + 
        if s[i] < mn:
            mn = s[i]
            low_cnt = low_cnt + 
    return high_cnt,low_cnt            


s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))
