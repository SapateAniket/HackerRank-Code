#!/bin/python

import math
import os
import random
import re
import sys

lst = []
x = input()
lst = map(int, raw_input().split())
upd_lst = []
for i in lst:
    upd_lst.append(abs(i))
upd_lst.sort()
print upd_lst[1] - upd_lst[0]
