#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    x,cnt=0,
    while(True):
        if x + 2 < len(c) and c[x+2] == 0:
            x = x + 
        else:
            x = x + 

        if x == len(c) or x + 2 > len(c):
            break
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())