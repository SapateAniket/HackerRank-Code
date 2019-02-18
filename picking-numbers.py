#!/bin/python

import sys

def pickingNumbers(a):
    no_set = list(set(a))
    no_cnt, cnt_lst = [], []
    mx_cnt = 
    for i in range(len(no_set)):
        no_cnt.append(a.count(no_set[i]))
    
    print no_set, no_cnt
    for i in range(len(no_set)-1):
        if no_set[i+1] -  no_set[i] <= 1 and (no_cnt[i] + no_cnt[i+1]) > mx_cnt :
            mx_cnt = no_cnt[i+1] + no_cnt[i]

            
    #print no_set, no_cnt
    return mx_cnt
        
if __name__ == "__main__":
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    result = pickingNumbers(a)
    print result