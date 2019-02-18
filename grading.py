#!/bin/python

import sys

def solve(grades):
    res = []
    for i in grades:
        if i < 38:
            res.append(i)
        else:
            nxt_mltpl = ((i/5) + 1)*
            if nxt_mltpl - i < 3:
                res.append(nxt_mltpl)
            else :
                res.append(i)
    return res

n = int(raw_input().strip())
grades = []
grades_i = 
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
for i in result : 