#!/bin/python

import sys


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())

if s==t:
    print 'Yes'
else:
    if len(s)>len(t):
        mx=len(t)
    else:
        mx=len(s)

    for i in range(mx):
        if s[i] != t[i]:
            df.append(s[i:])
            ind=i
            break
    #print i, df            
    if len(t)-i+len(df) <= k:
        print 'Yes'