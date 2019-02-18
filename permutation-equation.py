#!/bin/python

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    x=[]
    for i in range(1,len(p)+1):
        x.append(p.index(p.index(i)+1)+1)
    return x

if __name__ == '__main__':


    n = int(raw_input())

    p = map(int, raw_input().rstrip().split())

    result = permutationEquation(p)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')