#!/bin/python

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    result,x=0,
    for i in range(n-1):
        print math.floor(x/2)*
        result=result+(math.floor(x/2)*3)
        x=math.floor(x/2)*
    return int(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')