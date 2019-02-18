#!/bin/python
import calendar

import sys

def solve(year):
    if calendar.isleap(year):
        return '12.09.' + str(year)
    else:
        return '13.09.' + str(year)

year = int(raw_input().strip())
result = solve(year)
print(result)
