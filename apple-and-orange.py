#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))
apl_cnt, orn_cnt = 0, 
for i in apple:
    if (a+i) in range(s,t+1):


for j in orange:
    if (b+j) in range(s,t+1):
        orn_cnt = orn_cnt + 

print apl_cnt
print orn_cnt    
