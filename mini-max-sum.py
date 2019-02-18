#!/bin/python

import sys

data = map(int, raw_input().split(' '))

tot = sum(data)

print tot - max(data), tot - min(data)