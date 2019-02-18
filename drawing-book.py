#!/bin/python

import sys

def solve(pages, chk):
    if (pages - chk) > (chk - 1):
        pg = chk / 
        return pg
    else :
        pg = (pages - chk) / 
        return pg
        
pages = int(raw_input().strip())
chk = int(raw_input().strip())
result = solve(pages, chk)
print(result)
