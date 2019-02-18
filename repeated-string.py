#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())
if len(s) == 1 and s=='a':
    print n
else:
    f_str = s * n
    print f_str[:n].count('a')
