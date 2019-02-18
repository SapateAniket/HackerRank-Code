#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the weightedUniformStrings function below.
#
def weightedUniformStrings(s, queries):
    lst, lst_set, dic_list, weight_list = list(s), set(s), dict(), []
    for i in lst_set:
        dic_list[i] = lst.count(i)
        
    for key, value in dic_list.iteritems():

            if key*i in s:
                weight_list.append(ord(key)%96*i)
                #print(key*i)
    for i in queries:
        if i in weight_list:
            print('Yes')
        else:
            print('No')