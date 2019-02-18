#!/bin/python

import sys

def getMoneySpent(keyboards, drives, s):
    if min(keyboards) + min(drives) > s:
        return '-1'
    while(1):
        ky, dr = max(keyboards), max(drives)
                
        if ky + dr < s:
            return ky + dr
            
        elif ky > dr:
            drives.remove(dr)
            dr = max(drives)

            keyboards.remove(ky)
            ky = max(keyboards)
        if keyboards==[] or drives==[]:
            return '-1'
            

s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]