#!/bin/python

import sys

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int, raw_input().strip().split(' '))
cnt = 
for i in range(n):
    for j in range(i+1,n):
        if (a[i] + a[j]) % k == 0:
#            print a[i], a[j]
            cnt = cnt + 
print cnt            
          
     
