#!/bin/python

import sys


S = raw_input().strip()
print len(S) - (S.count('S') + S.count('O'))

