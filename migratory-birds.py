#!/bin/python

import sys


n = int(raw_input().strip())
types = map(int, raw_input().strip().split(' '))
distnct = set(types)
mx_typ, cnt = 0, 
for i in distnct:
    if cnt < types.count(i):
        cnt = types.count(i)
        mx_typ = i
print mx_typ        
