#!/bin/python

import sys

x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
if x1 > x2 and v1 > v2 :
    print 'NO'
    sys.exit()
if x1 < x2 and v1 < v2 :
    print 'NO'
    sys.exit()
ahead = 'x1' if x1 > x2 else 'x2'
while(1):
    x1 = x1 + v
    x2 = x2 + v

    if x1 == x2:
        print 'YES'
        break
    elif x1 > x2 and ahead == 'x2':
        print 'NO'
        break
    elif x2 > x1 and ahead == 'x1':
        print 'NO'