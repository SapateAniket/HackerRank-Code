#!/bin/python

import sys


q = int(raw_input().strip())
chk_lst = ['h','a','c','k','e','r','r','a','n','k']
for a0 in xrange(q):
    s = raw_input().strip()
    pos = 
    indx = 
    for i in chk_lst:
        if i in s[indx:]:
            indx = s.index(i) + 
        else :
            indx = -

    if indx == -1:
        print 'NO'
    else:
        print 'YES'