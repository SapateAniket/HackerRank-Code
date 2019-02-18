#!/bin/python

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    nbr_lst = list(i for i in range(p,m,-d))
    in_cash_cnt = (s - sum(nbr_lst))/m
    return len(nbr_lst) + in_cash_cnt
 


    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = raw_input().split()

    p = int(pdms[0])

    d = int(pdms[1])
