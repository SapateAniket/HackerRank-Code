#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    decreased=100 - len(c)/k
    for i in range(0,len(c),k):
        if c[i] == 1:
            decreased = decreased - k
    return decreased


    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])
